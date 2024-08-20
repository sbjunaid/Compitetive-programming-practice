#Flipping an Image

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        newlist = []
        for item in image:
            newlist.append(list(map(lambda x: 1 if x==0 else 0, item[::-1])))
        return newlist