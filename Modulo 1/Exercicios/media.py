print("|------------------------|")

print("SISTEMA DE PROVAS")
print("|------------------------|")

nome =(input("Nome do aluno: "))
nota1 =float(input("Nota da primeira prova: "))
nota2 = float(input("Nota da segunda prova: "))
nota3 = float(input("Nota da terceira prova:"))
print("|------------------------|")
media = (nota1 + nota2 + nota3)/3
print(f'Aluno foi aprovado {media >=5}')