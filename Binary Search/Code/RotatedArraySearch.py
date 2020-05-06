class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        A = list(A)
        start = A[0]
        for i in range(len(A)):
            A.remove(A[0])
            A.append(start)
            if A[0] < start:
                break
            start = A[0]
            
        start = 0
        end = len(A)-1
        mid = (start + end) / 2
        
        while start <= end:
            if A[mid] == B:
                return mid
            elif A[mid] > B:
                start = mid+1
            else:
                end = mid-1
                
        return -1