# Leetcode Problem 2806: Account Balance After Rounded Purchase
# https://leetcode.com/problems/account-balance-after-rounded-purchase/description/
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # first divide the purchase amount with 10
        rounded_amount = (purchaseAmount + 5) // 10
        # second, the rounded amount should be multiplied with 10, to round up to nearest multiple of 10 using round function
        rounded_amount = rounded_amount * 10
        # finally, we need to return the total amount present in the account
        return 100-rounded_amount

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")