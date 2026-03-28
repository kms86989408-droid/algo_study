# https://leetcode.com/problems/house-robber-ii/?utm_source=chatgpt.com
class Solution:
    def rob(self, nums: List[int]) -> int:
        # def linear(arr):
        #     m = len(arr)
        #     if m == 1:
        #         return arr[0]
            
        #     dp = [0] * m
        #     dp[0] = arr[0]
        #     dp[1] = max(arr[0], arr[1])

        #     for i in range(2, arr):
        #         dp[i] = max(dp[i -1], dp[i - 2] + arr[i])
            
        #     return dp[-1]

        # n = len(nums)

        # if n ==1 :
        #     return nums[0]
        
        # return max(linear(nums[:-1], linear(nums[1:])))
# =========================================
        n = len(nums)
        
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        
        arr1 = nums[:-1]
        dp1 = [0] * len(arr1)
        dp1[0] = arr1[0]
        dp1[1] = max(arr1[0], arr1[1])

        for i in range(2, len(arr1)):
            dp1[i] = max(dp1[i -1], dp1[i-2] + arr1[i])

        arr2 = nums[1:]
        dp2 = [0]*len(arr2)
        dp2[0] = arr2[0]
        dp2[1] = max(arr2[0], arr2[1])

        for i in range(2, len(arr2)):
            dp2[i] = max(dp2[i -1], dp2[i-2] + arr2[i])
        
        return max(dp1[-1], dp2[-1])