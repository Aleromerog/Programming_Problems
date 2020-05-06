# Grid Unique Paths



A robot is located at the top-left corner of an **A x B grid** (marked ‘Start’ in the diagram below).

![](https://i.imgur.com/3eaivQ5.png)

Path Sum: Example 1

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).

How many possible unique paths are there?

Note: A and B will be such that the resulting answer fits in a 32 bit signed integer.

**Example :**

    Input : A = 2, B = 2
    Output : 2

    2 possible routes : (0, 0) -> (0, 1) -> (1, 1) 
                OR  : (0, 0) -> (1, 0) -> (1, 1)



### **My Solution**

```python
import math
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        n = A-1 + B-1
        r = B-1
        return int(math.factorial(n) / (math.factorial(n-r) * math.factorial(r)))
```

* Python 3.6