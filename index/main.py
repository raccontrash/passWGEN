import os
from func_espc import versionamento
from func_espc import criarLista
from ASCIIIMAGE import ANGRYBOYSINC
import random
import string
from func_espc import passwd_gen
from func_espc import criando_arq
# ORGANIZAR ESSES ITENS DEPOIS


ANGRYBOYSINC()
versionamento()

print("1. Iniciar.")
print("2. Sair")


i = input("Escolha a opção: ")
if i == "1":
    # print("console.log("")")
    passwd_gen()
    criando_arq()
else:
    print("fechando programa")
    quit()


# C:\Users\bruno\Desktop\brunobruno\prgm\OUTROS\passWGen\index\senhas.txt