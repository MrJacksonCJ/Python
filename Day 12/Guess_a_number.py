import random
import art

def level_escoger(dificulty):
        if dificulty == "facil":
            return 10
        else:
            return 5

def evaluar_numero(num_escogido):

    if num_escogido < numero:
        print("Muy bajo")
    elif numero_escogido > numero:
        print("Muy alto")
    return -1

print(art.logo)
global numero

numero = random.randint(1,100)
print("Estoy pensando un numero entre 1 y 100.")
dificultad = input("Escoje una dificultad: Escribe 'facil' o 'dificil': ").lower()
intentos = level_escoger(dificultad)
while intentos != 0:
    print(f"Tienes {intentos} intentos para adivinarlo")
    numero_escogido = int(input("Escribe un numero: "))
    intentos += evaluar_numero(numero_escogido)
    if numero_escogido == numero:
        print(f"Lo adivinaste! El numero era {numero_escogido}.")
        break
    else:
        if intentos >=1:
          print("Intenta de nuevo")
if intentos== 0:
    print("Ya no tienes mas intentos")