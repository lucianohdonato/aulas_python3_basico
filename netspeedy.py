#!/usr/bin/python3
#-*- coding: UTF-8 -*-

tamanho = float(input("Qual o tamanho do arquivo? (em MiB)"))
velocidade = float(input("Qual a velocidade do Link de internet? (em Mbps)"))
speedy = (tamanho * 8) / velocidade
print('Seu tempo de download estimnado é de' , speedy , 'segundos.')
 
