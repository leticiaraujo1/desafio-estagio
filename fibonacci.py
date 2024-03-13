# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor
# sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8,
# 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado
# um número, ele calcule a sequência de Fibonacci e retorne uma mensagem 
# avisando se o número informado pertence ou não a sequência.

num = int(input('Digite um número: '))

def fibonacci(n):
    list = [0,1]

    while list[-1] <= n:
        next_num = list[-1] + list[-2]
        list.append(next_num)

    if n in list:
        print(f'O número {n} pertence a sequência fibonacci')
    else:
        print(f'O número {n} não pertence a sequência fibonacci')

fibonacci(num)