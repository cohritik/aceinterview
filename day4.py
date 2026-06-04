# Day 4 Problem: Valid Palindrome
# Here is your problem for today. As requested, there is no solution—just the prompt!
# Problem Statement: Given a string s, return True if it is a palindrome, or False otherwise. 
# A string is a palindrome if, after converting all uppercase letters into lowercase letters and 
# removing all non-alphanumeric characters, it reads the same forward and backward.
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: True (Because "amanaplanacanalpanama" reads the same forward and backward)
# Example 2:
# Input: s = "race a car"
# Output: False (Because "raceacar" is not a palindrome)
# Your Task: Try to solve this using the Two Pointers pattern in O(N) time and O(1) space
# .

# Brute force approach: iterate the string also in another nested loop iterate from ending and match. if no match then 
# false, if for whole iteration matched then true. But the solution is in O(N2) and Space O(N) 

s = "A man, a plan, a canal: Panama"

#s = "race a car"
only_char = ''.join(char for char in s if char.isalpha())

clean_text = only_char.lower()


def brute_force_palindrome(clean_text):
  
    for forward in clean_text:
        for backward in range(len(clean_text) -1 , 0, -1):
        
            if forward != clean_text[backward]:
                return False
    
    return True

print(brute_force_palindrome(clean_text))

# Optimized apprach will use 2 pointer. I will have a pointer for low will be starting and one pointer at end named high
# will start with comparing low with high and in each iteration will increment low by 1 and decrement high by one
# first will check if not matching will return false. and if low = high i.e. mid value so it is palindrome

def optimized_approach_palindrome(clean_text):
   
    low = 0
    high = len(clean_text) - 1

    while low < high:

        if clean_text[low] != clean_text[high]:
            return False
        
        else:
            low += 1
            high -= 1
    
    return True

print(optimized_approach_palindrome(clean_text))

