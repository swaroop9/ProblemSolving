string = 'wwwwaaadexxxxxxywww'


def output_encode(given_string):
    length_of_given_string = len(given_string)

    output = ''
    i = 0
    # dict_chars = {}
    while i < length_of_given_string:
        # print(given_string[i])
        count = 1
        while i < length_of_given_string - 1 and given_string[i] == given_string[i + 1]:
            count += 1
            i += 1
        output += given_string[i] + str(count)
        i += 1
    return output


print(output_encode(string))
