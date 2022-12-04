"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista = [10, 20, 30, 40]
lista.insert(0, 5) # lista.insert(índice que você quer inserir o novo dado, valor que você quer atribuir a este índice)
lista.insert(10000, 'Lucas') # Se você colocar um índice que não tem na sua lista ele irá adicionar no final
print(lista)