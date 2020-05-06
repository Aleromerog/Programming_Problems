class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        start = 1
        end = A
        mid = (end + start) / 2
        while start <= end:
            if mid**2 == A:
                return mid
            elif mid**2 > A:
                end = mid-1
            else:
                start = mid+1
            
        return start