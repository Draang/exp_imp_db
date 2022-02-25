#importancion de paquetes
from pymongo import MongoClient #Cliente para Mongo
import random #Generar aleatorio
import time #usar un Delay

#Simular captura de datos de un sensor y enviarla a mongo

#Generar la conexion con el servidor
client = MongoClient(host='localhost', port=27017)

print("ejecutando...")
limite = 0

while True:
    #Simulacion de la lectura de la temperatura
    rad1 = random.randint(0, 500)
    rad2 = random.randint(100, 1500)
    rad3 = random.randint(0, 100)
    #genera objeto Json con los datos de interes
    valor1 = {
        'Nombre':'Linea Roja',
        'Nivel de Peligro':'Alto',
        'Estaciones':'16',
        'Rediacion':rad1
    }

    valor2 = {
        'Nombre':'Conjunto de estaciones independientes',
        'Nivel de Peligro':'Indeterminable',
        'Estaciones':'6',
        'Rediacion':rad2
    }

    valor3 = {
        'Nombre':'Hanza',
        'Nivel de Peligro':'Bajo',
        'Estaciones':'20',
        'Rediacion':rad3
    }

    #conectar a la base de datos
    db = client['Reg_Radiacion_Metro']
    #genera la coleccion
    coleccion_1_data = db['Linea_Roja']
    #inserta un dato en la coleccion
    coleccion_1_data.insert_one(valor1)
    #presentacion
    print('LR:', valor1)

    coleccion_2_data = db['Estaciones_Independientes']
    #inserta un dato en la coleccion
    coleccion_2_data.insert_one(valor2)
    #presentacion
    print('EI', valor2)

    coleccion_3_data = db['Hanza']
    #inserta un dato en la coleccion
    coleccion_3_data.insert_one(valor3)
    #presentacion
    print('H', valor3)

    #añadir un delay de medio segundo
    time.sleep(0.1)

    limite = limite + 1

    if limite == 990:
        break
