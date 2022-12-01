# Operadores in (entre) e not in (não está entre)
# Strings são iteráveis (pode navegar item por item)
# 0 1 2 3 4 5
# O t á v i o
# -6-5-4-3-2-1

nome = 'Otávio'
print(nome[2])
print(nome[-4])

print('á' in nome) # á está entre as letras do nome? True
print('z' in nome)
print('vio' in nome)
print('zero' in nome)
print(10 * '-')

print('vio' not in nome) # vio não está entre as letras do nome? False
print('zero' not in nome)

nome2 = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')