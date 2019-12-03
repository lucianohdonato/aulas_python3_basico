#!/usr/bin/python3
#-*- coding: UTF-8 -*-

x1 = x2 = aux = 0
L = [0] * 10

for x1 in range(0, 10):
    L[x1] = int(input("Digite elemento: "))

for x1 in range(0, 9):
    for x2 in range(x1 + 1, 10):
        if L[x1] > L[x2]:
            aux = L[x1]
            L[x1] = L[x2]
            L[x2] = aux

for x1 in range(0, 10):
    print(L[x1])
