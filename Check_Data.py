dia = mes = ano = ind_e = 0
dm = [00, 31, 28, 31, 30, 31, 30 ,31, 31, 30, 31, 30, 31]
dia = int(input("Dia: "))
mes = int(input("Mes: "))
ano = int(input("Ano: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    dm[2] = 29
else: dm[2] = 28

if mes < 1 or mes > 12:
    ind_e = 1
else:    
    if dia < 1 or dia > dm[mes]:
        ind_e = 1
if ano < 0:
    ind_e = 1

if ind_e == 1:
    print("Data invalida")
else: print("Data valida")

        