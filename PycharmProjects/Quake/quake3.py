import json


# def ler_arquivo(nome_arquivo):
#     arquivo = open(nome_arquivo, 'r')
#     lista = arquivo.read()
#     print(lista)
#     print(lista.find('0:00'))
#     lista_nova = lista.split('0:00')
#     # for x in lista:
#     #     lista_nova.append(x)
#     print(lista_nova)

    # lista = lista.split('InitGame:')

    # print(lista)
    # for x in lista:
    #     if x != str(''):
    #         x = int(x)
    #         lista_nova.append(x)
    #
    # soma = 0
    # cont = 0
    # lista_maior_que_zero = []
    # for x in lista_nova:
    #     if x != 0:
    #         lista_maior_que_zero.append(x)
    #         soma = soma + float(x)
    #         cont = cont + 1
    #         media = soma / cont
    # dias = 0
    # for x in lista_maior_que_zero:
    #     if float(x) > media:
    #         dias = dias + 1
    #


# def retorna_dados(nome_arquivo):
#     response = requests('Quake.txt')
    # print(response.status_code)
    # print(response.json())
    # print(type(response.json()))
    # dados = response.json()
    # print(dados['InitGame'])
    # print(dados['complemento'])
    # return dados

if __name__ == '__main__':
    print('O arquivo escolhido foi Quake.txt\n')
    filename = 'Quake.txt'
    dict1 = {}
    with open(filename) as fh:

        for line in fh:
            # reads each line and trims of extra the spaces
            # and gives only the valid words
            command, description = line.strip().split(None, 1)

            dict1[command] = description.strip()

            # creating json file
    # the JSON file is named as test1
    out_file = open("quake1.json", "w")
    json.dump(dict1, out_file, indent=4, sort_keys=False)
    out_file.close()

    # retorna_dados('Quake.txt')
    print('Fim do programa!')