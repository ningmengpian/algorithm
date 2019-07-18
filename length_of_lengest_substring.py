"""
question:
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

example:
示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
"""


class Solution(object):
    def lengthOfLengestSubstring(self, s):
        """
        :param s: str
        :return: int
        """
        # 方法一：暴力求解
        s_len = len(s)
        if s == ' ' or s_len == 1:
            return 1
        s_index = 0
        max_length = 0
        while s_index < s_len-1:
            substring_index = s_index + 1
            substring = s[s_index:substring_index]
            index = s_index + 1
            while index < s_len:
                if s[index] not in substring:
                    substring_index = substring_index + 1
                    substring = s[s_index:substring_index]
                else:
                    break
                index = index + 1
            if max_length < len(substring):
                max_length = len(substring)
            s_index = s_index + 1
            if max_length >= s_len-s_index:
                break
        return max_length

    def lengthOfLengestSubstring_2(self, s):
        # 方法二：滑动窗口，将自字符串放置于滑动窗口中，若下一个字符在窗口中则窗口左边界右移，否则窗口右边界右移
        s_i = 0
        s_j = 0
        s_len = len(s)
        max_length = 0
        substring = s[s_i:s_j]
        while s_i < s_len and s_j < s_len:
            if s[s_j] not in substring:
                substring = substring + s[s_j]
                max_length = max(max_length, len(substring))
                s_j = s_j + 1
            else:
                s_i = s_i + 1
                substring = substring[s_i:s_j]
        return max_length


if __name__ == "__main__":
    # 注意测试字符串为空格的情况
    test_str = 'c'

    solution = Solution()
    # 方法一：
    # max_length = solution.lengthOfLengestSubstring(test_str)

    # 方法二：
    max_length = solution.lengthOfLengestSubstring_2(test_str)
    print(max_length)
