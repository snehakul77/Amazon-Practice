#Find First Non-Repeating Character

#Given a string, return the first character that does not repeat. If all characters repeat, return

#def first_unique(s):
#    d = {}
##    for i in s:
#        if i in d:
#            d[i] +=1
#        else:
#            d[i] = 1
#    print(d)

#    for i in d:
#        if d[i] == 1:
#            return i
#    return None

#print(first_unique("amazon"))
#------------------------------------------------------------------------------------
#Longest Substring Without Repeating Characters

#Given a string s, find the length of the longest substring without repeating characters.

#def longest_substring(s):
#    left = 0
#    seen_chars = set()
#    max_length = 0

#    for right in range(len(s)):
#        while s[right] in seen_chars:
#            seen_chars.remove(s[left])
 #           left += 1

#        seen_chars.add(s[right])
#        max_length = max(max_length, right - left + 1)
#    return max_length

#print(longest_substring("abcabcbb"))
#--------------------------------------------------------
# Maximum Sum of Subarray of Size K
#Given an array of integers and a number k, find the maximum sum of any contiguous subarray of size k.

#def max_sum_subarray(arr,k):

#    window_sum = sum(arr[:k])
#    max_sum = window_sum
#    for i in range(k,len(arr)):
##        window_sum = window_sum - arr[i-k] + arr[i]
 #       if window_sum > max_sum:
 #           max_sum = window_sum
 #   return max_sum

#print(max_sum_subarray([2, 1, 5, 1, 3, 2],3))
#-------------------------------------------------
#Minimum Size Subarray Sum (Variable Sliding Window)
#Given an array of positive integers arr and a target sum target, find the length of the smallest contiguous subarray whose sum is greater than or equal to target.
#If no such subarray exists, return 0.

def min_subarray(arr,target):
    start = 0
    end = len(arr)-1
    window_sum = 0
    min_length = 0
    while end in range(len(arr)):
        window_sum += arr[end]
        if window_sum >= target:
            min_length = end-start+1
        window_sum -= arr[start]
        start += 1
    return(min_length)

print(min_subarray([2, 3, 1, 2, 4, 3],7))


















