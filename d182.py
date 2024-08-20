#Arranging Coins


class Solution:
            #approach 1 binary solution
    def arrangeCoins(self, n: int) -> int:
        # return int((math.sqrt(8 * n + 1)-1)/2)
        # approach 3
        low,total=1,n
        res=0
        while low<=total:
            mid=(low+total)//2
            count=(mid/2)*(mid+1)
            if count<=n:
                res=mid
                max(res,mid)
                low=mid+1
            else:
                total=mid-1
        return res