while True:
    # Leitura dos dados do aluno
    numero_identificacao = int(input("Digite o número de identificação do aluno: "))
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    nota3 = float(input("Digite a terceira nota do aluno: "))
    media_exercicios = float(input("Digite a média dos exercícios do aluno: "))

    # Cálculo da média de aproveitamento
    ma = (nota1 + nota2 * 2 + nota3 * 3 + media_exercicios) / 7

    # Determinação do conceito
    if ma >= 9.0:
        conceito = "A"
    elif 7.5 <= ma < 9.0:
        conceito = "B"
    elif 6.0 <= ma < 7.5:
        conceito = "C"
    elif 4.0 <= ma < 6.0:
        conceito = "D"
    else:
        conceito = "E"

    # Exibição dos resultados
    print("\nNúmero de identificação:", numero_identificacao)
    print("Notas: {}, {}, {}".format(nota1, nota2, nota3))
    print("Média dos exercícios:", media_exercicios)
    print("Média de aproveitamento:", ma)
    print("Conceito:", conceito)

    # Verificação de aprovação/reprovação
    if conceito in ["A", "B", "C"]:
        print("APROVADO")
    else:
        print("REPROVADO")

    # Verificar se o usuário deseja digitar as notas de outro aluno
    resposta = input("\nDeseja digitar as notas de outro aluno? (S/N): ")
    if resposta.lower() != "s":
        break
