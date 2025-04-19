"""
Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. This problem is similar to Two Sum. (In Two Sum, the input is not sorted).

For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.
"""

def two_sum_sorted_unique(nums, target):
    # the key here is sorted array and unique integers
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return False
# Example usage
nums = [1, 2, 4, 6, 8, 9, 14, 15]
target = 13

result = two_sum_sorted_unique(nums, target)
print(f"Does the array contain a pair that sums to {target}? {result}")
