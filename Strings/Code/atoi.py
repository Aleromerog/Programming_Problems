class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        return int(self.findMyNumber(A))

    def findMyNumber(self,string):
        # flag indicates we found a number
        flag = False
        newStr = ''
        for char in string:
            # Check if char is an acceptable character
            if char.isdigit() or (char == '+' and flag == False) or (char == ' ' and flag == False) or (char == '-' and flag == False):
                if char != ' ':
                    newStr += char
                    flag = True

            else:
                break

        if flag and newStr != '-' and  newStr != '+':
            # Number has to fit in a 32 bit integer
            if int(newStr) > 2**31 -1:
                return 2**31 -1
            if int(newStr) < -(2**31) + 1:
                return -(2**31)

            return newStr
        # If no flag means
        else:
            return 0
