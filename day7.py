# Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(logN) runtime complexity.
# Example 1:
# Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
# Output: 4
# (Explanation: 9 exists in nums and its index is 4)
# Example 2:
# Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
# Output: -1
# (Explanation: 2 does not exist in nums so return -1)
# Your Task: Try to solve this by managing a left and right pointer and 
# using a while loop to continuously bisect the array


# nums = [-1, 0, 3, 5, 9, 12]
# target = 9

nums = [-1, 0, 3, 5, 9, 12]
target = 2

def binary_search(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right: 

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        elif nums[mid] < target:
            left = mid + 1 

        elif nums[mid] > target:
            right = mid - 1
        
    return -1

print(binary_search(nums, target))