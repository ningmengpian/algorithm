"""
question:
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

example:
示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
"""


class Solution:
    def reverse(self, x: int) -> int:
        symbol = 1
        if x < 0:
            x = abs(x)
            symbol = -1
        new_value = x % 10
        now_model = x // 10
        while now_model:
            now_remainder = now_model % 10
            new_value = new_value * 10 + now_remainder
            now_model = now_model // 10
        result = new_value * symbol
        if result < -pow(2, 31) or result > (pow(2, 31) - 1):
            return 0
        return result


if __name__ == '__main__':
    reverse = Solution()
    result = reverse.reverse(-123)
    print(result)
