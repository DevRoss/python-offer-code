#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-3-29

"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。
例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = list()
        length = len(nums)
        nums.sort()
        for i in range(length):
            if i == 0 or nums[i] > nums[i - 1]:
                l = i + 1
                r = length - 1
                target = -nums[i]
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        ret.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
        return ret


if __name__ == '__main__':
    pass
