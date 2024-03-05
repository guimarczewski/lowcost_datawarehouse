import requests
from contracts.schema import GenericSchema, CompraSchema
from typing import List

class APICollector:
        def __init__ (self, schema):
            self._schema = schema
            self._aws = None
            self._buffer = None
            return

        def start(self, param):
            response = self.getData(param)
            response = self.extractData(response)
            return response

        def getData(self, param):
            response = None
            if param > 1:
                response = requests.get(
                    f"https://8000-guimarczews-lowcostdata-tglj9m4hd9x.ws-us108.gitpod.io/gerar_compra/{param}"
                ).json()
            else:
                response = requests.get("https://8000-guimarczews-lowcostdata-tglj9m4hd9x.ws-us108.gitpod.io/gerar_compra").json()
            return response
        
        def extractData(self, response):
            result: List[GenericSchema] = []
            for item in response:
                index = {}
                for key, value in self._schema.items(): # fazer uma validação do contrato, se não estiver exclui
                    if type(item.get(key)) == value:
                        index[key] = item[key]
                    else:
                        index[key] = None

                result.append(index)

            return result

        def transformDf(self):
            return