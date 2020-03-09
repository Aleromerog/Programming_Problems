class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        for i in A:
            if i > 0 and rom_val[i] > rom_val[i-1]:
                num += rom_val[i] - 2 * rom_val[i-1]
            else:
                num += rom_val[i]

        return num
