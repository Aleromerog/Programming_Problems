class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        # Check if String B exists in A, and return the index where it begins
        if B in A:
            return A.index(B)
        else:
            return -1
