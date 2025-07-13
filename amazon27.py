#split

#def words_len(s):
#    words = s.split()
#    print(words)
#    d = {}
#    for w in words:
#        if w not in d:
#            d[w] = len(w)
#    return d



#words_lenght = words_len("Python is a wonderful scripting language")
#print(words_lenght)

#From the following list, create a new list of cubes of even numbers only:

#def cubes_even(lst):
#    return [i**3 for i in lst if i % 2 == 0]

#print(cubes_even([1,2,3,4,5,6,7,8,9]))

#The union, intersection, and difference of these two sets

#set1 = {1, 2, 3, 4}
#set2 = {3, 4, 5, 6}

#union = set1 | set2
#difference = set1 - set2
#intersection = set2 & set1

#print(union)
#print(difference)
#print(intersection)

#Dictionay comprehension

#Convert this list into a dictionary where the key is the number and the value is its square:

#def convert_type(lst):
#    d = {}
##    for item in lst:
#        if item not in d:
#            d[item] = item*item
#    return d

#  d = {item = item*item for item in lst}

#print(convert_type([1, 2, 3, 4, 5]))

#Filter odd numbers from this list:
#lst = [1, 2, 3, 4, 5, 6, 7]

#odd = list(filter(lambda x: x%2 != 0, lst))
#print(odd)

#Sort this list of words by their length:
words = ["apple", "banana", "fig", "cherry"]
words_sort = sorted(words, key=len, reverse=True)
print(words_sort)
