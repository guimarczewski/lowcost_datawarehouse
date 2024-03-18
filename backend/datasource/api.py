import requests
import pandas as pd
import pyarrow.parquet as pq
import datetime
from io import BytesIO
from contracts.schema import GenericSchema, CompraSchema
from typing import List

class APICollector:
        def __init__ (self, schema, aws):
            self._schema = schema
            self._aws = aws
            self._buffer = None
            return

        def start(self, param):
            response = self.getData(param)
            response = self.extractData(response)
            response = self.transformDf(response)
            response = self.convertToParquet(response)

            if self._buffer is not None:
                file_name = self.fileName()
                print(file_name)
                # upload para a aws
                self._aws.upload_file(response, file_name)
                return True

            return False

        def getData(self, param):
            response = None
            if param > 1:
                response = requests.get(
                    f"https://8000-guimarczews-lowcostdata-tglj9m4hd9x.ws-us110.gitpod.io/gerar_compra/{param}"
                ).json()
            else:
                response = requests.get("https://8000-guimarczews-lowcostdata-tglj9m4hd9x.ws-us110.gitpod.io/gerar_compra").json()
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

        def transformDf(self, response):
            return pd.DataFrame(response)

        def convertToParquet(self, response):
            self._buffer = BytesIO()
            try:
                response.to_parquet(self._buffer)
                return self._buffer
            except:
                print("Erro ao transformar o DF em parquet")
                self._buffer = None

        def fileName(self):
            data_atual = datetime.datetime.now().isoformat()
            # remover as casas decimais do segundo
            match = data_atual.split(".")
            
            return f"api/api-response-compra{match[0]}.parquet"
