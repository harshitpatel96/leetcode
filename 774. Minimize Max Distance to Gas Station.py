class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        
        def isPossible(D):
            return sum(int((stations[i+1] - stations[i]) / D) for i in range(len(stations) - 1)) <= k
        
        l, r = sum(int((stations[i+1] - stations[i]))), 10**8
        while r - l > 1e-6:
            mid = l + (r - l) / 2
            if isPossible(mid):
                r = mid
            else:
                l = mid
                
        return l
