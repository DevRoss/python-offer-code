#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-3-22


class Solution:
    def findMin(self, nums: list) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMin([3, 4, 5, 1, 2]))
    print(solution.findMin([4, 5, 6, 7, 0, 1, 2]))
