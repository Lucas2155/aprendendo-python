"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a # valor da lista a será atribuido na lista b, o que for modificado nela também afetara a lista_b
lista_b = lista_a.copy() # copia a lista_a mas o que for modificada nela não afetara a lista_b

lista_a[0] = 'Qualquer coisa'

print(lista_a)
print(lista_b)