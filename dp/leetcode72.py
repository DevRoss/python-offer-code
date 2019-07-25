#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 2019/7/25


"""
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2:

输入: word1 = "intention", word2 = "execution"
输出: 5
解释:
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = self._dp(word1, word2)
        # for _ in dp:
        #     print(_)
        return dp[-1][-1]

    def _dp(self, word1: str, word2: str) -> list:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for j in range(len(word2) + 1):
            dp[0][j] = j

        i = 1
        while i <= len(word1):
            j = 1
            while j <= len(word2):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 其中，dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作。
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                j += 1
            i += 1
        return dp


if __name__ == '__main__':
    solution = Solution()
    # solution.minDistance('ABCBEBC', 'BBCD')
    # solution.minDistance('BBCD', 'ABCBEBC')
    print(solution.minDistance('intention', 'execution'))
