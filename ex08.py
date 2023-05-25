# Função para verificar se uma pessoa é maior de idade
def verificar_maioridade(idade):
    if idade >= 18:
        return "maior de idade"
    else:
        return "menor de idade"

# Laço para receber as idades e exibir a mensagem para cada pessoa
for i in range(1, 76):
    idade = int(input(f"Digite a idade da pessoa {i}: "))
    resultado = verificar_maioridade(idade)
    print(f"A pessoa {i} é {resultado}.")
