alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ,'ñ','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Escriba 'codificar' o 'decodificar' para hacer el mensaje:\n").lower()
text = input("Escriba su mensaje:\n").lower()
shift = int(input("Escriba el numero de diferencia:\n"))

#crear la funcion con el llamado de 2 variables
def codificar(texto_codificado, clave):
    texto_encriptado = ""
    for letra in text:
        if letra in alphabet: # se resuelve bucles inecesarios, mas efectivo el programa
                    indice = alphabet.index(letra)
                    numero_clave= (indice + shift) % len(alphabet) #resolver debordamiento cuando sea y y z 
                    texto_encriptado += alphabet[numero_clave]
    print(texto_encriptado)

def decodificar(texto_codificado, clave):
    texto_encriptado = ""
    for letra in text:
        if letra in alphabet: # se resuelve bucles inecesarios, mas efectivo el programa
                    indice = alphabet.index(letra)
                    numero_clave= (indice - shift) % len(alphabet) #resolver debordamiento cuando sea y y z 
                    texto_encriptado += alphabet[numero_clave]
    print(texto_encriptado)


def cifrado_cesar(entrada):
    if entrada == "codificar":
        codificar(text, shift)
    elif entrada == "decodificar":
        decodificar(text, shift)
    else:
        print("Intenta de nuevo")

cifrado_cesar(direction)