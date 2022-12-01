a = 'A'
b = 'B'
c = 1.1 # ao colocar :.2f ele irá pegar duas casas decimais
string = 'a={nome1} b={nome2} c={nome3:.2f}' # substitui os valores de acordo com a ordem dos argumentos dentro de format
formato = string.format(
    nome1=a, nome2=b, nome3=c
    )

print(formato)
