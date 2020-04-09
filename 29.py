heroes =  [('Super Man', 'Imortal'),('Iron Man', 'Mortal'), ('Spider Man', 'Mortal'), ('Batman', 'Mortal')]

def ordem_crescente(a):
    a.sort()
    return a

def ordem_decrescente(b):
    b.sort(reverse=True)
    return b

print(ordem_crescente(heroes))
print(ordem_decrescente(heroes))
