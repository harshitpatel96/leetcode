class UF:
    def __init__(self, vars):
        self.parents = {var: var for var in vars}
        self.size = {var: 1 for var in vars}
        
    def find(self, var):
        root = self.parents[var]
        while root != self.parents[root]:
            root = self.parents[root]
        
        while self.parents[var] != root: 
            var, self.parents[var] = self.parents[var], root
            
        return root
    
    def union(self, var1, var2):
        root_1, root_2 = self.find(var1), self.find(var2)
        if root_1 == root_2: return
        if self.size[root_1] < self.size[root_2]:
            self.parents[root_1] = root_2
            self.size[root_2] += self.size[root_1]
        else:
            self.parents[root_2] = root_1
            self.size[root_1] += self.size[root_2]
            

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        vars = set()
        for eqn in equations: 
            vars.add(eqn[0])
            vars.add(eqn[-1])
        
        uf = UF(vars)
        for eqn in equations:
            if eqn[1:-1] == "==":
                uf.union(eqn[0], eqn[-1])
        
        for eqn in equations:
            if eqn[1:-1] == "!=" and uf.find(eqn[0]) == uf.find(eqn[-1]):
                return False
        return True
