#Find the Missing Number
#You are given a list of n-1 integers in the range 1 to n.
#There are no duplicates, and exactly one number is missing.
#Write a function to find that missing number.

#def find_num(num):
#    n = len(num) + 1

#    expected_sum = n * (n + 1) // 2
#    actual_sum = sum(num)
#    missing_sum = expected_sum - actual_sum
#    return missing_sum


#print(find_num([1, 2, 4, 6, 3, 7, 8]))

#-----------------------------
#Write a function to return all the duplicates, without repeating any in the result.

#def find_duplicates(nums):
#    d = {}
#    for num in nums:
#        if num in d:
#            d[num] += 1
#        else:
#            d[num] = 1
#    print(d)
#    l = []
#    for key, value in d.items():
#        if value > 1:
#            l.append(key)
#    return l

#print(find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))

#-----------------------------

#check even numbers in list

#def is_even(nums):
#    l = []
#    for num in nums:
#        if num % 2 == 0:
#            l.append(num)
#    return l

#even = is_even([1, 2, 3, 4, 5, 6])
#print(even)

#--------------------------------------

#Write a function to count how many words in a sentence start with a capital letter.


def is_caps(sentence):
    words = sentence.split()
    counter = 0
    for c in words:
        if c[0].isupper():
            counter += 1
    return counter

sentence = "Amazon Quality Engineers Ensure Excellence"
print(is_caps(sentence))



#
