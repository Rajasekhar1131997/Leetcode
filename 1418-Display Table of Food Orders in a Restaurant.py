# Leetcode Problem 1418: Display Table of Food Orders in a Restaurant
# https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/description/
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        # initialize an empty output list to store the result
        output = []
        # initialize an empty hashmap  to store frequency of each table number and food pair
        hash_map = {}
        # loop through each order in orders table
        for order in orders:
            # assign the customer, table and food item accordingly
            customer = order[0]
            table = order[1]
            fooditem = order[2]
            # store the frequency of each table and food items pair
            hash_map[(table, fooditem)] = hash_map.get((table, fooditem), 0) + 1
        
        # sort the rows based on table numbers and food items for columns
        sorted_orders = dict(sorted(hash_map.items(), key=lambda x: (int(x[0][0]), x[0][1])))
        
        # sort the food items
        foods = sorted(set(food for (_, food) in sorted_orders.keys()))
        # sort the tables
        tables = sorted(set(int(table) for (table, _) in sorted_orders.keys()))
        
        # add the header row to the output
        output = [['Table'] + foods]
        # loop through each table row
        for table in tables:
            # make each table as a row
            row = [str(table)]
            # we need to add food items also into the row
            for food in foods:
                # we get the count of each food item based on table row
                count = sorted_orders.get((str(table), food), 0)
                # append count of each food item to that row
                row.append(str(count))
            # finally append that row to output list
            output.append(row)
        # return the final output
        return output
    
print("Time Complexity: O(N log N)")
print("Space Complexity: O(N)")