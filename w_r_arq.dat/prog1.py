#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# prog1.py

ind_erro = codigo = dia = mes = ano = salario = 0
dm = [00, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
nome = " "
digita = "s"

import struct
arquivo = open("arq_func.dat","wb")

while codigo != 9999:
    digita = "s"
    while digita == "s":
        codigo = input("\nDigite o código do funcionário: ")
        ind_erro = 0
        if codigo.isdigit():
            codigo = int(codigo)
        else: codigo = 0
        if codigo == 9999:
            ind_erro = 1
            break
        if codigo <= 0: ind_erro = 1
        digita = "?"
        if ind_erro == 1:
            while digita != "s" and digita != "n":
                digita = input("Código inválido. Corrigir? (s/n) ")

    if ind_erro == 0:
        digita = "s"
        while digita == "s":
            nome = input("\nDigite o nome do funcionário: ")
            ind_erro = 0
            if nome == "": nome = " "
            if len(nome) > 30: 
                ind_erro = 1
                print("Limite de 30 letras estourado")
            if nome[0] < "A" or nome[0] > "Z": ind_erro = 1
            digita = "?"
            if ind_erro == 1:
                while digita != "s" and digita != "n":
                    digita = input("Nome inválido. Corrigir? (s/n) ")
    
    if ind_erro == 0:
        digita = "s"
        while digita == "s":
            dia = input("\nDigite o dia da admissão: ")
            mes = input("Digite o mês da admissão: ")
            ano = input("Digite o ano da admissão: ")
            ind_erro = 0
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
            digita = "?"
            if ind_erro == 1:
                while digita != "s" and digita != "n":
                    digita = input("Data inválida. Corrigir? (s/n) ")

    if ind_erro == 0:
        digita = "s"
        while digita == "s":
            ind_erro = 0
            try:
                salario = float(input("\nDigite o salário: "))
            except ValueError:
                ind_erro = 1
            if salario <= 0: ind_erro = 1
            digita = "?"
            if ind_erro == 1:
                while digita != "s" and digita != "n":
                    digita = input("Código inválido. Corrigir? (s/n) ")
    if ind_erro == 0:
        print ("Cadastro realizado com sucesso")
        registro = struct.pack("i30siiif", codigo, nome.encode("ascii"), dia, mes, ano, salario)
        arquivo.write(registro)
arquivo.close()
