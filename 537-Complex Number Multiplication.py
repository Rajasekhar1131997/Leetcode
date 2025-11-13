# Leetcode Problem 537: Complex Number Multiplication
# https://leetcode.com/problems/complex-number-multiplication/description/
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # split the given num1 and num2 string using split method
        real1, imag1 = num1.split('+')
        real2, imag2 = num2.split('+')
        # convert them from string to integers
        real1 = int(real1)
        real2 = int(real2)
        imag1 = int(imag1[:-1])
        imag2 = int(imag2[:-1])

        # computing the real and imaginary numbers
        real = (real1 * real2) - (imag1 * imag2)
        imag = (real1 * imag2) + (real2 * imag1)
        # return their multiplication in the format of "real+imaginaryi"
        return str(real) + '+' + str(imag) + 'i'

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")