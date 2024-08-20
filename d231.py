#Check If N and Its Double Exist

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        a=len(arr)
        for i in range(a):
            if 2*arr[i] in arr and i!=arr.index(2*arr[i]):
                return True
                break