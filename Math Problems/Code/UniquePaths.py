import math
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        n = A-1 + B-1
        r = B-1
        return int(math.factorial(n) / (math.factorial(n-r) * math.factorial(r)))
