import art
import random
import game_data

def sacar_famoso():
    return random.choice(game_data.data)

def comparar():
    if famoso_a['follower_count'] > famoso_b['follower_count']:
        return famoso_a['follower_count']
    elif famoso_b['follower_count'] > famoso_a['follower_count']:
        return famoso_b['follower_count']



#se escoge aleatorio el famoso
famoso_a = sacar_famoso()
score = 0
print(art.logo)
while True:
    famoso_b = sacar_famoso()
    #se imprime los famosos escogidos
    print(f"Compare A: {famoso_a['name']} a {famoso_a['description']}, from {famoso_a['country']}")
    print(art.vs)
    print(f"Against B: {famoso_b['name']} a {famoso_b['description']}, from {famoso_b['country']}")
    comparado = input("Who has more followers? Type 'A' or 'B': ").lower()
    #se trae el numero de followers a una variable para comparar
    if comparado == "a":
        escogido = famoso_a['follower_count']
    else:
        escogido = famoso_b['follower_count']
    #se compara
    if escogido == comparar():
        score += 1
        if comparado == "b":
            famoso_a = famoso_b
        print(art.logo)
        print(f"You're right! Current score: {score}.")
    else:
        print("\n"*20 , art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        break
