# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        """
        "4 (2(3)(1)) (6(5)(7))"
        """
        
        n = len(s)
        
        def dfs(start, end):
            
            if start >= end: return None
            currEnd = start
            while currEnd < end and s[currEnd] != "(":
                currEnd += 1
            
            node = TreeNode(s[start:currEnd])
            if currEnd == end: return node
            
            leftParans, rightParans = 0, 0
            
            for partition in range(currEnd, end):
                leftParans += s[partition] == "("
                rightParans += s[partition] == ")"
                if leftParans == rightParans: break
            
            node.left = dfs(currEnd+1, partition)
            node.right = dfs(partition + 2, end-1)
            return node
        
        return dfs(0, n)
