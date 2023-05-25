# Variáveis para armazenar os valores
soma_custo = 0
soma_venda = 0

# Laço para receber os preços de custo e venda dos produtos
for i in range(1, 41):
    custo = float(input(f"Digite o preço de custo do produto {i}: "))
    venda = float(input(f"Digite o preço de venda do produto {i}: "))

    soma_custo += custo
    soma_venda += venda

    if venda > custo:
        resultado = "lucro"
    elif venda < custo:
        resultado = "prejuízo"
    else:
        resultado = "empate"

    print(f"Produto {i}: {resultado}")

# Calculando a média de preço de custo e preço de venda
media_custo = soma_custo / 40
media_venda = soma_venda / 40

# Exibindo a média
print(f"Média de preço de custo: R$ {media_custo:.2f}")
print(f"Média de preço de venda: R$ {media_venda:.2f}")
