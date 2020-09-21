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


if __name__ == '__main__':
    suma()
    resta()
    multiplicación()