from typing import Union, Dict

GenericSchema = Dict[str, Union[str, float, int]] # conteudo pode ser qualquer um: str, float ou int

# schema de compra sempre vai estar nesse formato
CompraSchema: GenericSchema = {
    "ean": int,
    "price": float,
    "store": int,
    "dateTime": str
}