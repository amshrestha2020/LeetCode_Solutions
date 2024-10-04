You are given an array of positive integers beans, where each integer represents the number of magic beans found in a particular magic bag.

Remove any number of beans (possibly none) from each bag such that the number of beans in each remaining non-empty bag (still containing at least one bean) is equal. Once a bean has been removed from a bag, you are not allowed to return it to any of the bags.

Return the minimum number of magic beans that you have to remove.

 

Example 1:

Input: beans = [4,1,6,5]
Output: 4
Explanation: 
- We remove 1 bean from the bag with only 1 bean.
  This results in the remaining bags: [4,0,6,5]
- Then we remove 2 beans from the bag with 6 beans.
  This results in the remaining bags: [4,0,4,5]
- Then we remove 1 bean from the bag with 5 beans.
  This results in the remaining bags: [4,0,4,4]
We removed a total of 1 + 2 + 1 = 4 beans to make the remaining non-empty bags have an equal number of beans.
There are no other solutions that remove 4 beans or fewer.
Example 2:

Input: beans = [2,10,3,2]
Output: 7
Explanation:
- We remove 2 beans from one of the bags with 2 beans.
  This results in the remaining bags: [0,10,3,2]
- Then we remove 2 beans from the other bag with 2 beans.
  This results in the remaining bags: [0,10,3,0]
- Then we remove 3 beans from the bag with 3 beans. 
  This results in the remaining bags: [0,10,0,0]
We removed a total of 2 + 2 + 3 = 7 beans to make the remaining non-empty bags have an equal number of beans.
There are no other solutions that removes 7 beans or fewer.
 

Constraints:

1 <= beans.length <= 105
1 <= beans[i] <= 105




class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        from typing import List


        beans.sort()  # Sort the array to make it easier to calculate removals
        total_beans = sum(beans)  # Sum of all beans
        min_removal = float('inf')  # Start with a large number for minimum removal
        
        # Iterate through the unique values in the sorted beans list
        for i in range(len(beans)):
            # Current target is beans[i]
            target = beans[i]
            # The number of remaining beans if we set the target for all bags
            # that have more than target beans
            # The number of bags that have more than target is (len(beans) - i)
            # Remaining beans after removal:
            remaining_beans = target * (len(beans) - i)
            # Calculate beans to be removed
            beans_to_remove = total_beans - remaining_beans
            
            # Update minimum removals
            min_removal = min(min_removal, beans_to_remove)
        
        return min_removal