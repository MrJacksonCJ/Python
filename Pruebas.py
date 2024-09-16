import art
import random

def calcular_suma(cartas):
    """Función para calcular la suma de las cartas."""
    return sum(cartas)

def mostrar_estado_usuario():
    """Muestra las cartas y la suma actual del usuario."""
    suma_usuario = calcular_suma(user_cards)
    primera_carta_maquina = pc_cards[0]
    print(f"         Tus cartas: {user_cards}, suma actual: {suma_usuario}")
    print(f"         Primera carta de la máquina: [{primera_carta_maquina}]")

def turno_maquina():
    """Lógica de la máquina para sacar cartas hasta que su suma sea al menos 17."""
    while calcular_suma(pc_cards) < 17:
        pc_cards.append(rand_card())

def final():
    """Función que maneja el final del juego."""
    suma_usuario = calcular_suma(user_cards)
    suma_maquina = calcular_suma(pc_cards)

    print(f"         Tus cartas: {user_cards}, tu suma: {suma_usuario}")
    print(f"         Cartas de la máquina: {pc_cards}, suma de la máquina: {suma_maquina}")

    if suma_usuario > 21:
        print(f"Perdiste, tu suma es {suma_usuario} y la de la máquina es {suma_maquina}. La casa gana.")
    elif suma_maquina > 21:
        print(f"Ganaste, tu suma es {suma_usuario} y la de la máquina es {suma_maquina}.")
    elif suma_maquina > suma_usuario:
        print(f"Perdiste, la suma de la máquina es {suma_maquina} y tu suma es {suma_usuario}. La casa gana.")
    elif suma_maquina < suma_usuario:
        print(f"Ganaste, tu suma es {suma_usuario} y la de la máquina es {suma_maquina}.")
    else:
        print(f"Es un empate. Tu suma: {suma_usuario}, suma de la máquina: {suma_maquina}.")

def rand_card():
    """Función para obtener una carta aleatoria."""
    return random.choice(cards)

# Juego completo en bucle
def jugar_blackjack():
    print(art.logo)

    # Inicialización de las cartas
    global user_cards, pc_cards,cards
    user_cards = []
    pc_cards = []
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # Repartir dos cartas al jugador y a la máquina
    for _ in range(2):
        user_cards.append(rand_card())
        pc_cards.append(rand_card())

    mostrar_estado_usuario()

    # Ciclo de toma de decisiones del jugador
    intento = True
    while intento:
        o_intento = input("Escribe 's' para sacar otra carta, 'n' para pasar: ").lower()

        if o_intento == "s":
            user_cards.append(rand_card())
            mostrar_estado_usuario()

            # Verificar si el usuario ha perdido inmediatamente
            if calcular_suma(user_cards) > 21:
                print(f"Te pasaste de 21. Perdiste.")
                intento = False
        elif o_intento == "n":
            turno_maquina()
            final()
            intento = False
        else:
            print("El valor ingresado no es válido.")

# Bucle principal del juego
while True:
    jugar_blackjack()
    jugar_de_nuevo = input("¿Quieres jugar otra vez? Escribe 's' para sí o 'n' para no: ").lower()
    if jugar_de_nuevo != "s":
        print("Gracias por jugar. ¡Hasta luego!")
        break
