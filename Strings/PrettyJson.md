# Pretty JSON

Given a string A representing json object. Return an array of string denoting json object with proper indentation.

Rules for proper indentation:

    Every inner brace should increase one indentation to the following lines.
    Every close brace should decrease one indentation to the same line and the following lines.
    The indents can be increased with an additional ‘\t’

Note:

    [] and {} are only acceptable braces in this case.

    Assume for this problem that space characters can be done away with.



Input Format

The only argument given is the integer array A.

Output Format

Return a list of strings, where each entry corresponds to a single line. The strings should not have "\n" character in them.

For Example

Input 1: ```A = "{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}"```

```
Output 1:
    {
        A:"B",
        C:
        {
            D:"E",
            F:
            {
                G:"H",
                I:"J"
            }
        }
    }
```

Input 2:
    A = ```["foo", {"bar":["baz",null,1.0,2]}]```
```
Output 2:
   [
        "foo",
        {
            "bar":
            [
                "baz",
                null,
                1.0,
                2
            ]
        }
    ]
```

### My Solution

```python
class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        ind = 0
        line = ''
        lines = []
        for c in A:
            # comma: add the comma to the string and append the string to the list. Means line Break
            if c == ',':
                line += c
                line = '\t'*ind + line
                lines.append(line)
                line = ''
            # Opening Bracket: Append last string, and append only the bracket with the corresponding indentation
            elif c == '{' or c == '[':
                if line != '':
                    line = '\t'*ind + line
                    lines.append(line)
                line =  '\t'*ind + c
                lines.append(line)
                ind += 1
                line = ''
            # Closing Bracket: append the last String, and makes the string the closing bracket only
            elif c == '}' or c == ']':
                if line != '':
                    line = '\t'*ind + line
                    lines.append(line)
                ind -= 1
                line = c
            else:
                line += c
        #Check if reminder exist
        if line != '':
            lines.append(line)
        return lines

```
* Python3.6