possui_passaporte = False

passagem_comprada = False

menor_de_idade = False
if passagem_comprada == False: 
    print ("Você não comprou a passagem!")
    
# Uma pessoa só pode viajar se possuir  passaporte e tiver a passagem comprada e não for menor de idade
print(possui_passaporte == True and passagem_comprada == True and not menor_de_idade == True ) #CERTO
# Uma pessoa só pode viajar se possuir passaporte ou tiver a passagem comprada e não for menor de idade
print(possui_passaporte == True or  passagem_comprada == True and not menor_de_idade == True) #CERTO
# Uma pessoa só pode viajar se não possuir passaporte ou tiver a passagem comprada e não for menor de idade
print(not possui_passaporte or  passagem_comprada == True and not menor_de_idade == True) #CERTO
# Uma pessoa não pode viajar se não possuir passaporte ou não tiver a passagem comprada e for menor de idade
print( not possui_passaporte  or not passagem_comprada == False and menor_de_idade == True) #CERTO 
