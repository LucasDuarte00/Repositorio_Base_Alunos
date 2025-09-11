modelo = input('Qual o modelo do carro? ')
dias = int(input('Por quantos dias o carro foi alugado? '))
km =float(input('Quantos km o carro rodou? '))

if modelo == 'uno':
    diaria = 120
elif modelo == 'bmw':
    diaria = 690
elif modelo == 'duster':
    diaria = 330
else:
    diaria = 60

total_dias = dias * diaria
total_km = km*0.20
valor_total = total_dias + total_km
print(f'Você andou {km}km por {dias} dias, então o preço a pagar é R${valor_total}.')