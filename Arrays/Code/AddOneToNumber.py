class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        # Will itererate from the last element to the first until is not a 9
        # If the element is not 9 then just add one.
        for i in range(len(A)):
            if(A[len(A)-1 -i] != 9):
                A[len(A)-1 -i] += 1
                break
            A[len(A)-1 -i] = 0
            # If first element reached then just add one at the begining
            if i == len(A)-1:
                A.insert(0, 1)
        # Removing unnesesary 0's at the left of the number
        while A[0] == 0:
            A.pop(0)
        return A
