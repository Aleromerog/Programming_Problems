class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):

        for i in range(len(A)):
            if(A[len(A)-1 -i] != 9):
                A[len(A)-1 -i] += 1
                break
            A[len(A)-1 -i] = 0
            if i == len(A)-1:
                A.insert(0, 1)

        while A[0] == 0:
            A.pop(0)
        return A
            
