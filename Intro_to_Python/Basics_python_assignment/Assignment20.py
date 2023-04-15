'''20.Write a Python function words_count(sentence) to return a dictionary with the length of words as key and number words with such length as value.'''

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if len(word) in counts:
            counts[len(word)] += 1
        else:
            counts[len(word)] = 1

    return counts

print(word_count('the quick brown fox jumps over the lazy dog.'))