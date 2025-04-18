def largest_sum_subarray(nums: list[int], k: int) -> int:
    """
    Find the largest sum of a contiguous subarray of size k.

    Args:
        nums (list[int]): List of integers.
        k (int): Size of the subarray.

    Returns:
        int: Largest sum of a contiguous subarray of size k.
    """
    if len(nums) < k or k <= 0:
        return 0

    max_sum = current_sum = sum(nums[:k])

    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum