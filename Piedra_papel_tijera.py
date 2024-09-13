#Importamos la biblioteca random
import random
#Creamos 3 variables: opciones, jugador y la computadora
opciones = ("piedra", "papel", "tijera")
correr = True 

while correr:   
#Utilizamos un bucle  
# not in: operador de pertenencia evalúa como veradero si no encuentra una variable en la secuencia especificada
    jugador = None #None es un valor especial con falta de definición
    computadora = random.choice(opciones) #Choice: función que elige un valor al azar en un conjunto de elementos
    
    while jugador not in opciones:
        jugador = input("Elije pibe (piedra, papel o tijera):\n") #/n para dar salto de linea

    print(f"jugador:{jugador}") #Concatenar
    print(f"computadora:{computadora}") #Imprimimos

    if jugador == computadora:
        print("¡Es un empate!")
    elif jugador == "piedra" and computadora == "tijera":
        print("¡Ganaste!")
    elif jugador == "papel" and computadora == "piedra":
        print("¡Ganaste!") 
    elif jugador == "tijera" and computadora == "papel":
        print("¡Ganaste!")           
    else:
        print("¡Flasheaste confianza, perdiste!")
    
    if not input("¿Jugar otra vez? (si/no):\n").lower() == "si":
        correr = False
  
print("¡Gracias por jugar!")