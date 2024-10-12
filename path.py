class Solution:
    def pairWithMaxSum(self, arr):
        # If the array has less than 2 elements, return -1
        if len(arr) < 2:
            return -1
        
        # Initialize the maximum sum to a very small value
        max_sum = -1
        
        # Traverse through adjacent elements in the array
        for i in range(len(arr) - 1):
            # Get the sum of two adjacent elements
            current_sum = arr[i] + arr[i + 1]
            
            # Update max_sum if the current sum is larger
            max_sum = max(max_sum, current_sum)
        
        return max_sum
