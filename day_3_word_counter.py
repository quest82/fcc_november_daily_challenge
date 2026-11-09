import string

def count_words(sentence):
    words = [word.strip(string.punctuation) for word in sentence.split(" ")]
    return len(list(words))


print(count_words("The missing semi-colon crashed the entire internet."))