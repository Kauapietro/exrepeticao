total_avaliacoes = int(input("Digite o total de avaliações: "))
notas = []

for i in range(total_avaliacoes):
    nota = float(input("Digite a nota da avaliação {}: ".format(i+1)))
    notas.append(nota)

media = sum(notas) / total_avaliacoes
print("A média aritmética das notas é:", media)
