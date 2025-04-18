class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        current_sum = sum(nums[0:k])
        max_avg = current_sum/float(k)
        for right in range(k,len(nums)): 
            current_sum += nums[right]-nums[right-k]
            current_avg = current_sum/float(k)
            max_avg = max(max_avg,current_avg)
        return float(max_avg)


# Example usage 
if __name__ == "__main__":
    nums = [1,12,-5,-6,50,3]
    k = 4
    solution = Solution()
    result = solution.findMaxAverage(nums, k)
    print(result)  # Output: 12.75