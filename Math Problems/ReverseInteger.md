# Reverse integer



Reverse digits of an integer.

**Example1:**

x = 123,

return 321

**Example2:**

x = -123,

return -321

Return 0 if the result overflows and does not fit in a 32 bit signed integer

## **My solution:**

```python
class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        if A.bit_length() >= 31:
            return 0
        n = [d for d in str(A)]
        i1 = 0
        i2 = len(n)-1
        if n[0] == '-':
            i1 = 1
        while (i1 < i2):
            temp = n[i1]
            n[i1] = n[i2]
            n[i2] = temp
            i1+=1
            i2-=1
        return int("".join(n))
```

* Python 3