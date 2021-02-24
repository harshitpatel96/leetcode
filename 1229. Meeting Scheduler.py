class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        """
        using two pointers
        """
        
        slots1.sort()
        slots2.sort()
        
        i, j = 0, 0
        
        while i < len(slots1) and j < len(slots2):
            start1, end1 = slots1[i]
            start2, end2 = slots2[j]
            e = min(end1, end2)
            s = max(start1, start2)
            if e - s >= duration:
                return [s, min(e, s+duration)]
            
            if end1 < end2: i += 1
            else: j += 1
            
        return []
