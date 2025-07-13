#Write a function that takes a list of numbers and returns a new list that contains only the numbers which are:
#greater than 10 and even

#def is_even(n):
#    l = []
#    for i in n:
##        if i % 2 == 0 and i > 10:
#            l.append(i)
#    return l

#print(is_even([4,12,14,6,8,13,20]))

#--------------------------------

#Filter Odd Numbers Less Than 10

def filter_odd(n):
    l = []
    for i in n:
        if i % 2 != 0 and i < 10:
            l.append(i)
    return l

print(filter_odd([3,4,5,7,12,13,15]))

