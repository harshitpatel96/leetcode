class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        a bulb would only be on if it was hit odd number of times i.e. for 3 bulb would be hit twice once by switching every 1st bulb and second time by switching every 3rd bulb. Once we move on to switching every 4th bulb, then 3rd bulb would never be touched again. Hence it has been hit even number of times (2 times in case of 3), so its initial state was off, 1st change switched it on and second change switched it off again. So we can see how hitting a bulb odd number of times would leave it ON in the end.
        """
        
        return int(math.sqrt(n))
