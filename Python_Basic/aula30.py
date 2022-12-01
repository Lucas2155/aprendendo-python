"""
Flag (Bandeira) - Marcar um local
None = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
"""
# Ambas variáveis terão o mesmo ID na memória
v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2))

condicao = False # Se eu colocar True ele irá mudar o valor de passou_no_if para True e executa o if
passou_no_if = None # Criando uma variavél vazia

if condicao:
    passou_no_if = True # Se for True irá mudar o passou_no_if para True
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)