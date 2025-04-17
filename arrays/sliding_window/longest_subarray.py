"""
Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k. 
"""

def find_length(nums : list, k: int) -> int:
    left=right=0
    max_length=0
    current_sum=0
    

    while left <= right:
        current_sum += nums[right]
        if current_sum <= k: 
            current_length = right - left + 1
            max_length = max(max_length, current_length)
            right += 1
        else:
            current_sum -= nums[left]
            left += 1
    return max_length

# Example usage
nums = [1, 2, 3,1,1,1, 1,2,1,1,4, 5,6]
k = 8
result = find_length(nums, k)
print(f"The length of the longest subarray with sum less than or equal to {k} is: {result}")