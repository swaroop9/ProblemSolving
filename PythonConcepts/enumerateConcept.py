grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))

# converting to list
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))

for item in enumerate(grocery):
    print(item)  # get tuple

for count, item in enumerate(grocery):
    print(count, item)  # destructuring

print('\n')
# changing default start value
for count, item in enumerate(grocery, 100):
  print(count, item)