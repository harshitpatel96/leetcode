# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> bool:
#        
#
#    def isTarget(self) -> None:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        revD = {"U": "D", "D": "U", "L": "R", "R": "L"}
        dirs = {"U": (-1,  0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        visited = set()
        def dfs(x, y):
            if (x, y) in visited: return
            
            if master.isTarget():
                G[(x, y)] = 2
                return
            
            G[(x, y)] = 1
            visited.add((x, y))
            for d in "UDLR":
                nr, nd = x + dirs[d][0], y + dirs[d][1]
                if master.canMove(d):
                    master.move(d)
                    dfs(nr, nd)
                    master.move(revD[d])
            
        
        G = {}
        dfs(0, 0)
        visited = set()
        q = collections.deque([(0, 0, 0)])
        
        while q:
            cx, cy, cost = q.popleft()
            if G[(cx, cy)] == 2:
                return cost
            
            for d in "UDLR":
                nr, nd = cx + dirs[d][0], cy + dirs[d][1]
                if (nr, nd) in visited or (nr, nd) not in G: continue
                visited.add((nr, nd))
                q.append((nr, nd, cost+1))
            
        return -1
