#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# prog2.py

inss = irrf = salario_liquido = 0.0

import struct
tamanho = len(struct.pack("i30siiif", 0, " ".encode("ascii"), 0, 0, 0, 0.0))
arquivo = open("arq_func.dat", "rb")

while True:
    registro = arquivo.read(tamanho)
    if registro == b"": break
    (codigo, nome, dia, mes, ano, salario) = struct.unpack("i30siiif", registro)
    inss = salario * 0.11
    if inss > 615: inss = 615.00
    irrf = (salario - inss) * 0.245
    salario_liquido = salario - inss - irrf
    print("\nCódigo:          %03d" % codigo)
    print("Nome:            %-30s" % str(nome,"ascii").strip("\x00"))
    print("Data adm.        %02d/%02d/%04d" % (dia, mes, ano))
    print("Salário:         %08.2f" % salario)
    print("Vlr. do INSS:    %08.2f" % inss)
    print("Vlr. do IRRF:    %08.2f" % irrf)
    print("Sal. Líquido:    %08.2f" % salario_liquido)
    a = input("Pressione ENTER para ver o próximo registro. ")
arquivo.close()
