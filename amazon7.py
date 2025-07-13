
#Write a function to reverse a string
#def reverse_string(sentence):
#    sentence = sentence[::-1]
#    return sentence

#print(reverse_string("My name is sneha"))

#Write a function to check if two strings are anagrams of each other.

#def check_anagram(s1,s2):
#    if sorted(s1) == sorted(s2):
#        return True
#    else:
 #       return False

#print(check_anagram("hello","world"))

#Write a function that takes a list and returns a new list with duplicates removed, preserving the order of first occurrence.

#def remove_duplicates(s):
##   seen = set()
 #   result = []
 #   for item in s:
 #       if item not in seen:
 #           result.append(item)
 #           seen.add(item)
  #  return result

#print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

#Find maximum and minimum in an array

#def find_max(lst):
#    max_num = max(lst)
#    return max_num

#def find_min(lst):
#    min_num = min(lst)
#    return min_num

#print(find_max([10, 2, 33, 5, 1]))
#print(find_min([10, 2, 33, 5, 1]))

#Write a function to check if a list of numbers is sorted in ascending order.

#def sorted_num(lst):
#    if lst == sorted(lst):
#        return True
#    else:
#        return False

#print(sorted_num([1, 3, 2, 4]))

#Count Occurrences of Each Character in a String

#def char_count(s):
#    d = {}
#    for c in s:
#        if c in d:
#            d[c] += 1
#        else:
#            d[c] = 1
#    return d

#print(char_count("sneha"))

#Find the Second Largest Number in a List

#def find_secondmax(lst):
#    max_num = sorted(lst, reverse=True)
#    return max_num[1]

#print(find_secondmax([10, 20, 20, 4, 45, 99]))

#Given an array, move all 0s to the end while keeping the order of non-zero elements.

def move_zeros(lst):
    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(i)
    return lst

print(move_zeros([0, 1, 0, 3, 12]))


