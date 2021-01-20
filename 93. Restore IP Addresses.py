class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(dotPos):
            if len(dotPos) == 3:
                validIP, ip = validateIP(dotPos)
                if validIP: allIps.add(ip)                  
                return
            
            prevDot = len(dotPos) if not dotPos else dotPos[-1]
            for i in range(prevDot+1, n):
                backtrack(dotPos + [i])
        
        def validateIP(dotPos):
            lastPos = 0
            newip = []
            for pos in dotPos:
                newip.append(s[lastPos:pos])
                lastPos = pos

            newip.append(s[lastPos:])
            for subip in newip:
                if not 0 <= int(subip) <= 255 or (len(subip) > 1 and subip[0]=='0'):
                    return False, None
            return True, ".".join(newip)
        
        n = len(s)
        if n > 12: return []
        allIps = set()
        backtrack([])
        return allIps
        
