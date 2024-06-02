Given an array arr that represents a permutation of numbers from 1 to n.

You have a binary string of size n that initially has all its bits set to zero. At each step i (assuming both the binary string and arr are 1-indexed) from 1 to n, the bit at position arr[i] is set to 1.

You are also given an integer m. Find the latest step at which there exists a group of ones of length m. A group of ones is a contiguous substring of 1's such that it cannot be extended in either direction.

Return the latest step at which there exists a group of ones of length exactly m. If no such group exists, return -1.

 

Example 1:

Input: arr = [3,5,1,2,4], m = 1
Output: 4
Explanation: 
Step 1: "00100", groups: ["1"]
Step 2: "00101", groups: ["1", "1"]
Step 3: "10101", groups: ["1", "1", "1"]
Step 4: "11101", groups: ["111", "1"]
Step 5: "11111", groups: ["11111"]
The latest step at which there exists a group of size 1 is step 4.
Example 2:

Input: arr = [3,1,5,4,2], m = 2
Output: -1
Explanation: 
Step 1: "00100", groups: ["1"]
Step 2: "10100", groups: ["1", "1"]
Step 3: "10101", groups: ["1", "1", "1"]
Step 4: "10111", groups: ["1", "111"]
Step 5: "11111", groups: ["11111"]
No group of size 2 exists during any step.
 

Constraints:

n == arr.length
1 <= m <= n <= 105
1 <= arr[i] <= n
All integers in arr are distinct.





class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m > n:
            return -1
        
        # lengths[i] keeps the length of the segment that position i is part of
        lengths = [0] * (n + 2)
        # count[k] keeps the number of segments of length k
        count = [0] * (n + 1)
        
        result = -1
        
        for step, pos in enumerate(arr, 1):
            left = lengths[pos - 1]
            right = lengths[pos + 1]
            current_length = left + right + 1
            
            lengths[pos - left] = current_length
            lengths[pos + right] = current_length
            
            count[left] -= 1
            count[right] -= 1
            count[current_length] += 1
            
            if count[m] > 0:
                result = step
        
        return result
