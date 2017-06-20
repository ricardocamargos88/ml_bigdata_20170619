#conda install boto3
import boto3
import json
import pandas as pd
from datetime import datetime
 
def read_response(response):
     for val in response: 
         obj = json.loads(val['Data'].decode())
         lst_response.append(
                     [
                            obj['event_id'], 
                            obj['event_type'],
                            datetime.fromtimestamp(float(str(obj['datetime'])[0:10]))]    
                     );
       



client = boto3.client('kinesis', 
                      region_name = 'us-east-1',
                      aws_access_key_id = 'ACCESS KEY',
                      aws_secret_access_key = 'SECRET KEY')

shard_id = 'shardId-000000000000'

shard_iterator = client.get_shard_iterator(
        StreamName = 'big-data-analytics-desafio', 
        ShardId = shard_id, 
        ShardIteratorType = 'TRIM_HORIZON'        
        )['ShardIterator']

repeat = True

lst_response = []   

while(repeat):
    response = client.get_records(
              ShardIterator = shard_iterator,
              Limit = 10000
            )
    shard_iterator = response['NextShardIterator']
    
    valor = response['Records']
    
    if len(valor) > 0:
        read_response(valor)
        repeat = False;
        
k_data = pd.DataFrame(lst_response, columns=['event_id','event_type','datetime'])
k_data.to_csv(".\k_data.csv", sep='\t', index = False)

print('Processo finalizado...')