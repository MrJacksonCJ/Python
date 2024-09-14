import art
import random

def calculo():
    suma_cards = 0
    for i in user_cards:
        suma_cards += i
    maquina = pc_cards[0]
    print(f"         Tus cartas: {user_cards}, suma actual: {suma_cards}")
    print (f"         Primera carta de la maquina: [{maquina}]")

def Final():
    suma_cards = 0
    suma_cards2 = 0
    for i in user_cards:
        suma_cards += i
    for i in pc_cards:
        suma_cards2 += i
    if suma_cards <= 17:
        print("Debes escojer  otra carta")
        return 0
    elif suma_cards2 <= 17 :
        pc_cards.append(rand_card())


    print(f"         Tus cartas: {user_cards}, Tu  suma: [{suma_cards}]")
    print (f"         Cartas de la maquina {pc_cards}, Suma de la maquina: [{suma_cards2}]")
    if suma_cards > 21:
        print(f"Perdiste tu maso suma {suma_cards} y el de el pc {suma_cards2}, por lo tanto la casa gana. ")
    elif suma_cards2 > 21:
        print(f"Ganaste tu maso suma {suma_cards} y el de el pc {suma_cards2}. ")
    elif suma_cards2 > suma_cards:
        print(f"Perdiste tu maso suma {suma_cards} y el de el pc {suma_cards2}, por lo tanto la casa gana. ")
    elif suma_cards2 <= 17 :
        pc_cards.append(rand_card())
        Final()
    else:
        print(f"Ganaste tu maso suma {suma_cards} y el de el pc {suma_cards2}. ")

def rand_card():
    ini_card = random.choice(cards)
    return ini_card

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
pc_cards = []

rand_blackjack = True

while rand_blackjack:
    if len(user_cards) == 0 or len(user_cards) == 1 :
        user_cards.append(rand_card())
    if len(pc_cards) == 0 or len(pc_cards) == 1 :
        pc_cards.append(rand_card())
    if len(user_cards) == 2 and len(pc_cards) == 2:
        rand_blackjack = False


intento = True
calculo()
while intento:
    o_intento = input("Escribe 's' para sacar otra carta, 'n' para pasar:").lower()

    if o_intento == "s":
        user_cards.append(rand_card())
        calculo()
    elif o_intento == "n":
        de_nuevo = Final()
        if de_nuevo == 0:
             intento = True
        else:
            intento = False
    else:
        print("El valor ingresado no es valido")