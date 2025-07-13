#Count Vowels in Each Word

#Write a function that takes a sentence as input and returns a dictionary where each key is a word from the sentence, and its value is the number of vowels in that word.

def count_vowels(sentence):
    words = sentence.split()
    d = {}
    for word in words:
        count = 0
        for char in word:
            if char in 'aeiouAEIOU':
               count += 1
        d[word] = count
    return d

print(count_vowels('Amazon is hiring quality engineers'))
