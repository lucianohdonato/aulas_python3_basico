#!/usr/bin/python3
# -*- coding: UTF-8 -*-

largura = int(input('informe a largura da parede: '))
altura = int(input('informe a altura da parede: '))
area = largura * altura
litros = area / 2
custo = litros * 14
print('A parede possui ', area, 'm². Para pinta-la serão necessários ', litros, 'litros de tintas, e o custo total será de R$', custo)


