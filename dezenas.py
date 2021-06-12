################################################################################################
#Disciplina - Python ministrado pela USP - Universidade da Cidade de São Paulo
#Exercicio extra realizado em 12/06/2021 às 02:25
#Programação em python
################################################################################################
''' Dica:: O operador "//" faz uma divisão inteira jogando fora o resto, ou seja, 
# aquilo que é menor que o divisor. O operador "%" devolve apenas o resto da divisão inteira 
# jogando fora o resultado, ou seja, tudo que é maior ou igual ao divisor.'''
################################################################################################
#Problema
''' Faça um programa em Python que recebe um número inteiro 
e imprime seu dígito das dezenas. Observe o exemplo abaixo:
'''
valor = int(input("Digite um número para encontrar a sua dezena: "))
dezena = (valor//10) % 10
print('O dígito das dezenas é', dezena )              

