from fastapi import FastAPI
from faker import Faker
import pandas as pd
import random

app = FastAPI()
fake = Faker()

lojapadraoonline = 11

file_name = 'backend/fakeapi/products.csv'
df = pd.read_csv(file_name, sep=",")
df['index'] = range(1, len(df) + 1)
df.set_index('index', inplace=True)

@app.get("/gerar_compra")
async def gerar_compra():
    index = random.randint(1, len(df) - 1)
    tuple = df.iloc[index]
    return [
        {
            "client": fake.name(),
            "creditcard": fake.credit_card_provider(),
            "product": tuple["Product Name"],
            "ean": int(tuple["EAN"]),
            "price": round(float(tuple["Price"]) * 1.2, 2), 
            "clientPosition": fake.location_on_land(),
            "store": lojapadraoonline,
            "dateTime": fake.iso8601(),
        }
    ]

@app.get("/gerar_compra/{numero_registro}")
async def gerar_compra(numero_registro: int):

    if numero_registro < 1:
        return {"Error": "Numero de registros precisa ser maior que 1"}
    
    respostas = []
    for _ in range(numero_registro):
        index = random.randint(1, len(df) - 1)
        tuple = df.iloc[index]
        compra = {
                "client": fake.name(),
                "creditcard": fake.credit_card_provider(),
                "product": tuple["Product Name"],
                "ean": int(tuple["EAN"]),
                "price": round(float(tuple["Price"]) * 1.2, 2), 
                "clientPosition": fake.location_on_land(),
                "store": lojapadraoonline,
                "dateTime": fake.iso8601(),
        }
        respostas.append(compra)

    return respostas
    

        