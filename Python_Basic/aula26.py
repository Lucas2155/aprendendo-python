"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::] - i = inicio, f = fim , p = passo (de quanto em quatos caracteres ele irá pular)
Se o final for omitido ele irá fatiar até o fim da string
Obs.: a função len retorna a qtd 
de caracteres da str
Índice começa do 0
Já a contagem na função len começa no 1
"""
variavel = 'Olá mundo'
print(variavel[4:])
print(variavel[0:5])
print(variavel[:5])
print(variavel[-8:-2])
print(len(variavel[4]))
print(variavel[0:len(variavel):1])
print(variavel[0:len(variavel):2])