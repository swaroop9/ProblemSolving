S = "aabcccccaaabbcde"

def encode(string):
    encoded_str =''
    count=1
    for idx in range(1, len(string)):
        if string[idx]==string[idx-1]:
            count+=1
        else:
            encoded_str+=string[idx-1]+str(count)
            count=1
    encoded_str+=string[idx]+str(count)
    
    return encoded_str




print(encode(S))