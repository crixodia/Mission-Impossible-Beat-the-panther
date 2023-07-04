# Día 15: El Adivinador de Números

Historia: Eres un adivinador profesional que ha sido desafiado a adivinar un número secreto. Tienes un máximo de 5 intentos para adivinar el número correcto. Después de cada intento, recibirás una pista para ayudarte a acercarte al número secreto.

Instrucciones:

1. Escribe un programa que genere un número aleatorio entre 1 y 100 como el número secreto.
2. Pídele al usuario que ingrese un número como su intento.
3. Compara el número ingresado con el número secreto y muestra un mensaje indicando si el número ingresado es mayor, menor o igual al número secreto.
4. Repite los pasos 2 y 3 hasta que el usuario adivine el número secreto o se queden sin intentos.

- [Día 15: El Adivinador de Números](#día-15-el-adivinador-de-números)
  - [Contexto](#contexto)
  - [Solución](#solución)
  - [Ejecución](#ejecución)
  - [Resultados](#resultados)

## Solución

´´´python
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
´´´