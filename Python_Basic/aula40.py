"""
while/else
"""
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    #break
    # se tiver um break dentro do while, o else não será executado

    print(letra)
    i += 1
else:
    print('O else foi executado')
print('Fora do while')