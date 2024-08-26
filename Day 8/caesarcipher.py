import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ,'ñ','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cifrado_cesar(entrada, texto_original, clave):
    if entrada == "decodificar":
        clave = clave *-1
    texto_encriptado = ""
    for letra in texto_original:
        if letra in alphabet: # se resuelve bucles inecesarios, mas efectivo el programa
                    indice = alphabet.index(letra)
                    numero_clave= (indice + clave) % len(alphabet) #resolver debordamiento cuando sea y y z 
                    texto_encriptado += alphabet[numero_clave]
        else:
            texto_encriptado += letra #se agrega para que no codifique espacios ni letras ni simbolos

    print(f"Este es el texto {entrada}:\n {texto_encriptado}")

decision = "si"
print(art.logo)
while decision == "si": # se agrega para mantener el programa corriendo por si se necesita hacer algo mas
    direction = input("Escriba 'codificar' o 'decodificar' para hacer el mensaje:\n").lower()
    if direction == "codificar" or direction == "decodificar":
        text = input("Escriba su mensaje:\n").lower()
        shift = int(input("Escriba el numero de diferencia:\n"))
        cifrado_cesar(direction, text, shift)
        decision = input("Quieres seguir? Escribe 'si' o 'no': \n").lower()
    else:
        print("Lo que escribiste no tiene nada que ver")