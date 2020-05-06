# Excel Column Title


Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 


## **My solution**

```python
class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        s = ""
        while A:
            t = A%26
            if t == 0:
                t == 26
            s += chr(64+t)
            A = int(A/26)
        return s
```
* Python 3