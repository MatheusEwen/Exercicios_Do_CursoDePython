soma = 0
cont = 0
for c in range(1, 501, 2):
    resul = c % 3
    if resul == 0:
        cont = cont +1
        soma += c
print('A soma de todos os valores é',soma)
print('os valores que foram contados', cont)


