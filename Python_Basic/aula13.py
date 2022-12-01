nome = 'Lucas Linhares'
altura = 1.82
peso = 71
imc = peso / altura ** 2

# f-string -> formatação -> envolve a variável através de {}
linha_1 = f'{nome} tem {str(altura)} de altura,'
linha_2 = f'pesa {str(peso)} quilos e seu IMC é'
linha_3 = f'{imc}'

print(linha_1)
print(linha_2)
print(linha_3)

# Output deverá ser:
# Lucas Linhares tem 1.82 de altura,
# pesa 71 quilos e seu IMC é
# 29.4324653146745645
