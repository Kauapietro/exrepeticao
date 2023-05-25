# Variáveis para armazenar o total de carros até 2000 e o total geral
total_ate_2000 = 0
total_geral = 0

# Laço para calcular o desconto e o valor a ser pago para cada carro
continuar = True
while continuar:
    ano = int(input("Digite o ano do veículo: "))
    valor = float(input("Digite o valor do veículo: "))

    if ano <= 2000:
        desconto = 0.12
        total_ate_2000 += 1
    else:
        desconto = 0.07

    valor_desconto = valor * desconto
    valor_pago = valor - valor_desconto

    print(f"Desconto: R$ {valor_desconto:.2f}")
    print(f"Valor a ser pago: R$ {valor_pago:.2f}")

    total_geral += 1

    resposta = input("Deseja continuar calculando descontos? (S/N) ")
    if resposta.upper() == "N":
        continuar = False

# Exibindo o total de carros até 2000 e o total geral
print(f"Total de carros até 2000: {total_ate_2000}")
print(f"Total geral: {total_geral}")
