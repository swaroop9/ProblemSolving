l = [1, 2, 3, 4]

l_sqr = [x * x for x in l if x % 2 == 0]

print(*l_sqr)
print(l_sqr)

d = {"fn": "poorna", "ln": "Swaroop", "age": 28}

d_out = {d[x] for x in d if x == "fn"}
print(type(d_out))

# Using Dictionary comprehensions
# for constructing output dictionary

state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']

dict_using_comp = {key: value for (key, value) in zip(state, capital)}

print(type(dict_using_comp))

print("Output Dictionary using dictionary comprehensions:", dict_using_comp)

# Using Set comprehensions
# for constructing output set

input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

set_using_comp = {var for var in input_list if var % 2 == 0}

print("Output Set using set comprehensions:", set_using_comp)

x = lambda y: y ** 2

print(x(5))

z = filter(x, l)

print(list(z))

z = map(x, l)

print(list(z))

# Add two lists using map and lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

# https://book.pythontips.com/en/latest/map_filter.html


from functools import reduce

numbers = [1, 2, 3, 4]

value = reduce(lambda a, b: a * b, numbers)
print(value)
