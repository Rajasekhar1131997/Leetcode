class Solution {
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        for(int i=n-1;i>=0;i--){ // Traversing the array from the last index
            if (digits[i] < 9){ // If the last digit is less than 9, we will just add 1 to it
                digits[i]++;
                return digits; // return the array
            }
            digits[i] = 0; // since the last digit is less than 9, we will set the carry value to 0.
        }
        // Dealing with the case when all the digits are 9 in the array.
        int [] newdigits = new int[n+1]; // Initializing a new array of size n+1.
        newdigits[0] = 1; // Setting the first index of the new array to 1.
        return newdigits; // returning the new array.
    }
}