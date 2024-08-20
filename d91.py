#plus one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=str()
        for i in digits:
            s+=str(i)
        a=int(s)+1
        return [int(i) for i in str(a)]