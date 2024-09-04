import art

print(art.logo) #se imprime el logo para iniciar

continuar = True
binder = {}

#inicializar variables

while continuar == True:
    name = input("Cual es tu nombre? ")
    price = input("Cual es su puja? $")
    binder [name] = price
    more_binders = input("Hay mas personas participando?  Escribe 'si o no'. \n ").lower()

    if more_binders == "no":
        continuar = False
        precio_alto = max(binder.values())
        for x , y in binder.items(): #se busca la clave comparando el value
            if y == precio_alto:
                nombre_puja = x
    else:
        print("\n" *20) #se limpia pantalla
print(f"El ganador de la puja es {nombre_puja} con un valor de ${precio_alto}.")

