#Write a script to print the number of occurrences of a given character or all letters in a string

#def count_occurances(s,c):
#    count = 0
#    for char in s:
#        if char == c:
#            count += 1
#    return count

#print(count_occurances("sneha","e"))

#def count_occurance(s):
#    d = {}
#    for char in s:
#        if char in d:
#            d[char] += 1
#        else:
#            d[char] = 1
#    return d

#print(count_occurance("abba"))

#How to reverse an array in the subset of N

def reverse_array(arr,n):
    result = []
    for i in range(0, len(arr),n):
        chunk = arr[i:i+n]
        result.extend(chunk[::-1])
    return result

if __name__ == "__main__":
    array = [1, 3, 5, 7, 9, 11, 15, 17, 19]
    N = 3
    output = reverse_array(array,N)
    print(output)

