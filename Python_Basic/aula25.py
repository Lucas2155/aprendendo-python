"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel:$^10}.')
print(f'{1000.3124657267:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}') # 08X = Tem que ter 8 casas, caso necessite completará com 0. O X maisculo indica que o Hexadecimal será mostrado maiúsculo.
