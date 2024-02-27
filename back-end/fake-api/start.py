from fastapi import FastAPI

app = FastAPI()

@app.get("/gerar_compra")
async def gerar_compra():
    return {
        "client": "Nome",
        "creditcard": "Tipo de Cartao",
        "ean": "Codigo de barra do produto",
        "price": "Preco do produto",
        "store": 11,
        "dateTime": "Data da compra",
        "clientPosition": "Posicao do cliente"
    }
