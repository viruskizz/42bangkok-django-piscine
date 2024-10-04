def my_var():
    num = 42
    s = '42'
    deux = 'quarante-deux'
    digit = 42.0
    iss = True
    li = [42]
    ob = {42: 42}
    tu = (42,)
    se = set()
    print("42 has a type", type(num))
    print(f'{s} has a type {type(s)}')
    print(f'{deux} has a type {type(deux)}')
    print(f'{digit} has a type {type(digit)}')
    print(f'{iss} has a type {type(iss)}')
    print(f'{li} has a type {type(li)}')
    print(f'{ob} has a type {type(ob)}')
    print(f'{tu} has a type {type(tu)}')
    print(f'{se} has a type {type(se)}')

if __name__ == '__main__':
    my_var()