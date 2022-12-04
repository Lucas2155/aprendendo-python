"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""
lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        valor = input('Valor: ')
        lista.append(valor)
        print(valor)
        continue
    elif opcao == 'a':
        apagar = input('Escolha o índice que deseja apagar: ')
        apagar_int = int(apagar)
        if apagar_int <= len(lista):
            del lista[apagar_int]
        else:
            print('Desculpe, este índice não existe na sua lista.')
    elif opcao == 'l':
        for lista_comprar in enumerate(lista):
            print(lista_comprar)
    else:
        print('Por favor, digite um valor válido!')
