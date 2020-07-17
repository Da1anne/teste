
lista = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

tupla = (1, 10, 12, 14)
print(tupla[3])
print(len(lista_animal))

tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)

# lista_animal[0] = 'macaco'
# print(lista_animal)

#print(lista_animal[1])
# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# lista_animal.reverse()
# print(lista_animal)


# novo_lista = lista_animal * 3
# print(novo_lista)

# if 'lobo' in lista_animal:
#     print('existe um lobo na lista')
# else:
#     print('não existe um lobo na lista')
#     lista_animal.append('lobo')
#     print(lista_animal)

# lista_animal.remove('gato')
# print(lista_animal)
#
# lista_animal.pop(2)
# print(lista_animal)

#print(max(lista_animal))

# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)