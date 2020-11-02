arr = ["lion", "tiger", "buffalo", "goat", "elephant"]


#    +
#   + +
#   + +
#  ++ +
# +++++
# +++++
# +++++
# +++++


def print_histogram(string_array):
    # string_array_len = len(string_array)
    # max_len = 0
    len_stings = []

    for string in string_array:
        len_stings.append(len(string))

    max_len = max(len_stings)

    while max_len != 0:
        for i in len_stings:
            if i >= max_len:
                print("+", end="")
            else:
                print(" ", end="")
        print()
        max_len -= 1


print_histogram(arr)
