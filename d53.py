#Add to Array-Form of Integer

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s=str()
        for i in num:
            s+=str(i)
        s=int(s)+k
        return map(int,[i for i in str(s)])