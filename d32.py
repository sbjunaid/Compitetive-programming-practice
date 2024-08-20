#Count Items Matching a Rule

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        a=0
        if ruleKey=="type":
            a=0
        if ruleKey=="color":
            a=1
        if ruleKey=="name":
            a=2
        return [items[i][a] for i in range(len(items))].count(ruleValue)