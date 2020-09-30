def division():#Function that make a division
    num1 = int(input("Dame un numero: "))
    num2 = int(input("Dame otro numero: "))
    print("La resta es:", num1 / num2)

def multiplicación():#Function that make a multiplication
    num1 = int(input("Dame un numero: "))
    num2 = int(input("Dame otro numero: "))
    print("La resta es:", num1 * num2)

def resta():#Function that make a substraction
    numero1 = int(input("Dame un numero: "))
    numero2 = int(input("Dame otro numero: "))
    print("La resta es:", numero1 - numero2)

def suma():#This step publish a sum
    numero1 = int(input("Dame un número: "))
    numero2 = int(input("Dame otro número: "))
    print("La suma es:", numero1 + numero2)

def menu():
    print("Menu de opciones")
    print("Seleccione una opción")
    print("1 Suma\n2 Resta\n3 Divicion\n 4 Divicion")

    return 2

if __name__ == '__main__':
    opcion = menu()
    if opcion == 1:#This step publish a sum
        suma()
        suma()
    elif opcion == 2:#This step publish a substraction
        resta()
    elif opcion == 3:
        multiplicación()#This step publish multiplication
    elif opcion == 4:
        division() #By last in this step finish whit a division
