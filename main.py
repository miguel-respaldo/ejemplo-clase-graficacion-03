def division():
    num1 = int(input("Dame un numero: "))
    num2 = int(input("Dame otro numero: "))
    print("La resta es:", num1 / num2)



def multiplicación():
    num1 = int(input("Dame un numero: "))
    num2 = int(input("Dame otro numero: "))
    print("La resta es:", num1 * num2)



def resta():
    numero1 = int(input("Dame un numero: "))
    numero2 = int(input("Dame otro numero: "))
    print("La resta es:", numero1 - numero2)



def suma():
<<<<<<< HEAD
    numero1 = int(input("Dame un numero: "))
    numero2 = int(input("Dame otro numero: "))
=======
    numero1 = int(input("Dame un número: "))
    numero2 = int(input("Dame otro número: "))
>>>>>>> parent of 03b48b6... jajaja ya te borre
    print("La suma es:", numero1 + numero2)



def menu():
    print("Menu de opciones")
    print("Seleccione una opción")
    print("1 Suma\n2 Resta\n3 Divicion\n 4 Divicion")

    return 2

if __name__ == '__main__':
    opcion = menu()
    if opcion == 1:
        suma()
<<<<<<< HEAD
=======
        suma()
>>>>>>> parent of 03b48b6... jajaja ya te borre
    elif opcion == 2:
        resta()
    elif opcion == 3:
        multiplicación()
    elif opcion == 4:
        division()
