#Find N Unique Integers Sum up to Zero

class Solution:
    import math
    def sumZero(self, n: int) -> List[int]:
        if n%2==0:
            u=[]
            l=math.ceil(n/2)+1
        else:
            u=[0]
            l=math.ceil(n/2)
        for i in range(1,l):
            u.append(i)
            u.append(-i)
        return u