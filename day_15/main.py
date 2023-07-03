from random import randint

intentos = 0
adivinar = randint(1,100)

while intentos < 5:
    numero = int(input("Ingresa un número: "))
    intentos += 1
    if numero == adivinar:
        print("Correcto!")
        exit(0)
    
    if numero < adivinar:
        print("El número a adivinar es mayor")
    else:
        print("El número a adivinar es menor")

print("Ya no tienes intentos :c")