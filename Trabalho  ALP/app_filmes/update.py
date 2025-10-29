# Mosias
def update(dicionario):

    while True:

        print("------------------------",f"\n{dicionario}")
        resposta = input("O que você quer atualizar?: ")

        if resposta in dicionario:
            item_para_ser_atualizado = int(input("Você quer mudar (1)Titulo, (2)Genêro, (3)Ano, (4)Plataforma, (5)Sair: "))
            print("Carregando sua resposta...")

            if item_para_ser_atualizado == 1:
                novo_titulo = input("Coloque o novo titulo: ")

                if novo_titulo != "":
                    G_A_P = dicionario[f"{resposta}"]
                    del dicionario[f"{resposta}"]
                    dicionario[f"{novo_titulo}"] = G_A_P
                    print(dicionario)

            elif item_para_ser_atualizado == 2:
                print("Carregando genêro...")
                genero_antigo = input("Coloque o antigo genero: ")
                novo_genero = input("Coloque o novo genêro: ")

                if novo_genero != "":
                    for i in dicionario[resposta]:
                        print(i)
                        if i == genero_antigo:
                            dicionario[f"{resposta}"].remove(i)
                            dicionario[f"{resposta}"].insert(0, novo_genero)
                            print(dicionario)
                        else:
                            print("O seu genero não foi encontrado, repita novamente.")
                            continue
                else:
                    print("O novo genero não pode estar vazio, repita novamente.")
                    continue

            elif item_para_ser_atualizado == 3:
                print("Carregando ano...")
                novo_ano = int(input("Coloque o novo ano: "))

                if novo_ano >= 1888 and novo_ano <= 2030:
                    contA = 0
                    for i in dicionario[resposta]:
                        if contA == 1:
                            dicionario[f"{resposta}"].remove(i)
                            dicionario[f"{resposta}"].insert(1, novo_ano)
                            print(dicionario)
                        contA += 1
                else:
                    print("O novo ano tem que ser adequado a linha do tempo, repita novamente.")
                    continue

            elif item_para_ser_atualizado == 4:
                print("Carregando plataforma...")
                nova_plataforma = input("Coloque o nova plataforma: ")

                if nova_plataforma != "":
                    contP = 0
                    for i in dicionario[resposta]:
                        if contP == 2:
                            dicionario[f"{resposta}"].remove(i)
                            dicionario[f"{resposta}"].insert(2, nova_plataforma)
                            print(dicionario)
                        contP += 1
                else:
                    print("A plataforma não foi reconhecida, repita novamente.")
                    continue

            elif item_para_ser_atualizado == 5:
                print("Finalizando...")
                break
            else:
                print("ERRO NA RESPOSTA REPITA")
                continue