################################################################################################
#Disciplina - Python ministrado pela USP - Universidade da Cidade de São Paulo
#Exercicio extra realizado em 12/06/2021 às 01:28
#Programação em python
################################################################################################
#Problema
''' Reescreva o programa contaSegundos para imprimir também a quantidade de dias, ou seja,
 faça um programa em Python que, dada a quantidade de segundos, "quebre" esse valor em dias, 
 horas, minutos e segundos. A saída deve estar no formato: a dias, b horas, c minutos e d segundos.
'''
segundos = int(input("Digite a quantidade de segundos que deseja converter: "))
calc_dias = segundos//86400
rest_segundos = segundos % 86400
calc_horas = rest_segundos // 3600
rest_segundos = rest_segundos % 3600
calc_min = rest_segundos //60
rest_segundos = rest_segundos % 60
print(calc_dias,"dias,",calc_horas,"horas,",calc_min,"minutos e",rest_segundos, "segundos" )              

