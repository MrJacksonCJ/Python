alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ,'ñ','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Escriba 'codificar' o 'decodificar' para hacer el mensaje:\n").lower()
text = input("Escriba su mensaje:\n").lower()
shift = int(input("Escriba el numero de diferencia:\n"))

def cifrado_cesar(entrada, texto_original, clave):
    if entrada == "decodificar":
        clave = clave *-1
    texto_encriptado = ""
    for letra in texto_original:
        if letra in alphabet: # se resuelve bucles inecesarios, mas efectivo el programa
                    indice = alphabet.index(letra)
                    numero_clave= (indice + clave) % len(alphabet) #resolver debordamiento cuando sea y y z 
                    texto_encriptado += alphabet[numero_clave]
    print(texto_encriptado)

cifrado_cesar(direction, text, shift)