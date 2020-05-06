# Rearrange Array

Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

**Example:**

    Input : [1, 0]
    Return : [0, 1]


>Lets say N = size of the array. Then, following holds true :
> 1. All elements in the array are in the range [0, N-1]
> 2. N * N does not overflow for a signed integer


## **My solution:**

```python
class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        put(0, A, A[0])
    def put(ind, A, val):
        newInd = A.index(ind)
        temp = A[newInd]
        A[newInd] = val
        put(newInd, A, temp)
```

* Python 3.6 