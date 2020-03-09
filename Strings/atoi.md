# Atoi

Implement atoi to convert a string to an integer.

Example :

Input : "9 2704"
Output : 9

Note: There might be multiple corner cases here. Clarify all your doubts using “See Expected Output”.

    Questions:

    Q1. Does string contain whitespace characters before the number?
    A. Yes

    Q2. Can the string have garbage characters after the number?
    A. Yes. Ignore it.

    Q3. If no numeric character is found before encountering garbage characters, what should I do?
    A. Return 0.

    Q4. What if the integer overflows?
    A. Return INT_MAX if the number is positive, INT_MIN otherwise.

**Warning : DO NOT USE LIBRARY FUNCTION FOR ATOI.
If you do, we will disqualify your submission retroactively and give you penalty points.**

```python
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

```
