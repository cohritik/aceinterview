# Day 8 Problem: Valid Parentheses
# Here is your problem for today. This is one of the most frequently asked interview questions of all 
# time (especially at companies like Microsoft), and it perfectly tests your ability to use a stack
# . As always, no solution is provided yet!
# Problem Statement: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Example 1:
# Input: s = "()[]{}"
# Output: True
# Example 2:
# Input: s = "([)]"
# Output: False (Explanation: The square bracket closes before the inner parenthesis does.)
# Example 3:
# Input: s = "{[]}"
# Output: True
# Your Task: Try to solve this in O(N) time and O(N) space

s = ")[]{}"

def valid_parentheses(s):

    parenthese_pair = {
        ')':'(',
        ']':'[',
        '}':'{'
    }

    stack = []

    for parenthese in s:

        if parenthese in parenthese_pair:
            top = stack.pop() if stack else '#'
            if parenthese_pair[parenthese] != top:
                return False
        else:        
            stack.append(parenthese)

    return not stack 
print(valid_parentheses(s))


# Time Complexity: O(N)
# Space Complexity: 0(K)