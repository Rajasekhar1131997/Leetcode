// 119. Pascal's Triangle II
// https://leetcode.com/problems/pascals-triangle-ii/description/

class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> row = new ArrayList<>(); // Create a list to store the row
        for(int i=0;i<rowIndex+1;++i){ // Loop through the row index
            row.add(1); // Add 1 to the list for each index
        }
        for (int i=1; i<rowIndex;++i){ // Loop through the row index
            for (int j=i;j>0;--j){ //
                row.set(j, row.get(j)+ row.get(j-1)); // Update the value at index j
            }
        }
        return row;
    }
}