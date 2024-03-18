from datasource.postgre import PostgresCollector
from tools.aws.client import S3Client

aws = S3Client()

def getPostgre(aws, dbId):
    postgres = PostgresCollector(aws, dbId).start()

# database 1
getPostgre(aws, dbId=1)

# database 2
getPostgre(aws, dbId=2)