"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


# what if you cant use additional space?
"""
def twoSum (nums, target):
    """
    time complexity is O(n)
    space complexity is O(n)
    """
    pair_idx = {}

    for i, num in enumerate(nums):
        if target - num in pair_idx:
            return [i, pair_idx[target - num]]
        pair_idx[num] = i 

def twoSumNoAdditonalSpace(nums, target): 
    """
    time complexity is O(nlogn)
    space complexity is O(1)
    """
    nums.sort()
    left,right = 0,len(nums)-1
    while left < right:
        if nums[left] + nums[right] == target:
            return [left, right]
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
    return None 