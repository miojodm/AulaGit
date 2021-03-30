print('Primeira Data')
dia1 = int(input('Dia: '))
mes1 = int(input('Mes: '))
ano1 = int(input('Ano: '))

print('Segunda Data')
dia2 = int(input('Dia: '))
mes2 = int(input('Mes: '))
ano2 = int(input('Ano: '))

dataMaior = 0

if ano1 < ano2:
    dataMaior = 1
if ano1 == ano2:
    if mes1 < mes2:
        dataMaior = 1
    elif mes2 < mes1:
        dataMaior = 2
    else:
        if dia1 < dia2:
            dataMaior = 1
        elif dia2 < dia1:
            dataMaior = 2
if ano2 < ano1:
    dataMaior = 2

if dataMaior == 1:
    print('Data 1 maior')
elif dataMaior == 0:
    print('Datas iguais')
else:
    print('Data 2 maior')
