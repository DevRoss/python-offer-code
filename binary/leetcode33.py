#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-3-22


class Solution:
    def search(self, nums: list, target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) >> 1
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if nums[mid] == target:
                return mid
            if nums[l] > nums[mid]:
                if nums[mid] < target < nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] < target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
                    
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 3))
