#Create Target Array in the Given Order

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans=[]
        d=len(nums)
        for i in range(d):
            ans.insert(index[i],nums[i])
        return ans