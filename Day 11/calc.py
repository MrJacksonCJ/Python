import art


def add(n1, n2):
    return n1 + n2

def restar(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    return n1 / n2

operadores = {
    "+" : add,
    "-" : restar,
    "*" : multiplicar,
    "/" : dividir
}

calcular = True

while calcular:
    print(art.logo)
    numero_1 = float (input("Cual es el primer numero?: "))
    num_continua = True
    while num_continua:
        operar = input(" + \n - \n * \n / \n Escoge una operacion: ")
        numero_2 = float (input("Cual es el segundo numero?: "))
        resultado = operadores[operar](n1 = numero_1, n2 = numero_2)
        print(f"{numero_1} + {numero_2} = {resultado}")
        decision = input(f"Escribe 's' para continuar calculando con {resultado}, o escribe 'n' para hacer un nuevo calculo: ").lower()
        if decision == "s":
            numero_1 = resultado
        elif decision == "n":
            num_continua = False
            print("\n" * 20)
        else:
            print("No es valido")

