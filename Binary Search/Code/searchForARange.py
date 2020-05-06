class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        index1 = -1
        index2 = -1
    
        start = 0
        final = len(A)-1
        mid = (start + final) // 2
        while start <= final:
            if A[mid] == B:
                index1, index2 = self.findIndex(mid, index1, index2, A, B)
                break
            elif A[mid] < B:
                start = mid+1
                mid = (start + final) // 2
            else:
                final = mid-1
                mid = (start + final) // 2
    
        return [index1, index2]
    
    def findIndex(self, mid, index1, index2, A, B):
        t = mid
        while mid < len(A):
            if A[mid] == B:
                index2 = mid
                mid += 1
            else:
                break
        mid = t
        while mid >= 0:
            if A[mid] == B:
                index1 = mid
                mid -= 1
            else:
                break
        return index1, index2
            
        
        
        
        
        