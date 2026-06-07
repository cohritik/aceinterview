# Day 6 Problem: Longest Substring Without Repeating Characters
# Here is your problem for today. As usual, no solution is provided yet! 
# This is a classic interview question asked frequently at companies like Google
# .
# Problem Statement: Given a string s, 
# find the length of the longest substring without repeating characters
# .
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# (Explanation: The answer is "abc", with the length of 3.)
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# (Explanation: The answer is "b", with the length of 1.)
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# (Explanation: The answer is "wke", with the length of 3. Notice that the answer must be a contiguous substring, so "pwke" is a subsequence and not a valid answer.)
# Your Task: Try to solve this using the Dynamic Sliding Window pattern in O(N) time
# .


# Brute Force approach: Use hash set for stroing the unique subset, iterating through the whole string if 
# duplicate element is found reset the hash set before that take a count of hash set. Store the count in a array
# after whole iteration will check the max in array

s = 'abcabcbb'

def brute_force_substring(s):

    hash_set = set()
    count_array = []

    for i in s:
        if i in hash_set:
            print(hash_set)
            count_array.append(len(hash_set))
            hash_set = set()
        hash_set.add(i)
    
    return max(count_array)

print(brute_force_substring(s))


def optimized_substring(s):

    hash_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):

        while s[right] in hash_set:
            hash_set.remove(s[right])
            left += 1
        
        hash_set.add(s[right])

        max_length = max(max_length, right - left + 1)
    
    return max_length

print(optimized_substring(s))
