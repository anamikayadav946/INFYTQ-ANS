'''21.Write a Python function vowel_count(sentence) to return a dictionary with vowels, consonants, others as key and respective number of vowels, consonants, others characters as value.
Note: Do case insensitive operations'''

def vowel_count(sentence):
    counts = dict({'vowel':0,'consonant':0,'others':0})
    for i in sentence:
        if i.lower() in 'aeiou':
            counts['vowel'] += 1
        elif i.lower() in 'bcdfghjklmnpqrstvwxyz':
            counts['consonant'] += 1
        else:
            counts['others'] += 1   
    return counts         

print(vowel_count('I love python and it so easy to learn'))