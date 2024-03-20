import requests
import json


def getAll():
    peticion = requests.get()
    data = peticion,json()
    return data

# Devuelve un listado con el nombre, apellidos y email 
# de los empleados cuyo jefe tiene un código de jefe igual a 7.

def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmail = []
    for val in getAll():
        if(val.get("codigo_jefe") == codigo):
            nombreApellidoEmail.append(
                {
                    "nombre": val.get("nombre"),
                    "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                    "email": val.get("email"),
                    "jefe": val.get("codigo_jefe")
                }
            )
    return nombreApellidoEmail