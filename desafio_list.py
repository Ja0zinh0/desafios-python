from itertools import zip_longest
produtos = ['produto 1', 'produto 2', 'produto 3','produto 4','produto 5']
precos = [500,1500,2700,5800]
for produto,preco in zip_longest(produtos,precos):
     print(f'{produto} encontrado no valor de {preco}')

