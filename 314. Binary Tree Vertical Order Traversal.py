# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        arrs = {}
        minInd, maxInd = inf, -inf
        q = collections.deque([[root, 0]])
        minInd, maxInd = inf, -inf
        while q:
            n = len(q)
            for i in range(n):
                node, ind = q.popleft()
                minInd = min(ind, minInd)
                maxInd = max(ind, maxInd)
                if ind not in arrs: arrs[ind] = [node.val]
                else: arrs[ind].append(node.val)
                if node.left: q.append([node.left, ind-1])
                if node.right: q.append([node.right, ind+1])
                
        ans = []
        for i in range(minInd, maxInd+1):
            ans.append(arrs[i])
        return ans
