"""
question:
实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx

example:
输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :param x: int
        :return: int
        """

        left = 0
        right = x

        while left < right:
            mid = left + (right - left + 1) // 2
            square = mid * mid

            if square > x:
                right = mid - 1
            else:
                left = mid
        return left


if __name__ == "__main__":
    test_x = 2147395599
    solution = Solution()
    my_sqrt = solution.mySqrt(test_x)
    print(my_sqrt)
