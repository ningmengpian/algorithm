"""
question:
给定两个二进制字符串，返回他们的和（用二进制表示）。
输入为非空字符串且只包含数字 1 和 0。

example:
输入: a = "11", b = "1"
输出: "100"

"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :param a: str
        :param b: str
        :return: str
        """
        a_len = len(a)
        b_len = len(b)
        if a_len < b_len:
            a = '0'*(b_len - a_len) + a
            deal_len = b_len
        else:
            b = '0'*(a_len - b_len) + b
            deal_len = a_len
        ans = ''
        carry_flag = 0
        index = deal_len - 1
        while index >= 0:
            if a[index] == b[index]:
                if carry_flag == 1:
                    ans = '1' + ans
                else:
                    ans = '0' + ans
                if a[index] == '1':
                    carry_flag = 1
                else:
                    carry_flag = 0
            else:
                if carry_flag == 1:
                    ans = '0' + ans
                else:
                    ans = '1' + ans
            index = index - 1
        if carry_flag == 1:
            ans = '1' + ans
        return ans


if __name__ == "__main__":
    test_a = ''
    test_b = ''
    solution = Solution()
    result = solution.addBinary(test_a, test_b)
    print(result)
