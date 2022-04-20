def cube(num):
    print(f'calling cube')
    return num**3

num_list = [i for i in range(10)]
print(num_list)

print('walrus operator')
cubes_walrus = [y for x in num_list if (y :=cube(x)) < 20]

print('list comprehension')
cubes_comprehension = [cube(num) for num in num_list if cube(num) < 20]

print(cubes_walrus)
print(cubes_comprehension)