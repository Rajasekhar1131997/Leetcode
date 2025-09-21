# Leetcode Problem 2469: Convert the Temperature
# https://leetcode.com/problems/convert-the-temperature/description/
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        # by adding 273.15 to celsius gives the kelvin
        kelvin = celsius + 273.15
        # by using the below formula, we get the fahrenheit
        fahrenheit = celsius * 1.80 + 32.00
        # return the results in a list
        return [kelvin, fahrenheit]

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")