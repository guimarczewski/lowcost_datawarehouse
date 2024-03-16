from datasource.api import APICollector
from datasource.postgre import PostgresCollector
from contracts.schema import CompraSchema
from tools.aws.client import S3Client

import time
import schedule

schema = CompraSchema
aws = S3Client()

minha_classe = APICollector(schema, aws).start(500)
print(minha_classe)
#def apiCollector(schema, aws, repeat):
#    response = APICollector(schema, aws).start(repeat)
#    print("Finalizado")
#    return

# schedule.every(1).minutes.do(apiCollector,schema, aws, 50)


# while True:
#     schedule.run_pending()
#     time.sleep(1)

#def getPostgre(aws, dbId):
#    postgres = PostgresCollector(aws, dbId).start()

#getPostgre(aws, dbId=1)
#getPostgre(aws, dbId=2)