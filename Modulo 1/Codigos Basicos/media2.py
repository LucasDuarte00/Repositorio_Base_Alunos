from colorama import init, Fore
init(autoreset=True)
print('|------------------------|')
print('SISTEMA DE PROVAS')
print('|------------------------|')
nome =(input(f'Nome do aluno: '))
nota1 =float(input(f'Nota da primeira prova: '))
nota2 = float(input(f'Nota da segunda prova: '))
nota3 = float(input(f'Nota da terceira prova:'))
print('|------------------------|')
media = (nota1 + nota2 + nota3)/3
if media >=5:
    print(Fore.GREEN+f'Aluno foi aprovado!')
else:
    print(Fore.RED+f'Aluno foi reprovado.')