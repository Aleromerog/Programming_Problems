# Square Root of Integer

Given an integar A.

Compute and return the square root of A.

If A is not a perfect square, return floor(sqrt(A)).

**DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY**



**Input Format**

    The first and only argument given is the integer A.

**Output Format**

    Return floor(sqrt(A))

**Constraints**

    1 <= A <= 10^9

**For Example**

    Input 1:
        A = 11
    Output 1:
        3

    Input 2:
        A = 9
    Output 2:
        3


## **My solution:**

```python
class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        start = 1
        end = A
        mid = (end + start) / 2
        while start <= end:
            if mid**2 == A:
                return mid
            elif mid**2 > A:
                end = mid-1
            else:
                start = mid+1
            
        return start
```

* Python 3