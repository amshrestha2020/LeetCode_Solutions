You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the same difficulty level.

Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.

 

Example 1:

Input: tasks = [2,2,3,3,2,4,4,4,4,4]
Output: 4
Explanation: To complete all the tasks, a possible plan is:
- In the first round, you complete 3 tasks of difficulty level 2. 
- In the second round, you complete 2 tasks of difficulty level 3. 
- In the third round, you complete 3 tasks of difficulty level 4. 
- In the fourth round, you complete 2 tasks of difficulty level 4.  
It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.
Example 2:

Input: tasks = [2,3,3]
Output: -1
Explanation: There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same difficulty level. Hence, you cannot complete all the tasks, and the answer is -1.
 

Constraints:

1 <= tasks.length <= 105
1 <= tasks[i] <= 109
 

Note: This question is the same as 2870: Minimum Number of Operations to Make Array Empty.




class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        from collections import Counter
        
        task_count = Counter(tasks)
        
        # Step 2: Initialize total rounds
        total_rounds = 0
        
        # Step 3: Iterate through the frequency dictionary
        for count in task_count.values():
            # If there's only 1 task of this difficulty, it's impossible
            if count == 1:
                return -1
            # If the count is divisible by 3, we can complete in count // 3 rounds
            elif count % 3 == 0:
                total_rounds += count // 3
            # If the count is not divisible by 3, use (count // 3) + 1 rounds
            else:
                total_rounds += count // 3 + 1
        
        return total_rounds