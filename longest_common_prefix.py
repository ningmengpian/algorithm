"""
最长公共前缀
question:
编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 ""

说明:所有输入只包含小写字母 a-z 。

example：
示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
"""


class Solution:

    def longest_common_prefix(self, strs) -> str:
        if strs:
            first_str = strs[0]
            shortest_str = len(first_str)
            # 查找最短字符串
            for temp in strs:
                temp_len = len(temp)
                if temp_len < shortest_str:
                    shortest_str = temp_len

            index = 0
            while index < shortest_str:
                match_flag = 0
                for temp in strs[1:]:
                    if temp[index] != first_str[index]:
                        match_flag = 1
                if match_flag:
                    break
                index = index + 1
            return first_str[0:index]
        return ''


if __name__ == '__main__':
    # 测试用例
    strs = ["flower", "flow", "flight"]
    strs_2 = ["dog", "racecar", "car"]
    strs_3 = []

    prefix = Solution()
    result = prefix.longest_common_prefix(strs)
    print(result)
