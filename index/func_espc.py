def versionamento():
    build_version = "1.4.4"
    print("build", build_version)

def criarLista():
    entradaUser = []
    lista_montada = []
    while True:
        # confirmação do usuario deve ser > Enter <, não FIM (TRABALHANDO NISSO AINDA)
        entradaUser = input("Digite as palavras para adicionar na lista. (ou 'cancelar' para sair): ")
        if entradaUser == 'cancelar':
            break # fecha loop

        lista_montada.append(entradaUser) # adiciona a palavra a lista

    print("GERANDO SENHAS COM BASE NAS SEGUINTES PALAVRAS: \n")
    print(entradaUser)