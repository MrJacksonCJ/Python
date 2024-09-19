import random
import art

def sacar_carta():
    return random.choice(cards)

def repartir_carta():
    for i in range(2):
        user_cards.append(sacar_carta())
        pc_cards.append(sacar_carta())

def calculo_suma(suma):
    return sum(suma)

def suma_pccards():
    suma_pc = calculo_suma(pc_cards)
    while suma_pc < 17:
        pc_cards.append(sacar_carta())
        suma_pc = calculo_suma(pc_cards)

def final():
    suma_user = calculo_suma(user_cards)

    while suma_user < 17:
        maso_bajo = input("Te recomendamos sacar otra carta quieres sacarla? 's' o 'n':").lower()
        if maso_bajo == "s":
            user_cards.append(sacar_carta())
            suma_user = calculo_suma(user_cards)
            blackjack()
            return
        else:
            break

    suma_pccards()
    suma_pc = calculo_suma(pc_cards)
    if suma_pc > 21:
        calculo_bust()
        return

    mostrar_cartas()

    if suma_pc == suma_user:
        print("Empate")
    elif suma_user < suma_pc:
        print("La casa gana")
    elif suma_pc < suma_user:
        print("Tu ganas")

def mostrar_cartas():
    suma_user = calculo_suma(user_cards)
    suma_pc = calculo_suma(pc_cards)
    print(f"            Tus barajas son {user_cards} y la suma de tus cartas es {suma_user}")
    print(f"            Las barajas de la casa son {pc_cards} y la suma es {suma_pc}")

def calculo_bust():
    suma_user = calculo_suma(user_cards)
    suma_pc = calculo_suma(pc_cards)
    if suma_pc > 21:
        print("\n")
        mostrar_cartas()
        print("bust. Tu ganas")
        return
    elif suma_user > 21:
        print("\n")
        mostrar_cartas()
        print("bust. La casa gana")
        return

def blackjack():
    while True:
        suma_pc = calculo_suma(pc_cards)
        suma_user = calculo_suma(user_cards)
        if suma_pc > 21 or suma_user > 21:
            calculo_bust()
            break
        elif suma_pc == 21:
            mostrar_cartas()
            print("la casa gana")
            break
        elif suma_user == 21:
            mostrar_cartas()
            print("Tu ganas")
            break
        print(f"            Tus cartas son {user_cards} y suma {calculo_suma(user_cards)}")
        print(f"            Las primera carta del pc es [{pc_cards[0]}] ")
        otra_carta = input("Quieres otra carta escribe 's' si pasas escribe 'n': ").lower()
        if otra_carta == "s":
            user_cards.append(sacar_carta())
        else:
            if suma_pc > 21 or suma_user > 21:
                calculo_bust()
                break
            final()
            break
    return

global user_cards, pc_cards,cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
while True:
    user_cards = []
    pc_cards = []
    print(art.logo)
    repartir_carta()
    blackjack()
    de_nuevo = input("\n Quieres jugar de nuevo? 's' o 'n'").lower()
    if de_nuevo == "s":
        print("\n" *20)
    else:
        break