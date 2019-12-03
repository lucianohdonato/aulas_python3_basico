#!/usr/bin/python3
#-*- coding: UTF-8 -*-

dm = [00, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ind_erro = dia = mes = ano = 0
dia = input("Digite o dia da admissão: ")
mes = input("Digite o mês da admissão: ")
ano = input("Digite o ano da admissão: ")

if dia.isdigit():
    dia = int(dia)
else: dia = 0
if mes.isdigit():
    mes = int(mes)
else: mes = 0
if ano.isdigit():
    ano = int(ano)
else: ano = 0

if dia < 1 or ano < 1 or mes < 1 or mes > 12:
    ind_erro = 1
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    dm[2] = 29
else: dm[2] = 28
if ind_erro == 0:
    if dia > dm[mes]:
        ind_erro = 1

if ind_erro == 1:
    print("A data {}/{}/{} é inválida".format(dia,mes,ano))
else: print("A data {}/{}/{} esta correta".format(dia,mes,ano)
