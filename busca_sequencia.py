#!/usr/bin/python3
#-*- coding: UTF-8 -*-

cont = ix = 0
texto = input("Digite sequência de caracteres: ")
while ix < len(texto) - 2:
    txt = texto[ix] + texto[ix + 1] + texto[ix + 2]
    if txt == "alo":
        cont = cont + 1
    ix = ix + 1
print("a sequência 'alo' aparece ", cont, "vezes")