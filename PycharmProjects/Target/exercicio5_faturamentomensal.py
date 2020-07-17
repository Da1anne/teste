
a = 67836.43
print('O valor do faturamento do estado de SP foi de: {}'.format(a),'reais.')
b = 36678.66
print('O valor do faturamento do estado de RJ foi de: {}'.format(b),'reais.')
c = 29229.88
print('O valor do faturamento do estado de MG foi de: {}'.format(c),'reais.')
d = 27165.48
print('O valor do faturamento do estado de ES foi de: {}'.format(d),'reais.')
e = 19849.53
print('O valor do faturamento de outros estados foi de: {}'.format(e),'reais.')
total = a + b + c + d + e
print('O faturamento total dos estados é de: {}'.format(total),'reais.')
fator = 100 / total
calculo_a = a * fator
calculo_b = b * fator
calculo_c = c * fator
calculo_d = d * fator
calculo_e = e * fator

a_final = round(calculo_a)
b_final = round(calculo_b)
c_final = round(calculo_c)
d_final = round(calculo_d)
e_final = round(calculo_e)

print('A representatividade do estado de SP é de {}'.format(a_final),'%.')
print('A representatividade do estado de RJ é de {}'.format(b_final),'%.')
print('A representatividade do estado de MG é de {}'.format(c_final),'%.')
print('A representatividade do estado de ES é de {}'.format(d_final),'%.')
print('A representatividade do restante dos estados é de {}'.format(e_final),'%.')
