"""
    Laboratorio 04
    author: Jorgeflowers18
"""
# librerias para trabajar con archivos y cadenas en python
import  json
import codecs
# creamos una variable con la cual abrir para leer el archivo txt
archivo = codecs.open("datos.txt", "r")
# creamos una variable para leer cada linea del archivo
data = archivo.readlines()
# variable en la cual convertimos todas las cadenas en diccionario con una complex list
dicry = [json.loads(l) for l in data]
# obtenemos solo las alturas en una lista
height = list(map(lambda x: list(x.items())[2][1], dicry))
# comparamos cada altura con las obtenidas anteriormmente buscando el mínimo y el máximo
maxi = lambda x: list(x.items())[2][1] == max(height)
minin = lambda x: list(x.items())[2][1] == min(height)
# imprimimos con un filter los que hayan obtenido mas de tres goles
print("\nLos jugadores que han hecho mas de 3 goles son:\n")
print(list(filter(lambda x: list(x.items())[1][1] > 3 , dicry)))
# imprmimos con un filter los jugadores de nigeria
print("\nLos jugadores que son de Nigeria son:\n")
print(list(filter(lambda x: list(x.items())[0][1] == "Nigeria", dicry)))
# imprimimos con las funciones anteriormente realizadas para el minimo y máximo los jugadores
print("\nEl jugador más alto es:\n")
print(list(filter(maxi, dicry)))
print("\nEl jugador más pequeño es:\n")
print(list(filter(minin, dicry)))



