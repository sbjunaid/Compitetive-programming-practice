# How Many Numbers Are Smaller Than the Current Number


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a={}
        sorted_nums=sorted(nums)
        for i,n in enumerate(sorted_nums):
            if n not in a:
                a[n]=i
        
        return [a[key] for key in nums]