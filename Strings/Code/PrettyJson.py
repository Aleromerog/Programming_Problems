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
            # Openning Bracket: Append last stirng, and append only the bracket with the corresponding indentation
            elif c == '{' or c == '[':
                if line != '':
                    line = '\t'*ind + line
                    lines.append(line)
                line =  '\t'*ind + c
                lines.append(line)
                ind += 1
                line = ''
            # Clossing Bracket: append the last String, and makes the string the clossing bracket only
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
