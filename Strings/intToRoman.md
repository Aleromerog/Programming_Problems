# Integer to Roman

Given an integer A, convert it to a roman numeral, and return a string corresponding to its roman numeral version

    Note : This question has a lot of scope of clarification from the interviewer. Please take a moment to think of all the needed clarifications and see the expected response using “See Expected Output”

    For the purpose of this question, https://projecteuler.net/about=roman_numerals has very detailed explanations.



**Input Format**

    The only argument given is integer A.

**Output Format**

    Return a string denoting roman numeral version of A.

**Constraints**

```1 <= A <= 3999```

**For Example**

    Input 1:
        A = 5
    Output 1:
        "V"

    Input 2:
        A = 14
    Output 2:
        "XIV"

---

### Solution

```python
class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        rom = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        i = 0
        romNum = ''
        while A > 0:
            for j in range(A // val[i]):
                A -= val[i]
                romNum += rom[i]
            i += 1

        return romNum

```
