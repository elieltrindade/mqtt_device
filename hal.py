#  Hardware Abstraction Layer, objetivo é criar uma camada de acesso ao Hardware separada do sistema
import random

def temperatura():
    return random.randrange(2, 32)

def umidade():
    return random.randrange(10, 95)

def aquecedor(estado: str):
    if estado == 'on':       #comando que liga
        print('AQUECERDOR LIGADO')
    else:
        print('AQUECEDOR DESLIGADO')