# Numbers of length N and value less than K

Given a set of digits (A) in sorted order, find how many numbers of length B are possible whose value is less than number C.

> ### ***Note:*** All numbers can only have digits from the given set

**Examples:**

	Input:
	  0 1 5  
	  1  
	  2  
	Output:  
	  2 (0 and 1 are possible)  

	Input:
	  0 1 2 5  
	  2  
	  21  
	Output:
	  5 (10, 11, 12, 15, 20 are possible)

**Constraints:**

    1 <= B <= 9, 0 <= C <= 1e9 & 0 <= A[i] <= 9


## My solution:

```python
import itertools

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        ways = 0
        permu = [p for p in itertools.product(A, repeat=B)]
        for sub in permu:
            s = ""
            for i in sub:
                s+= str(i)
            num = int(s)
            if( len(str(num)) == B ):
                if num < C:
                    ways += 1
        return ways
            
```
* Ptrhon3.6