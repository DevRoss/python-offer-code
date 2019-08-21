#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 2019/8/21


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        if len(nums) == 0:
            return 0
        dp[0] = 1
        for i in range(1, len(nums)):
            maxval = 0
            for j in range(0, i):
                if nums[j] < nums[i]:
                    maxval = max(maxval, dp[j])
            dp[i] = maxval + 1
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
