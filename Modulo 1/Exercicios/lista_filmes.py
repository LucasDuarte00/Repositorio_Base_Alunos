print('Digite o nome de 3 filmes para adicionar a lista: ')
contador = 1

nome = []

while contador <=3:
    filme = input(f'Digite o nome do {contador}° filme: ')
    nome.append(filme)
    contador = contador+1

print(nome)

