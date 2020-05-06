# Reverse String

Given a string A.

Return the string A after reversing the string word by word.

**NOTE:**

1. A sequence of non-space characters constitutes a word.

2. Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.

3. If there are multiple spaces between words, reduce them to a single space in the reversed string.



Input Format

The only argument given is string A.

Output Format

Return the string A after reversing the string word by word.

For Example

**Input 1:**

    A = "the sky is blue"

**Output 1:**

    "blue is sky the"

**Input 2:**

    A = "this is ib"

**Output 2:**

    "ib is this"

---

### My Solution

```python
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        #split the words into a list
        words = A.split()
        rev = []
        #Insert every word in order at the beginning of the new list
        for word in words:
            rev.insert(0, word)

        return ' '.join(rev)

```
* Python3.6