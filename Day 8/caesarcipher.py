alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ,'ñ','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Escriba 'codificar' o 'descodificar' para hacer el mensaje:\n").lower()
text = input("Escriba su mensaje:\n").lower()
shift = int(input("Escriba el numero de diferencia:\n"))

#crear la funcion con el llamado de 2 variables
def codificar(texto_codificado, clave):
    texto_encriptado = ""
    for letra in text:
        for letra_2 in alphabet:
            if letra == letra_2:
                    indice = alphabet.index(letra_2)
                    numero_clave= indice + shift
                    texto_encriptado += alphabet[numero_clave]
    print(texto_encriptado)



codificar(text, shift)