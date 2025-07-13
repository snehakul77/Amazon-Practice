#Write code to count the duplicate characters in a given string.

#def duplicate_char(s):
#    d = {}
#    for char in s:
#        if char in d:
#            d[char] += 1
#        else:
#            d[char] = 1
#    count = 0
#    for k,v in d.items():
#        if v > 1:
#            count+=1
#    return count

#print(duplicate_char("abccda"))

#Calculate the frequency of characters in a string. Print each char with its frequency. e.g. For input <abcabc>, output should be <(a,2),(b,2),(c,2)>.

#def freq_char(s):
#    d = {}
##    for c in s:
#        if c in d:
#            d[c] +=1
#        else:
#            d[c] = 1
#    return d
#print(freq_char('abc'))

#Print the first and final occurrence of a number in a sorted array of integers.
#e.g. int[] list = {1,2,3,4,5,5,7,8}
#list = [1,2,3,4,5,5,7,8]
#print(list[0],list[-1])

#Write a program to print the first non-repeated char in a string. e.g. A string “Is it your first company” returns ‘u’.

def nonrepearted_char(s):
    d = {}
    s = s.lower()
    for c in s:
        if c in d:
            d[c] +=1
        else:
            d[c] = 1
    print(d)
    for k,v in d.items():
        if v == 1:
            return k
    return None


print(nonrepearted_char("Is it your first company"))



