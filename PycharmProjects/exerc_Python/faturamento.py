
def info_faturamento(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    lista = arquivo.read()
    lista_nova = []
    lista = lista.split('\n')
    for x in lista:
        if x != str(''):
            x = int(x)
            lista_nova.append(x)

    soma = 0
    cont = 0
    lista_maior_que_zero = []
    for x in lista_nova:
        if x != 0:
            lista_maior_que_zero.append(x)
            soma = soma + float(x)
            cont = cont + 1
            media = soma / cont
    dias = 0
    for x in lista_maior_que_zero:
        if float(x) > media:
            dias = dias + 1

    arquivo.close()
    print('O maior faturamento em um dia do ano foi de {}'.format(max(lista_nova)), 'reais.')
    print('O menor faturamento em um dia do ano foi de {}'.format(min(lista_maior_que_zero)), 'reais.')
    print('O valor de vendas diárias é de em média {}'.format(media),'reais.')
    print('O número de dias onde o faturamento foi maior que a média foi de {}'.format(dias),'dias.')


if __name__ == '__main__':
    print('Escolha o arquivo a ser analisado.\n')
    print('O arquivo escolhido foi faturamento_2018.txt\n')
    info_faturamento('faturamento_2018.txt')
    print('Fim do programa!')

