# Lista de palabras posibles para el juego.
word_list = ["doctor", "murcielago", "ornitorrinco"]

hangmanimg = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


# Importamos el módulo random para seleccionar una palabra aleatoria de la lista.
import random
chosen_word = random.choice(word_list)

# Construimos una representación inicial de la palabra con guiones bajos.
display = ["_" for _ in chosen_word]

# Número de intentos permitidos.
attempts = 6
indicador = 0
print(" ".join(display))
print(f"Tu palabra tiene {len(chosen_word)} letras.")
# Mientras queden intentos y la palabra no esté completamente adivinada.
while attempts > 0 and "_" in display:
    # Pedimos al usuario que adivine una letra y la convertimos a minúscula.
    guess = input("Escribe una letra: ").lower()

    # Verificamos si la letra adivinada está en la palabra elegida.
    if guess in chosen_word:
        print("Bien")
        # Actualizamos la representación con la letra adivinada si está en la palabra.
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
    else:
        print("Mal")
        # Reducimos el número de intentos si la adivinanza es incorrecta.
        attempts -= 1
        indicador +=1

    print(hangmanimg[indicador])

    # Imprimimos la representación actualizada de la palabra.
    print(" ".join(display))
    # Mostramos los intentos restantes.

# Verificamos si el usuario ha ganado o perdido.
if "_" not in display:
    print("Felicidades, Ganaste!")
else:
    print(f"Mal, perdiste. La palabra era: '{chosen_word}'.")
