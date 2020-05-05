class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        rom = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        i = 0
        romNum = ''
        while A > 0:
            for j in range(A // val[i]):
                A -= val[i]
                romNum += rom[i]
            i += 1

        return romNum
