"""
Introdução ao desempacotamento
"""
# nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
nome1, *resto = ['Maria', 'Helena', 'Luiz'] # Colocar o * para ele gravar os outros valores dentro da variavel que você definiu
print(nome1, resto)
