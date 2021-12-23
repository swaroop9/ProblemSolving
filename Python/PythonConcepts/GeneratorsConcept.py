def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
for char in rev_str("hello"):
    print(char, end="")

print("\n----------------")


# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Using for loop
for item in my_gen():
    print(item)

print("\n----------------")


# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
list_ = [x ** 2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x ** 2 for x in my_list)

print(list_)
print(generator)
print(next(generator))


