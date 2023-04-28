import random
import string
import os
def versionamento():
    build_version = "1.4.7"
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

def passwd_gen():
    opcoes = string.ascii_letters + string.digits # monta alfabeto inteiro?
# equivalente > abcdefg(alfabeto inteiro)
    resultado = "" # resultado em branco
    for i in range(8): # definindo o numero max d character (8)
        resultado += random.choice(opcoes)
    return resultado

# gerando senha
senha = passwd_gen()

# criando arquivo e gravando senha nele
def criando_arq():
    with open('senhas.txt', 'a') as arquivo:
        arquivo.write(senha)
    print("senha salva com sucesso!")
