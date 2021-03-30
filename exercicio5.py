peso = float(input('Peso: '))
altura = float(input('Altura: '))

imc = peso / (altura*altura)

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 24.9:
    print('Peso normal')
elif imc > 24.9 and imc < 29.9:
    print('Sobrepeso')
elif imc >= 29.9 and imc < 39.9:
    print('Obesidade')
elif imc >= 39.9:
    print('Obesidade Severa')
