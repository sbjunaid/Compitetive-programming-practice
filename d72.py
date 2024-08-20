#Lucky Numbers in a Matrix

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        for i in range(len(matrix)):
            small=min(matrix[i])
            index=matrix[i].index(small)
            x=[]
            for j in range(len(matrix)):
                x.append(matrix[j][index])
            if max(x)==small:
                return [small]
            else:
                x.clear()

                