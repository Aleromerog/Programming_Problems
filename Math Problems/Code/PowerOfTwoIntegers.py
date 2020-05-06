import math
class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        for i in range (2, int(A**1/2)+1):
            y = 0
            while(i**y <= A):
                if(i**y == A):
                    return 1
                y += 1
        return 0
