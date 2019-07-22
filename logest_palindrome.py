"""
question:
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

example:
示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
"""


class Solution(object):
    def now_longest_palindrome(self, s, left, right):
        s_len = len(s)
        r_index = right
        l_index = left
        while l_index >= 0 and r_index < s_len and s[l_index] == s[r_index]:
            l_index = l_index - 1
            r_index = r_index + 1
        return r_index - l_index - 1

    def longest_palindrome(self, s):
        """
        :param s: str
        :return: str
        """
        # 使用中心扩展法则实现，分两种情况“”“"偶数回文" && ”"奇数回文",共2n-1种可能
        index = 0
        start = 0
        end = 0
        s_len = len(s)

        while index < s_len:
            # 求最长偶数回文
            enven_palindrome_len = self.now_longest_palindrome(s, index, index+1)
            # 求最长奇数回文
            odd_palindrome_len = self.now_longest_palindrome(s, index, index)
            max_len = max(enven_palindrome_len, odd_palindrome_len)
            if max_len > (end - start):
                start = index - (max_len-1) // 2
                end = index + max_len // 2
            index = index + 1
        return s[start:end+1]


if __name__ == "__main__":
    test_s = ''

    solution = Solution()
    ans_palindrome = solution.longest_palindrome(test_s)
    print(ans_palindrome)
