#Valid Perfect Square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Base case: 1 is a perfect square
        if num == 1:
            return True
        
        # Binary search for the square root of the number
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1
        
        # If we haven't found the square root, the number is not a perfect square
        return False