
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [-4, -1, 0, 3, 10]
    print(solution.sortedSquares(nums))  # Output: [0, 1, 9, 16, 100]