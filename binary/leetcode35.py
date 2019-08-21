#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 2019/8/21


class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] < target:
                l = mid + 1
            elif target == nums[mid]:
                return mid
            else:
                r = mid - 1
        return l


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 5))
    print(s.searchInsert([1, 3, 5, 6], 2))
    print(s.searchInsert([1, 3], 2))
