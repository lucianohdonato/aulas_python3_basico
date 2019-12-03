#!/usr/bin/python3
#-*- coding: UTF-8 -*-

num = int(input("Digite num para calcular fatorial: "))
fat = 1
for x in range(1, num + 1):
    fat = fat * x
print("O fatorial de %2d é = %d" %(num, fat))