import lista as lista

num = int(input('Digite um número: '))
fibo = int(input('Quantos elementos deseja na sequência de Fibonacci: '))
cont = 0
i = 0
j = 1
lista_i = []

while cont < fibo:
    cont = cont + 1
    lista_i.append(i)
    i = i + j
    j = i - j


print(lista_i)
if num in lista_i:
     print('O número {}'.format(num),'está na lista')
else:
     print('O número {}'.format(num),'não está na lista')
