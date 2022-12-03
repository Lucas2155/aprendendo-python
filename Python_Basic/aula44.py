"""
Como o for funciona por de trás dos panos
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue o interador
"""
# texto = iter('Lucas') # texto = 'Lucas'.__iter__()

# print(next(texto)) # print(texto.__next__())
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))

texto = 'Lucas'
iterador = iter(texto)

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break