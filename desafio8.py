# 1. Você quer simular a opção de jogar uma moeda e resultar em cara ou coroa
#     jogue as opções dentro de uma variável e depois crie um programa que imprimir 'cara' ou 'coroa' na tela

import random

moeda = ['cara','coroa']
print(random.choice(moeda))

sorteado = ['joao','gabi','lucas','pedro','mirela']

print(random.choice(sorteado))

print(random.randint(1,100))