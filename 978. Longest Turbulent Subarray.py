class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        [ 9 > 4 < 11 < 12 7 8 8 1 9 ]
          0 1 2    3   4  5 6 7 8
            
        """
        if len(arr) == 1: return 1
        
        currLen = 2 if arr[0] != arr[1] else 1
        maxLen = currLen
        
        for r in range(2, len(arr)):
            
            if arr[r] == arr[r-1]:
                currLen = 1
            elif arr[r] > arr[r-1] >= arr[r-2] or arr[r] < arr[r-1] <= arr[r-2]:
                currLen = 2
            else:
                currLen += 1
                
            maxLen = max(currLen, maxLen)
        
        return maxLen
