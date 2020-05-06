import itertools

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        ways = 0
        permu = [p for p in itertools.product(A, repeat=B)]
        for sub in permu:
            s = ""
            for i in sub:
                s+= str(i)
            num = int(s)
            if( len(str(num)) == B ):
                if num < C:
                    ways += 1
        return ways
            