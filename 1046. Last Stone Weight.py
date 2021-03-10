class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)): stones[i] = -stones[i]
        heapify(stones)
        while len(stones) > 1:
            l1 = -1 * heappop(stones)
            l2 = -1 * heappop(stones)
            if l1 == l2: continue
            new_weight = l1 - l2
            heappush(stones, -new_weight)
            
        return 0 if len(stones) == 0 else -stones[0]
