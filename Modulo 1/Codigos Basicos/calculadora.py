print('|----------------------|')
print('|Calculadora')
print('|----------------------|')
print('|1-Soma')
print('|2-Subtração')
print('|3-Multiplicação')
print('|4-Divisão')
print('|----------------------|')
opcao =float(input('|Escolha uma opção: '))
numero1 =float(input('|Digite o primeiro número: '))
numero2 =float(input('|Digite o segundo número: '))
if opcao == 1:
    print(f'|O resultado de {numero1} + {numero2} é {numero1+numero2}.')
elif opcao == 2:
    print(f'|O resultado de {numero1} - {numero2} é {numero1-numero2}.')
elif opcao == 3:
    print(f'|O resultado de {numero1} x {numero2} é {numero1*numero2}.')
elif opcao == 4:
    print(f'|O resultado de {numero1} / {numero2} é {numero1/numero2}.')
else:
    print('|Erro, escolha um número válido.')