numero1 = int(input('Insira o primeiro número: '))
numero2 = int(input('Insira o segundo número: '))
numero3 = int(input('Insira o terceiro número: '))
print('Hello World!')

if numero1 < numero2 and numero1 < numero3:
    print(numero1)
    if numero2 < numero3:
        print(numero2)
        print(numero3)
    else:
        print(numero3)
        print(numero2)
if numero2 < numero1 and numero2 < numero3:
    print(numero2)
    if numero1 < numero3:
        print(numero1)
        print(numero3)
    else:
        print(numero3)
        print(numero1)
if numero3 < numero1 and numero3 < numero2:
    print(numero3)
    if numero1 < numero2:
        print(numero1)
        print(numero2)
    else:
        print(numero2)
        print(numero1)
