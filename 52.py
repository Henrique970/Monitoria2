# O c é um valor defalt
# nomeado/ posicional
def asdf(a, b, c = 0):
    print(a, b, c)
asdf(1,2)

# Multiplos argumentos posicional o args
def asdf(*args):
    print(args)
asdf(1,2,3,4,5,6,7,8,9,0)


# Multiplos argumentos noeados o kwargs
def asdf(**kwargs):
    print(kwargs)
asdf(a = 1,b = 2,c = 3,d = 4,e = 5,f = 6,g = 7,h = 8,i = 9,j = 0)

# Todos juntos
def asdf(*args, **kwargs):
    print(args, kwargs)
asdf(1,2,3,d=4, e=5, f=6)
