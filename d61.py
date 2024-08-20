#Maximum Population Year

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        a=[0]*101
        for birth,death in logs:
            a[birth-1950]+=1
            a[death-1950]-=1
        print(a)
        c=m=year=0
        for i in range(101):
            c+=a[i]
            if c>m:
                m=c
                year=i+1950
        return year