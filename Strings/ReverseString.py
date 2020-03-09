class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        #split the words into a list
        words = A.split()
        rev = []
        #Insert every word in order at the beginning of the new list
        for word in words:
            rev.insert(0, word)
        
        return ' '.join(rev)
