#Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum=0
        a=nums[0]
        for i in nums:
            if cursum<0:
                cursum=0
            cursum+=i
            a=max(cursum,a)
        return a