#!/usr/bin/python3
#-*- coding: UTF-8 -*-

l1 = int(input("lado 1: "))
l2 = int(input("lado 2: "))
l3 = int(input("lado 3: "))
if l1 < (l2 + l3) and l2 < (l1 + l3) and le < (l1 + l2):
    print("lados de um triângulo: ", end = "")
    if l1 == l2 and l2 == l3:
        print("equilátero")
    else:
        if l1 == l2 or l1 == l3 or l2 == l3:
            print("isósceles")
        else: print("escaleno")
else: print("não formam um triângulo")