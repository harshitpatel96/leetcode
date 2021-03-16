class Solution:
    def __init__(self):
        self.parents = []
        self.size = []
        
    def find(self, c):
        root = self.parents[c]
        while root != self.parents[root]:
            root = self.parents[root]
            
        while self.parents[c] != root:
            tmp = self.parents[c]
            self.parents[c] = root
            c = tmp
        
        return root
    
    def union(self, c1, c2):
        root1, root2 = self.find(c1), self.find(c2)
        if root1 == root2: return
        if self.size[root1] < self.size[root2]:
            self.parents[root1] = root2
            self.size[root2] += self.size[root1]
        else:
            self.parents[root2] = root1
            self.size[root1] += self.size[root2]
    
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.parents = [i for i in range(len(s))]
        self.size = [1 for i in range(len(s))]
        for i, j in pairs:
            self.union(i, j)
            
        connected_slots = collections.defaultdict(list)
        connected_chars = collections.defaultdict(list)
        for i in range(len(s)):
            root = self.find(i)
            connected_slots[root].append(i)
            connected_chars[root].append(s[i])
        
        result = ['' for x in range(len(s))]
        for root in connected_slots:
            sorted_chars = sorted(connected_chars[root])
            for index, slot in enumerate(connected_slots[root]):
                result[slot] = sorted_chars[index]
                
        return ''.join(result)
                
                    
