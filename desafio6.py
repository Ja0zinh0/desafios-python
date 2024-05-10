# ​Desafio 1: Transforme a frase1 em uma lista de palavras e guarde o resultado em uma variável chamada palavras1

# Desafio 2: Transforme a frase2 em uma lista de palavras e guarde o resultado em uma variável chamada palavras2

# Desafio 3: Pegue o palavras1 e transforme elas no seguinte string: "Desafio,manipulação,de,strings". Imprima o resultado no console.

# Desafio 4: Pegue o palavras2 e transforme elas no seguinte string: frase2 = "jhonatan & rafael & carol & camilla". Imprima o resultado no console.

frase1 = 'Desafio manipulação de strings'
# print(frase1.split(' '))
frase2 = 'jhonatan,rafael,carol,camilla'
# print(frase2.split(','))

palavras1 = frase1.split(' ') 
print((',').join(palavras1))
                                  
palavras2 = frase2.split(',')
print(( ' & ' ).join(palavras2))

