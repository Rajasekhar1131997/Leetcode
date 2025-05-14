// 349. Intersection of Two Arrays
// https://leetcode.com/problems/intersection-of-two-arrays/description/
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>(); // Create a HashSet to store unique elements from nums1
        for(int x : nums1){ // Iterate through nums1
            set1.add(x); // Add each element to the HashSet
        }
        Set<Integer> set2 = new HashSet<>(); // Create a HashSet to store unique elements from nums2
        for(int x: nums2){ // Iterate through nums2
            set2.add(x); // Add each element to the HashSet
        }
        set1.retainAll(set2); // Retain only the elements that are present in both sets
        int [] result = new int[set1.size()]; // Create an array to store the result
        int index = 0; // Initialize an index to keep track of the position in the result array
        for (int s: set1){ // Iterate through the elements in set1
            result[index] = s; // Assign the current element to the result array
            index++; // Increment the index
        }
        return result; // Return the result array containing the intersection of the two arrays
    }
}