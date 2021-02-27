from heapq import *
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        scores = collections.defaultdict(list)
        
        for id, score in items:
            
            heappush(scores[id], score)
            if len(scores[id]) > 5:
                heappop(scores[id])
        
        
        ans = []
        for id, topScores in scores.items():
            ans.append([id, sum(topScores)//min(5, len(topScores))])
        
        ans.sort()
        return ans
