class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        self.put(0, A, A[0])

    def put(self, ind, A, val):
        newInd = A.index(ind)
        temp = A[newInd]
        A[newInd] = val
        self.put(newInd, A, temp)
        
        
