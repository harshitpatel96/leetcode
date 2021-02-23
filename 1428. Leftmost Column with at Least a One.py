# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        """
        binary search O(m*log(n))
        """
        m, n = binaryMatrix.dimensions()
        rmax = n-1
        smallestInd = n
        for row in range(m):
            left, right = 0, rmax
            while left < right:
                mid = left + (right - left)//2
                midVal = binaryMatrix.get(row, mid)
                if midVal == 0:
                    left = mid+1
                else:
                    right = mid
        
            if binaryMatrix.get(row, left) == 1:
                smallestInd = min(smallestInd, left)
                rmax = left
            
                    
        return -1 if smallestInd == n else smallestInd
                
        
        
        """Right to Left, Top to Down approach
           Start from top right cell
           Found a 0 move Down
           Foudn a 1 move Left
           Until Row or Column Exhausted
        """
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        m, n = binaryMatrix.dimensions()
        
        row, col = 0, n-1
        while row < m and col >= 0:
            if binaryMatrix.get(row, col) == 1:
                col -= 1
            else:
                row += 1
        
        return col + 1 if col != n-1 else -1
