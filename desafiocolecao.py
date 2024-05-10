nomes = ['larissa','rafael','marcus','john']

def pessoa_ap(pessoa):
    if pessoa == 'marcus':
        return True
    else:
        return False
print(list(filter(pessoa_ap, nomes)))
    


vagas = [
    ['vaga 1', 1200],
    ['vaga 2', 2550],
    ['vaga 3', 5000]
    
    
    
]
def salarios(vaga):
  if vaga[1] > 2500:
      return True
  else:
      return False
print(list(filter(salarios , vagas))) 
  
