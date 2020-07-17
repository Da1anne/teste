from aula8_contador_letras import contador_letras

if __name__ == '__main__':
    lista = ['elefante', 'cão', 'rato']
    total_letras = contador_letras(lista)
    print('total de letras por palavra {}'.format(total_letras))