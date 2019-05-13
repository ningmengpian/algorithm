"""
question:
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

example:
示例1：
输入：121
输出：True

示例2：
输入：-121
输出：False
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # -> 符号解释：常跟在函数名后，为函数添加元数据，描述函数的返回值类型
        if x < 0:
            return False
        # 方法一：将整数x转换为字符串后再进行判断
        # str_x = str(x)
        # x_last_index = len(str_x) - 1
        # middle_index = (x_last_index + 2) // 2
        # for index in range(middle_index):
        #     if str_x[index] != str_x[x_last_index - index]:
        #         return False
        # return True

        # 方法二：不将整数转换为字符串，使用求余的方式反向计算该整数的”"回文"数
        new_value = x % 10
        now_model = x // 10
        while now_model:
            now_remainder = now_model % 10
            new_value = new_value * 10 + now_remainder
            now_model = now_model // 10
        if x == new_value:
            return True
        return False


if __name__ == '__main__':
    palindrome = Solution()
    result = palindrome.isPalindrome(2121)
    print(result)
