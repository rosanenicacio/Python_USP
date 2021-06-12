################################################################################################
#Disciplina - Python ministrado pela USP - Universidade da Cidade de São Paulo
#Exercicio extra realizado em 12/06/2021 às 01:21
#progração em python
#problema:
''' Escreva um programa que receba (entrada de dados através do teclado) o nome do cliente,
dia de vencimento, o mês de vencimento e o valor da fatura  e imprima (saída de dados) 
# a mensagem com os dados recebidos, no mesmo formato da mensagem acima. 
# Note que o programa imprime a saída em duas linhas diferentes. 
# Note também que, como não é preciso realizar cálculos, 
# o valor não precisa ser convertido para número, pode ser tratado como texto.'''

nome = input("Digite o seu nome: ")
dia_vencimento = input("Digite o dia de vencimento da fatura: ")
mes_vencimento = input("Digite o mês de vencimento da fatura: ")
valor_fatura = input("Digite o valor da fatura: ")
print('Olá,',nome)
print('A sua fatura com vencimento em', dia_vencimento,'de', mes_vencimento,'no valor de R$', valor_fatura,'está fechada.')