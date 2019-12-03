#!/usr/bin/python3
# -*- coding: UTF-8 -*-

ordenado = float(input('Qual valor do seu ordenado/hora? '))
horatrabalho = float(input('Quantas horas você trabalha por mês? '))
bruto = ordenado * horatrabalho
irrf = bruto * 0.2
inss = bruto * 0.11
sindicato = bruto * 0.05
liquido = bruto - (irrf + inss + sindicato)
print('Salário Bruto: ..........R$', bruto)
print('IRRF (20%): .............R$', irrf)
print('INSS (11%): .............R$', inss)
print('Sindicato (5%): .........R$', sindicato)
print('Salário Liquido: ........R$', liquido)

