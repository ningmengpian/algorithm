"""
question:
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses

example:
示例 1:
输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"

示例 2:
输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
"""


class Solution:

    def longest_valid_parentheses(self, s):
        """
        :param s: str
        :return: int
        """
        # 方法一：
        # 1.从左往右，统计左右括号数若左右括号数相等则计算当前有效括号子串长度，若左括号数小于右括号数，则将左右括号数置零
        # 2.从右往左，统计左右括号数若左右括号数相等则计算当前有效括号子串长度，若左括号数大于右括号数，则将左右括号数置零
        max_len = 0
        count = {'(': 0, ')': 0}
        for temp in s:
            count[temp] += 1
            if count['('] == count[')']:
                number = 2 * count['(']
                if number > max_len:
                    max_len = number
            if count['('] < count[')']:
                count['('] = 0
                count[')'] = 0
        count['('] = 0
        count[')'] = 0
        for temp in s[::-1]:
            count[temp] += 1
            if count['('] == count[')']:
                number = 2 * count['(']
                if number > max_len:
                    max_len = number
            if count['('] > count[')']:
                count['('] = 0
                count[')'] = 0
        return max_len

    def way_2(self, s):
        """
        :param s: str
        :return: int
        """
        # 方法二：动态规划
        # 1.记dp[i]为前i个字符的最长有效括号子串长度；
        # 2.若第i个字符为‘(’,则dp[i]等于0；
        # 3.若第i个字符为“”“”‘)’,则与前i-1个字符组成有效括号对的可能形式为："......()"或"..((....))",
        # dp[i]=dp[i-2]+2 或 d[i]=dp[i-1]+2+dp[i-dp[i-1]-2]
        if s == '':
            return 0
        dp = [0 for i in range(len(s))]
        for index in range(1, len(s)):
            if s[index] == ')':
                val_1 = 0
                val_2 = 0
                if s[index-1] == '(':
                    val_1 = dp[index-2] + 2
                elif index - dp[index-1] > 0 and s[index-dp[index-1]-1] == '(':
                    val_2 = dp[index - 1] + 2
                    if index - dp[index-1] - 2 > 0:
                        val_2 = val_2 + dp[index-dp[index-1]-2]
                dp[index] = val_1 if val_1 > val_2 else val_2
        max_len = max(dp)
        return max_len


if __name__ == "__main__":
    solution = Solution()
    s = ')())'
    # result = solution.longest_valid_parentheses(s)
    result = solution.way_2(s)
    print('最长有效括号长度为：%d' % result)
