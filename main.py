def division():
    num1 = int(input("Dame un numero: "))
    num2 = int(input("Dame otro numero: "))
    print("La resta es:", num1 / num2)



def multiplicación():
    num1 = int(input("Dame un numero: "))
    num2 = int(input("Dame otro numero: "))
    print("La resta es:", num1 * num2)



def resta():
    num1 = int(input("Dame un numero: "))
    num2 = int(input("Dame otro numero: "))
    print("La resta es:", num1 - num2)



def suma():
    num1 = int(input("Dame un numero: "))
    num2 = int(input("Dame otro numero: "))
    print("La suma es:", num1 + num2)



def menu():
    print("Menu de opciones")
    print("Seleccione una opción")

    return 2

if __name__ == '__main__':
    opcion = menu()
    if opcion == 1:
        suma()
        suma()
    elif opcion == 2:
        resta()
    elif opcion == 3:
        multiplicación()
    elif opcion == 4:
        division()