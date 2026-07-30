class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = nums[0]
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                maxx = max(maxx, sum)
                if sum < 0:
                    sum = 0
        return maxx