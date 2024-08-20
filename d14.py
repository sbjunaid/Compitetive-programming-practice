#richest customer wealth
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        s=0
        for i in accounts:
            s=max(sum(i),s)
        return s