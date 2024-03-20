# import json
import requests

def getAllGama():
    # json-server storage/gama_producto.json -b 5502
    peticion = requests.get()
    data = peticion.json()
    return data

def getAllNombre():
    gamaNombre = []
    for val in getAllGama():
        gamaNombre.append(val.get("gama"))
    return gamaNombre