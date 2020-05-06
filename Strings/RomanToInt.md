# Roman to integer

Given a string A representing a roman numeral.
Convert A into integer.

A is guaranteed to be within the range from 1 to 3999.

**NOTE:** Read more
details about roman numerals at [Roman Numeric System](https://en.wikipedia.org/wiki/Roman_numerals#Roman_numeric_system)



**Input Format**

    The only argument given is string A.

**Output Format**

    Return an integer which is the integer verison of roman numeral string.

**For Example**

    Input 1:
        A = "XIV"
    Output 1:
        14

    Input 2:
        A = "XX"
    Output 2:
        20

---

### My Solution

```python
class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        for i in A:
            if i > 0 and rom_val[i] > rom_val[i-1]:
                num += rom_val[i] - 2 * rom_val[i-1]
            else:
                num += rom_val[i]

        return num

```
* Python3.6