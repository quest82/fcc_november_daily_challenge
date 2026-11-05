def verify(message, key, signature):
    from string import ascii_letters as alphabets
    
    encode = {}
    count = 1
    for letter in alphabets:
        encode[letter] = count
        count += 1


    complete_key = message + key
    only_alphabets = filter(lambda n:n.isalpha(), complete_key)

    total = 0
    for val in only_alphabets:
        total += encode[val]
    print(total)

    
verify("Check out the freeCodeCamp podcast,", "in the mobile app", 514)
    # return message