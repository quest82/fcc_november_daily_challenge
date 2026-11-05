def verify(message, key, signature):
    from string import ascii_letters as alphabets
    
    encode = {}
    count = 1
    for letter in alphabets:
        encode[letter] = count
        count += 1

    print(encode)

    

verify(1,2,3)
    # return message