# ml_bigdata_20170619

Este projeto de ETL tem por objetivo ler dados de duas fontes distintas, as fontes de dados são as seguintes:
1) MySQL
    Esta fonte contém dados de produtos e pedidos realizados, possui 3 tabelas sendo (products, orders e orderitem).
    Products -> Registro de todos os produtos;
    Orders -> Registro dos pedidos, valores dos pedidos e local do pedido;
    Orderitem -> Registros dos produtos e valores no pedido;
2) AWS - Kinesis
    Esta fonte de dados contém os eventos relacionados à e-mails enviados. O eventos podem ser os seguines:
    Sent -> Registo do envio do e-mail;
    Opened -> Registro da abertura do e-mail;
    Clicked -> Registro do acesso ao item enviado do e-mail;
      
O processo de ETL contém 2 arquivos:
1) MySQL.py -> Este processo é o responsável por coletar os dados na base MySQL e gerar um CSV para cada tabela da fonte de dados;
2) Kinesis.py -> Este processo é o responsável por coletar os eventos de streaming no AWS;

Para a execução do processo de ETL é necessário a instalação das seguintes dependências:
1) Biblioteca boto3;    
2) mysql-connector;

Também para a execução do processo, é necessário parametrizar os dados de acesso ao banco MySQL e ao AWS. Estes dados devem estar configurados no ambiente onde será executado.

O processo, por ser público, tem por finalidade gerar arquivos CSV. Esses arquivos são de fácil manuseio para alimentar ferramentas de visualização de dados pois não requerem instalação de nenhum outro software.
