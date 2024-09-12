You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

 

Example 1:

Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: arr = [2,2,2]
Output: 0
Explanation: There is no mountain.
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
 

Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?





class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # Initialize the maximum length of the mountain
        max_length = 0
        # The length of the array
        n = len(arr)
        
        # Iterate through the array, skipping the first and last elements
        # because a peak cannot exist at the boundaries
        i = 1
        while i < n - 1:
            # Check if the current element is a peak
            if arr[i - 1] < arr[i] > arr[i + 1]:
                # Expand to the left of the peak
                left = i - 1
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
                
                # Expand to the right of the peak
                right = i + 1
                while right < n - 1 and arr[right + 1] < arr[right]:
                    right += 1
                
                # Calculate the length of the mountain
                current_length = right - left + 1
                # Update the maximum length if the current mountain is longer
                max_length = max(max_length, current_length)
                # Move to the next potential peak
                i = right
            else:
                # If not a peak, move to the next element
                i += 1
        
        # Return the maximum length of the mountain found
        return max_length
