class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            y = str(x)[::-1]
            z = int(y)
            if z in range(-2**31, 2**31):
                return z
            else: return 0
        else:
            x *= -1
            y = str(x)[::-1]
            z = -1 * int(y)
            if z in range(-2**31, 2**31):
                return z
            else: return 0
