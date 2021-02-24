class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        l, r = 0, len(arr)-1
        
        while l <= r:
            m = l + (r - l)//2
            if (arr[m] - m - 1) < k: # this says if at index m the number present is not (m+1) then the total missing numbers on the left arr[m]-(m+1). if total missing numbers on left are less than k then search on right subarray else search on left subarray
                l = m + 1
            else:
                r = m - 1
                
        return l + k
