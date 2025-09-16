from random import randint


numero = randint(1,10)

print('| ------------------ SHOW DO LK💸 -------------------- |' )



print('Vou pensar em um número, tente adivinhar!')
numero1 = int(input('Digite um número de 1️⃣  a 🔟: '))

while numero1 != numero:
    print('Você errou!')
    if numero1 < numero:
        print('Número maior ☝️ ')
    else:
        print('Número menor 👇')
    numero1 =  int(input('Digite outro número: '))


print('Você acertou!!!👌😁')

