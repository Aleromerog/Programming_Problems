class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        s = '1'
        for i in range(1,A):
            index = 0
            val = ''
            newS = ''
            # Add to the NewString the counted numbers recieved in count function
            while index < len(s):
                counter = self.count(s, index)
                val = s[index]
                index += counter
                newS += str(counter) + val
            s = newS

        return s

    #Count how many consecutive numbers exist in the given String
    def count(self,s, index):
        val = s[index]
        counter = 0
        while s[index] == val:
            counter +=1
            index +=1
            if index > len(s)-1:
                break
        return counter
