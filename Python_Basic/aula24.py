"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Lucas'
preco = 1000.95897643
variavel = '%s, o preço total foi R$%.2f' % (nome, preco) # O () só virá caso você utilize mais que uma interpolação, como no caso do exemplo.
print(variavel)
print('O hexadecimal de %d é %X' % (15000, 15000))
