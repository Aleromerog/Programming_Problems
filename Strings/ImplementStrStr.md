# Implement strStr().

    strstr - locate a substring ( needle ) in a    string ( haystack ).

Try not to use standard library string functions for this question.

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

### My Solution

```python
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        # Check if String B exists in A, and return the index where it begins
        if B in A:
            return A.index(B)
        else:
            return -1

```
* Python3.6
