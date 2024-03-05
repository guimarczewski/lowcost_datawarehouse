from datasource.api import APICollector
from contracts.schema import CompraSchema

schema = CompraSchema

minha_classe = APICollector(schema).start(1)

print(minha_classe)