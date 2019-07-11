"""
question:
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
链接：https://leetcode-cn.com/problems/plus-one

example:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

输入：[999]
输出：[1000]
解释：输入数组表示数字 999。
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :param digits: List[int]
        :return: List[int]
        """
        # 注意最高位满十需自行添加数组空间并置一
        digits_len = len(digits)
        carry_flag = 0
        for index in range(digits_len-1, -1, -1):
            now_digits_val = digits[index] + 1
            if now_digits_val == 10:
                digits[index] = 0
                carry_flag = 1
            else:
                digits[index] = now_digits_val
                carry_flag = 0
            if carry_flag == 0:
                break
        if carry_flag == 1 and index == 0:
            return [1] + digits
        return digits


if __name__ == "__main__":
    test_digits = [9]
    solution = Solution()
    result = solution.plusOne(test_digits)
    print(result)
