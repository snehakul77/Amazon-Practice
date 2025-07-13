#2 point DSA problem : Check if Array Has a Pair with a Given Sum

#def has_pair_with_target(arr,target):
#    left = 0
#    right = len(arr) - 1

#    while left < right:
#        curr_sum = arr[left] + arr[right]
#        if curr_sum == target:
#            return True
#        elif curr_sum < target:
#            left += 1
#        else:
#            right -= 1
#    return False

#print(has_pair_with_target([1, 2, 3, 4], 7))

#Remove duplicates from the sorted array

def remove_duplicate(nums):
    if not nums:
        return 0
    slow = 0

    for fast in range(1,len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1


print(remove_duplicate([1, 1, 2, 2, 3]))
