#count unique words in a sentence
#If in a sentence you have to remove space, punctuations then use string module and maketrans and translate function

##def count_unique(sentence):
 #  words = sentence.split()
 #  print(words)
 #  d = {}
 #  count = 0
 #  for word in words:
 #      if word in d:
  #         d[word] += 1
  #     else:
  #         d[word] = 1

  # for k,v in d.items():
  #     if v == 1:
  #         count += 1
  # return count

#print(count_unique("Amazon tests Quality. Quality is key at Amazon"))
import string
def unique_count(sentence):
    translator = str.maketrans('','',string.punctuation)
    sentence = sentence.translate(translator).lower()

    words = sentence.split()

    d = {}
    for w in words:
        d[w] = d.get(w, 0) + 1

    count = sum(1 for v in d.values() if v == 1)
    return count

print(unique_count("Amazon tests Quality. Quality is key at Amazon!"))
