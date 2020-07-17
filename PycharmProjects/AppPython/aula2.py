
a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
# print(type(soma))
# soma = str(soma)
# print(type(soma))
print('soma: {soma}. \nsubtração: {subtracao}'
      '\nmultiplicação: {multiplicacao}'
      '\nDivisão: {divisao}'
      '\nResto: {resto}'.format(soma=soma,
                                subtracao=subtracao,
                                multiplicacao=multiplicacao,
                                divisao=divisao,
                                resto=resto))


# x = '1'
# soma2 = int(x) + 1
# print(soma2)
