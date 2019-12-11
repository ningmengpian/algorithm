"""
question:
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数 dividend 除以除数 divisor 得到的商。
说明:
被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divide-two-integers

example:
示例 1:
输入: dividend = 10, divisor = 3
输出: 3

示例 2:
输入: dividend = 7, divisor = -3
输出: -2
"""

import sys


class Soulution():

    def divide(self, dividend, divisor):
        """
        :param dividend: int
        :param divisor: int
        :return: int

        解题思路：
            1.商的值：被除数减除数的次数（被除数大于除数）
            2.商的符号：利用数的补码进行转换，商为负数时，将统计次数取反加1
            3.存储问题：由于正整数的个数比负整数的个数少1，因此计算时将除数与被除数均转化为负数进行计算
        """
        max_val = 2**31 - 1
        min_val = -2**31
        ans = -1
        sign = 1
        if dividend > 0:
            dividend = ~dividend + 1
            sign = ~sign + 1
        if divisor > 0:
            divisor = ~divisor + 1
            sign = ~sign + 1

        origin_dividend = dividend
        origin_divisor = divisor
        if divisor < dividend:
            return 0

        dividend -= divisor
        while divisor >= dividend:
            ans = ans + ans
            divisor = divisor + divisor
            dividend -= divisor

        result = ans + ~(self.divide(origin_dividend - divisor,
                                     origin_divisor)) + 1
        if result == min_val:
            if sign > 0:
                return max_val
            else:
                return min_val
        else:
            if sign > 0:
                return ~result + 1
            else:
                return result


if __name__ == "__main__":
    solution = Soulution()
    result = solution.divide(20, 3)
    print("商为：%d" %result)
