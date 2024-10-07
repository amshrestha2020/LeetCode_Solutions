Design a number container system that can do the following:

Insert or Replace a number at the given index in the system.
Return the smallest index for the given number in the system.
Implement the NumberContainers class:

NumberContainers() Initializes the number container system.
void change(int index, int number) Fills the container at index with the number. If there is already a number at that index, replace it.
int find(int number) Returns the smallest index for the given number, or -1 if there is no index that is filled by number in the system.
 

Example 1:

Input
["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
[[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]
Output
[null, -1, null, null, null, null, 1, null, 2]

Explanation
NumberContainers nc = new NumberContainers();
nc.find(10); // There is no index that is filled with number 10. Therefore, we return -1.
nc.change(2, 10); // Your container at index 2 will be filled with number 10.
nc.change(1, 10); // Your container at index 1 will be filled with number 10.
nc.change(3, 10); // Your container at index 3 will be filled with number 10.
nc.change(5, 10); // Your container at index 5 will be filled with number 10.
nc.find(10); // Number 10 is at the indices 1, 2, 3, and 5. Since the smallest index that is filled with 10 is 1, we return 1.
nc.change(1, 20); // Your container at index 1 will be filled with number 20. Note that index 1 was filled with 10 and then replaced with 20. 
nc.find(10); // Number 10 is at the indices 2, 3, and 5. The smallest index that is filled with 10 is 2. Therefore, we return 2.
 

Constraints:

1 <= index, number <= 109
At most 105 calls will be made in total to change and find.






from sortedcontainers import SortedList

class NumberContainers:
    def __init__(self):
        self.index_to_number = {}
        # This dictionary maps numbers to a SortedList of indices where that number is found.
        self.number_to_indices = {}


    def change(self, index: int, number: int) -> None:
        if index in self.index_to_number:
            previous_number = self.index_to_number[index]  # Get the previous number at this index
            
            # Remove the index from the previous number's SortedList
            if previous_number in self.number_to_indices:
                self.number_to_indices[previous_number].remove(index)
                # Clean up if the list is empty
                if not self.number_to_indices[previous_number]:
                    del self.number_to_indices[previous_number]

        # Update the index with the new number
        self.index_to_number[index] = number

        # Add the index to the SortedList for the new number
        if number not in self.number_to_indices:
            self.number_to_indices[number] = SortedList()
        self.number_to_indices[number].add(index)



    def find(self, number: int) -> int:
        if number in self.number_to_indices and self.number_to_indices[number]:
            return self.number_to_indices[number][0]  # Return the smallest index for number
        return -1  
    


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)