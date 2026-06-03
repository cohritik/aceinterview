#Problem Statement: Given an array of integers nums and an integer target, 
#return the indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution.
#You may not use the same element twice.
#You can return the answer in any order.
#Example:
#Input: nums =
#, target = 9
#Output: 
# (Because nums + nums
# == 9)
#Your Task: Try to solve this using a single loop in O(N) time by leveraging a dictionary to trade space
# for time.

nums = [1, 2, 5, 4, 7]
target = 9

# Brute force approach: iterate through nums array, find the complement then again iterate through nums array and if complement is present
# in array return the indices of loop. O(N**2), O(1)
def brute_force_two_sum(nums, target):

    for i in range(len(nums)):
        complement = target - nums[i]

        for j in range(i+1, len(nums)):
            if nums[j] == complement:
                return [i, j] 
    return False

print(brute_force_two_sum(nums, target))

# Optimized Approach: We will use hash map for storing key- value pair of array item and there indices 
# and find complement then search in hash map if complement is present. 

def optimized_approach_two_sum(nums, target):

    hash_map = {}

    for i in range(len(nums)):

        complement2 = target - nums[i]

        if complement2 in hash_map:
            return [i, hash_map[complement2]]
        
        hash_map[nums[i]] = i
    return []

        

print(optimized_approach_two_sum(nums, target))
        



