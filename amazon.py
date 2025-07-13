#WAP to feverse a string
#def reverse_string(s):
#    return s[::-1]

#print(reverse_string("amazon"))

#----------------------

#Write a function that counts the number of vowels (a, e, i, o, u) in a given string (case-insensitive)

#def count_vowels(s):
#    count = 0
#    for char in s.lower():
#        if char in 'aeiou':
#            count += 1
#    return count

# Test
#print(count_vowels("Amazon Quality"))

#--------------------------------------

#Write a function that takes a list of integers and returns the maximum number.

#def find_max(nums):
#    max_num = nums[0]
##    for num in nums:
 #       if num > max_num:
 #           max_num = num
 #   return max_num

#print(find_max([5,2,3,7,8,5]))

#Write a function that takes a string and returns a dictionary where the keys are words and the values are the number of times each word appears.
#This is letter frequency count
#def word_frequency(word):
#    freq = {}
#    for char in word:
#        if char not in freq:
#            freq[char] = 1
#        else:
#            freq[char] += 1
#    return freq

#result = (word_frequency("this is a test this is only a test"))
#print(result)

#def word_frequency(text):
#    freq = {}
#    words = text.split()
#    for word in words:
#        if word in freq:
#            freq[word] += 1
 #       else:
#            freq[word] = 1
#    return freq

#count = word_frequency("this is a test this is only a test")
#print(count)
#---------------------------------
#Palindrome checker

import string
#def is_palindrome(s):
#    s = s.lower()
#    s = "".join(char for char in s if char.isalnum())
#    return s == s[::-1]
#print(is_palindrome("A man, a plan, a canal, Panama"))

#WAP to check if a number is plaindrome or not

#def is_numpalindrome(n):
#   if n < 0:
#        return False

#    original = str(n)
#    reverse = original[::-1]
#    return original == reverse

#print(is_numpalindrome(121))

#---------------------------------------------

#Find Duplicates in a List

#def find_duplicates(nums):
#    L = []
#    D = []
 ##   for num in nums:
  #      if num not in L:
  #          L.append(num)
  #      else:
  #          D.append(num)
  #  return D

#duplicate = find_duplicates([1, 2, 2, 2, 3, 3, 4])
#print(duplicate)

#-----------------

#Write a function that takes a string and returns the first character that does not repeat anywhere in the string

##def first_nonrepeating(s):
 #   d = {}
 #   for x in s:
 #       if x not in d:
 #           d[x] = 1
 #       else:
 #           d[x] += 1
 #   return d

#dict = first_nonrepeating("aabbccdde")
##for x in dict:
 #   if dict[x] == 1:
 #       print(x)
 #       break

 #------------------------------------

 #Write a function that checks whether two strings are anagrams of each other.

def are_anagrams(str1,str2):
    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ','').lower()
    return sorted(str1) == sorted(str2)

print(are_anagrams("listen","silent"))



