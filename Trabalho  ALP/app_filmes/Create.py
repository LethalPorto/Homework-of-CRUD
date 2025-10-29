# Mosias
# Criação da função
def create(dicionario):
    # Loop de repetição
    while True:
        # Pedindo ao o usuário nome do titulo, o gênero, o ano de lançamento e a plataforma do filme
        Titulo = input("Insira o titulo: ")
        print("Adiconando o  titulo...")

        Genero = input("Insira o genero: ")
        print("Adiconando o  genero...")

        Ano = int(input("Insira o ano de lançamento: "))
        print("Adiconando o  ano...")

        Plataforma = input("Insira o Plataforma: ")
        print("Adiconando o  plataforma...")

        # Adicionando o Titulo como chave do dicionario, e dentro dele uma lista que vai conter Genero ano e plataforma
        dicionario[f"{Titulo}"] = [Genero, Ano, Plataforma]

        # Verificando se o titulo foi realmente adicionado ao dicionario
        if Titulo in dicionario:
            print("Confira se o seu filme foi adicionado:",f"\n{dicionario}")
            resposta = input("Deseja continuar? [s/n]").lower()

            if resposta == "s":
                continue
            if resposta == "n":
                break

        else:
            print("Houve um erro tente novamente.")
            continue