import random  # importa o módulo random, que contém funções para gerar números aleatórios
import random

print(random.random())


print(random.randint(1,10))
print(random.uniform(4,10))

cores = ['preto','rosa','azul']
print(random.choice(cores))

print(random.random)  # imprime um número float aleatório entre 0 e

print(random.uniform(4, 10))  # imprime um número float aleatório entre 4 e 10

print(random.randint(1, 10))  # imprime um número inteiro aleatório entre 1 e 10 (inclusive)


cores = ['preto', 'rosa', 'azul']  # cria uma lista de strings
print(random.choice(cores))  # imprime um elemento aleatório da lista

import random  # importa novamente o módulo random

# imprime um número float aleatório entre 0 e 1
print(random.random())

# imprime um número float aleatório entre 4 e 10
print(random.uniform(4, 10))

# imprime um número inteiro aleatório entre 1 e 10 (inclusive)
print(random.randint(1, 10))

cores = ['preto', 'rosa', 'azul']  # cria novamente uma lista de strings

# imprime um elemento aleatório da lista
print(random.choice(cores))