#importancion de paquetes
from pymongo import MongoClient #Cliente para Mongo
import random #Generar aleatorio
import time #usar un Delay

#Simular captura de datos de un sensor y enviarla a mongo

#Generar la conexion con el servidor
client = MongoClient(host='localhost', port=27017)

print("ejecutando...")

#conectar a la base de datos
db = client['Reg_Radiacion_Metro']
#genera la coleccion
linea_roja = db['Linea_Roja'] 
hanza = db['Hanza']
estaciones_independientes = db['Estaciones_Independientes']

for i in range(990):
    #Simulacion de la lectura de la temperatura
    rad1 = random.randint(0, 500)
    rad2 = random.randint(100, 1500)
    rad3 = random.randint(0, 100)
    #genera objeto  con los datos de interes
    VALOR_1 = {
        'Nombre':'Linea Roja',
        'Nivel de Peligro':'Alto',
        'Estaciones':'16',
        'Rediacion':rad1
    }
    VALOR_2 = {
        'Nombre':'Conjunto de estaciones independientes',
        'Nivel de Peligro':'Indeterminable',
        'Estaciones':'6',
        'Rediacion':rad2
    }
    VALOR_3 = {
        'Nombre':'Hanza',
        'Nivel de Peligro':'Bajo',
        'Estaciones':'20',
        'Rediacion':rad3
    }

   
  
    linea_roja.insert_one(VALOR_1)
  
    print('LR:', VALOR_1)
    
    #inserta un dato en la coleccion
    estaciones_independientes.insert_one(VALOR_2)
    print('EI', VALOR_2)

   
    #inserta un dato en la coleccion
    hanza.insert_one(VALOR_3)
  
    print('H', VALOR_3)

    #añadir un delay de medio segundo
    time.sleep(0.1)
