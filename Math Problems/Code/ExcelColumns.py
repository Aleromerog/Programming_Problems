class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        s = ""
        while A:
            t = A%26
            if t == 0:
                t == 26
            s += chr(64+t)
            A = int(A/26)
        return s
