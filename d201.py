#Search Insert Position


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        end=len(nums)
        start=0
        while(start<end):
            mid=(start+end)//2
            if target<=nums[mid]:
                end=mid
            elif target>nums[mid]:
                start=mid+1
            else:
                return mid     
                
        return start

