# Count and say

The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...

1 is read off as one 1 or 11.
11 is read off as two 1s or 21.

21 is read off as one 2, then one 1 or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

**Example:**

if n = 2,
the sequence is 11.

---

### My Solution

```python
class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        s = '1'
        for i in range(1,A):
            index = 0
            val = ''
            newS = ''
            # Add to the NewString the counted numbers recieved in count function
            while index < len(s):
                counter = self.count(s, index)
                val = s[index]
                index += counter
                newS += str(counter) + val
            s = newS

        return s

    #Count how many consecutive numbers exist in the given String
    def count(self,s, index):
        val = s[index]
        counter = 0
        while s[index] == val:
            counter +=1
            index +=1
            if index > len(s)-1:
                break
        return counter

```
* Python3.6