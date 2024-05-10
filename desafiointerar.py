# frutas = ['maça','laranja','morango','limão']
# for indice,fruta in enumerate(frutas,1):
#     print(indice,fruta)
#     if indice == 3:
#      print('a fruta 3 esta em promoção ')

#CORRIGIDO 
frutas = ['maça','laranja','morango','limão']
for indice,fruta in enumerate(frutas,0):
    if indice == 3:
     print(f'{indice} {fruta} EM promoção  ')
    else:
        print(indice,fruta)

