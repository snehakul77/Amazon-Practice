#Script to calculate the number of occurances of given element in an array

#def count_element(arr,target):
#    count = 0
#    for element in arr:
#        if element == target:
#            count += 1
#    return count

#if __name__ == "__main__":
#    array = [1,2,4,4,5,6,7,8]
#    target = 4
#    result = count_element(array,target)
 #   print(f"The count of {target} is {result}")

#Given a number in an array form. Write a program to move all zeros to the end.

#def move_zeros(arr):
#    non_zeros = 0

#    for i in range(len(arr)):
#        if arr[i] != 0:
##            arr[non_zeros] = arr[i]
  #          non_zeros+=1

#    for i in range(non_zeros,len(arr)):
#        arr[i] = 0

#    return arr

#if __name__ == "__main__":
#    array = [0,1,0,3,12]
#    result = move_zeros(array)
#

#Given are two ordered lists of sizes 7 and 3. The first list has three vacant spots in the end. Merge them in a sorted manner with a minimum number of steps.
#a = [1,5,6,3]
#b = [9,7,8,2]

#def merge_array(a,b):
#    c = a + b
 #   c.sort()
#    return c

#print(merge_array(a,b))

def merge_sorted_list(list1,list2,m,n):
    i = m - 1 
    j = n - 1
    k = m + n - 1
    while i>=0 and j>=0:
        if list1[i] > list2[j]:
            list1[k] = list1[i]
            i -=1
        else:
            list1[k] = list2[j]
            j -= 1
        k -=1

    while j>=0:
        list1[k] = list2[j]
        j -=1
        k -=1
    return list1

if __name__ =="__main__":
    list1 = [1,3,5,7,None,None,None]
    list2 = [2,4,6]
    result = merge_sorted_list(list1,list2,4,3)
    print(f"Merged list :" ,result)


