#! python3
import sys
import random #libreria que permite generar numeros aleatorios

numInferior = random.randint(1,5) #numero inferior entre
numSuperior= random.randint(6,10) #numero superior entre
intentos= random.randint(1,14) #numero de intentos entre 1 y 10
secretNumber = random.randint(numInferior, numSuperior) #Numero a adviniar con rango
numeroElegido = 0 #numero del usuario
userName=0

print ("Bienvenido a:\n\n -///Adivina el numero///-\n")
print ("Como te llamas?\n")
userName=input()
print ("Hola " + userName + "!!!\n\nEl objetivo es adivinar el numero entre " + str(numInferior), end="")
print (" y " + str(numSuperior) + " que estoy pensando en " + str(intentos) + " intentos\n")

print("Elije un numero entre " + str(numInferior), end="")
print(" y " + str(numSuperior)+":")
print(" ")

for i in range (intentos):
    try:
        numeroElegido=input()
            
        if (int(numeroElegido)<numInferior)or(int(numeroElegido)>numSuperior):
            print(userName + "... Te fuiste a la re verga")
            
        elif (int(numeroElegido)<secretNumber) and (int(numeroElegido)>=numInferior):
            print("Un poco mas alto " + userName)
            
        elif (int(numeroElegido)>secretNumber) and (int(numeroElegido)<=numSuperior):
            print("Un poco mas abajo " + userName)
        
        else:
            break #This condition is for the correct answer

    except ValueError:
       print("Eso no es un numero " + userName + ", perdiste una oportunidad. Intenta nuevamente")

if secretNumber == int(numeroElegido):
    print(str(secretNumber) + " es el numero indicado. Felicitaciones " + userName + "!!!!")
else:
    print("El numero era: " + str(secretNumber) + " mejor suerte para la proxima " + userName)


        
