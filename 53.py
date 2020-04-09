def media(*args):
    return sum(args) / len(args)

assert media(2,4) == 3
assert media(4,4,4) == 4
assert media(10,4,1) == 5
assert media(2,4,6) == 4
