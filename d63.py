#Two Sum
  

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=len(nums)
        for i in range(0,l):
            if (target-nums[i]) in nums:
                if i!=nums.index(target-nums[i]):
                    return [i,nums.index(target-nums[i])]
                    break