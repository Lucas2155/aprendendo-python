"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#         01234
#        -54321
string = 'ABCDE' # 5 caracteres

# Na lista você pode acessar por item
#         0    1           2           3   4
lista = [123, True, 'Lucas Linhares', 1.2, []]
# print(bool([])) # falsy
# print(lista, type(lista))
print(lista)
print(lista[2])
lista[2] = 'Maria'
print(lista[2])
print(lista)