class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        """
        w b w w b
        w w w w b
        w w b w w
        
        """
        
        m, n = len(picture), len(picture[0])
        cols = [0]*n # shows number of 1s in each column
        rows = set()
        for r in range(m):
            currRowOnes = 0
            for c in range(n):
                if picture[r][c] == "B":
                    cc = c
                    currRowOnes += 1
                    cols[c] += 1
                    
            if currRowOnes == 1: rows.add(cc)
        
        lonelyCount = 0
        for c, count in enumerate(cols):
            if count == 1 and c in rows:
                lonelyCount += 1
        
        return lonelyCount
