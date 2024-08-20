#Find the Highest Altitude

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum=0
        l=[0]
        n=len(gain)
        for i in range(n):
            sum+=gain[i]
            l.append(sum)
        return max(l)