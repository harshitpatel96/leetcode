# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        pathtop =self.getPath(root, p)
        pathtoq = self.getPath(root, q)

        i, j = 0, 0
        while i < len(pathtop) and j < len(pathtoq):
            if pathtop[i] != pathtoq[j]:
                return pathtop[i-1]
            i += 1
            j += 1

        if i == len(pathtop):
            return pathtop[i-1]
        return pathtoq[j-1]

            
    def getPath(self, root, node):
        if not root:
            return
        if root.val == node.val:
            return [root]
        
        left = self.getPath(root.left, node)
        if left:
            return [root] + left
        right = self.getPath(root.right, node)
        if right:
            return [root] + right
        
        return
        
