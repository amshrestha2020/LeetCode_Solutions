You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.

 

Example 1:

Input: cards = [3,4,2,3,4,7]
Output: 4
Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.
Example 2:

Input: cards = [1,0,5,3]
Output: -1
Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards.
 

Constraints:

1 <= cards.length <= 105
0 <= cards[i] <= 106





class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        from typing import List


        last_seen = {}
        min_length = float('inf')
        
        for i, card in enumerate(cards):
            if card in last_seen:
                # Calculate the length of the segment that includes the matching pair
                length = i - last_seen[card] + 1
                min_length = min(min_length, length)
            
            # Update the last seen index of the current card
            last_seen[card] = i
        
        # If min_length was updated, return it; otherwise return -1
        return min_length if min_length != float('inf') else -1
