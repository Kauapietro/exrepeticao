# Função para verificar o sinal de um número
def verificar_sinal(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "zero"

# Solicita o valor de N
N = int(input("Digite a quantidade de números que serão inseridos: "))

# Laço para receber os N números e exibir o sinal para cada um
for i in range(N):
    numero = float(input(f"Digite o número {i+1}: "))
    sinal = verificar_sinal(numero)
    print(f"O número {numero} é {sinal}.")
