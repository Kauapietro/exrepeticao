contador_intervalo = 0

for _ in range(5):
    numero = float(input("Digite um número: "))
    if 10 <= numero <= 150:
        contador_intervalo += 1

print("Quantidade de números no intervalo [10, 150]:", contador_intervalo)

