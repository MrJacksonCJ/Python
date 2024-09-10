def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    cuatrocientos = year % 400
    cien = year % 100
    cuatro = year % 4
    biciesto = None
    if cuatrocientos == 0:
        biciesto = True #Divisible por 400
    elif cuatro == 0 and not cien ==0:
        biciesto = True #Divisible por 4 pero no por 100
    elif cien == 0 and not cuatrocientos ==0:
        biciesto = False #Divisible por 100 pero no por 400
    else:
        biciesto = False
    return biciesto


print(is_leap_year(int(input("Escribe el año: "))))