class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        s = 1
        e = x
        while s <= e:
            mid = s + (e-s)//2
            square = (mid * mid)
            if square == x:
                return mid
            elif square > x:
                e = mid - 1
            else:
                s = mid + 1
        return int(e)