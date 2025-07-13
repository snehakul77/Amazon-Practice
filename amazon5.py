#Count Words by Length

#Write a function that takes a sentence and returns a dictionary showing how many words have a particular length.

def count_wordlength(sentence):
    words = sentence.split()
    d = {}
    for word in words:
        s = len(word)
        if word not in d:
            d[word] = s
    return d

print(count_wordlength("Amazon tests quality at scale"))

#----------------------------------

#Count character types
#Write a function to count how many letters, digits, and special characters are in a string.


#def count_char_types(s):
#    d = {"letters":0,"digits":0,"special":0}
#    for char in s:
#        if char.isalpha():
#            d["letters"]+=1
#        elif char.isdigit():
#            d["digits"]+=1
#        else:
#            d["special"]+=1
#    return d

#print(count_char_types("Amazon2025!#QA"))

#-------------------------------------------

#Word length frequency

#def word_length_map(sentence):
#    words = sentence.split()
#    d = {}
##    for w in words:
#        d[w] = len(w)
#    return d

#print(word_length_map("Quality at Amazon matters"))

#----------------------------------------------

#Filter words by length
#Return words longer than 4 characters from a sentence.

#def long_words(sentence):
#    l = []
#    words = sentence.split()
#    for w in words:
#        if len(w) > 4:
#            l.append(w)
#    return l

#print(long_words("Amazon tests quality at scale"))

#-----------------------------------------------------

#Write a function that takes a sentence and returns a list of the longest word(s) in the sentence. If multiple words have the same maximum length, include all of them.

def long_word(sentence):
    words = sentence.split()
    max_len = max(len(word) for word in words)
    l = []
    l.append(max_len)
    for word in words:
        if len(word) == max_len:
            l.append(len(word))
    return l

#print(long_word("Amazon hires only the best engineers"))

#---------------------------------------------------------

#Count Letter Frequency

#Write a function that takes a sentence as input and returns a dictionary where each letter (case-insensitive) is a key, and its frequency is the value. Ignore digits, spaces, and special characters.

#import string

#def letter_count(sentence):
#    translator = str.maketrans('', '', string.punctuation)
#    sentence = sentence.translate(translator)

#    words = sentence.split()

#   d = {}
#    for w in words:
#        for char in w:
#            if char in d:
#                d[char] += 1
#            else:
#                d[char] = 1
#    return d

#print(letter_count("Amazon hires QA Engineers!"))

#------------------------------------

#Most Frequent Word in a Sentence














