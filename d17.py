#Number of Good Pairs

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    a.append(1)
        return len(a)