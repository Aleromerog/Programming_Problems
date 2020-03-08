# Add One To Number


Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

**Example:**

If the vector has ``[1, 2, 3]``

the returned vector should be ``[1, 2, 4]``

as `123 + 1 = 124`.

---

### **Solution**
```python
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        # Will iterate from the last element to the first until is not a 9
        # If the element is not 9 then just add one.
        for i in range(len(A)):
            if(A[len(A)-1 -i] != 9):
                A[len(A)-1 -i] += 1
                break
            A[len(A)-1 -i] = 0
            # If first element reached then just add one at the beginning
            if i == len(A)-1:
                A.insert(0, 1)
        # Removing unnecessary 0's at the left of the number
        while A[0] == 0:
            A.pop(0)
        return A

```
