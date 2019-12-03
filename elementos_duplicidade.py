#!/usr/bin/python3
#-*- coding: UTF-8 -*-

x = y = 0
print("Busca duplicidade em string com n elementos")
s = input("digite string: ")
x = 0
while x < len(s) - 1:
    y = x + 1
    while y < len(s):
        if s[x] == s[y]:
            print(s[x], "existe nas pos. ", x + 1, " e ", y + 1)
        y = y + 1
    x = x + 1
print("Fim")
