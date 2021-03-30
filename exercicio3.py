x = float(input('Insira o valor de x: '))

if x <= 1:
    retorno = 1
elif x > 1 and x <= 2:
    retorno = 2
elif x > 2 and x <= 3:
    retorno = x * x
elif x > 3:
    retorno = x * x * x

print(retorno)
