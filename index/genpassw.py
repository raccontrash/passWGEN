import random
import string

def gen_pass():
    opcoes = string.ascii_letters + string.digits # monta alfabeto inteiro?
# equivalente > abcdefg(alfabeto inteiro)
    resultado = "" # resultado em branco
    for i in range(8): # definindo o numero max d character (8)
        resultado += random.choice(opcoes)

    print(resultado)