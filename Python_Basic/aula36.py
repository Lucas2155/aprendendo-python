contador = 0

while contador < 40:
    contador += 1
    
    if contador == 6:
        print('Não vou mostar o 6')
        continue

    if contador >= 10 and contador <= 27:
        continue

    print(contador)

    if contador == 38:
        break

print ('Acabou')