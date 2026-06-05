# Day 5 Problem: Maximum Average Subarray I
# Here is your problem for today. As requested, there is no solution here—just the prompt! 
# We are going to start with the Fixed Window flavor.
# Problem Statement: You are given an integer array nums consisting of n elements, 
# and an integer k. Find a contiguous subarray whose length is exactly equal to k 
# that has the maximum average value, and return this value.
# Example 1:
# Input: nums = [1, 12, -5, -6, 50, 3], k = 4
# Output: 12.75
# (Explanation: The subarray [12, -5, -6, 50] has the maximum sum of 51. The average is 51 / 4 = 12.75)
# Example 2:
# Input: nums =
# , k = 1
# Output: 5.0
# Your Task: Try to solve this using the Fixed Sliding Window pattern in O(N) time and O(1) space.

# Brute force approach: my approach will be that I will start from first element till k take avg of that
# then i'll start from second element till k take avg of that store in a list. Repeat this untill i reach 
# end element = k that would be my last iteration. then i'll find max. Done

nums = [1, 12, -6, 50, 3]

k = 4

def brute_force_fixed_window(nums, k):

    # Initialize to negative infinity to handle arrays with all negative numbers
    max_avg = float('-inf') 

    for i in range(len(nums) - k + 1):

        total_sum = 0
        
        for j in range(i, k + i):
            total_sum += nums[j]
        
        current_avg = float(total_sum/k)

        if current_avg > max_avg:
            max_avg = current_avg
       
    return max_avg

print(brute_force_fixed_window(nums, k))

# O(N*K) Time complexity
# O(1) Space Complexity

# Optimized approach: We first took the sum of initial window, then we iterated from k to length of array in which we removed a element from \
# left and added the right to the previous window element. Compared the current sum to maximum sum of first window
# O(N) Time complexity


def optimized_approach_fixed_window(nums, k):

    current_sum = sum(nums[:k])
    max_sum = current_sum

    for i in range(k, len(nums)):

        current_sum -= nums[i - k]

        current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
    
    return [max_sum/k]

print(optimized_approach_fixed_window(nums, k))
    



        

       