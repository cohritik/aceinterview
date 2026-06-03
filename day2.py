# Given an integer array nums, return true if any value appears at least twice in the array, and 
# return false if every element is distinct.

# Brute force: Idea is iterate through the nums array twice in 2 for loops then check for matching index if match is found
# increase count by 1. After the loop is closed then check if count is greater than 2.

nums = [1, 2, 5, 6, 34, 1, 2, 5, 6]

n = nums

def brute_force_solution(n):
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if n[i] == n[j]:
                return True 
    return False

print(brute_force_solution(nums)) 

# Above solution time complexcity is O(n**2) as there are 2 loops. And space complexcity is 1 

# Optimized solution: Hash map can be used for storing count/ frequency and in the end we can check if any value in dictionary is greater than 1

def optimized_solution(nums):
    unique_array = set()
    for value in nums:
        if value in unique_array:
            return True
        unique_array.add(value)
    return False

print(optimized_solution(nums))


        
