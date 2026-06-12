# Problem Statement: Given the root of a binary tree, return its maximum depth. 
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down 
# to the farthest leaf node.
# (Assume you are given a TreeNode class that has val, left, and right attributes).
# Example 1:
# Input: root = [3, 9, 20, null, null, 15, 7] (Imagine 3 is the root. 9 and 20 are its children.
#  15 and 7 are the children of 20).
# Output: 3
# Example 2:
# Input: root = [1, null, 2]
# Output: 2
# Your Task: Try to solve this using the Tree DFS pattern with recursion


root = [3, 9, 20, 'null', 'null', 15, 7] 

def tree_dfs(root):

    if root is None:
        return 0
    
    left_depth = tree_dfs(root.left)
    right_depth = tree_dfs(root.right)

    return 1 + max(left_depth, right_depth)

# Time Complexity: O(N)
# Space complexity: O(H)



