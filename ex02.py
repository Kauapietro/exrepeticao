while True:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if senha != usuario:
        break
    else:
        print("Erro: A senha não pode ser igual ao nome de usuário. Tente novamente.")

print("Cadastro realizado com sucesso!")
