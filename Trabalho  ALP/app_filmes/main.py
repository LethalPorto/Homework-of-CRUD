#Chamando o as funções
import app_filmes

#criação do dicionario para executar as funções
dic_filmes = {}

#Print de seja bem_vindo
print("Seja Bem_Vindo")

#While True que vai chamar as funções e verificar se o usuário  quer fazer as operações
while True:
    #Aqui nesse if estou verificando se há alguma chave existente no dicionario
    if not dic_filmes:
        print("O registro esta vazio recomendamos adicionar algo, pois as operações LEITURA, ATUALIZAR e DELETAR não vão funcionar.")

    #resposta concernente ao o que o usuário quer fazer
    resposta = int(input("(1)ADICIONAR, (2)LEITURA, (3)ATUALIZAR, (4)DELETAR, (5)SAIR: "))


    if resposta == 1:

        print("Abrindo...")
        app_filmes.create(dic_filmes)

    if resposta == 3:

        print("Abrindo...")
        app_filmes.update(dic_filmes)

    if resposta == 5:
        break