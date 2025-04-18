class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # TODO Find the total number of subarray that contains elements who's sum is <=k 
        if k <= 1:
            return 0

        ans = left = 0
        curr = 1

        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                curr //= nums[left]
                left += 1
                
            ans += right - left + 1

        return ans

if __name__ == "__main__":
    solution = Solution()
    nums = [10,5,2,6]
    print(solution.numSubarrayProductLessThanK(nums,100)) 