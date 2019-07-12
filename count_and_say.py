"""
question:
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
注意：整数顺序将表示为一个字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-and-say

example:
示例 1:
输入: 1
输出: "1"

示例 2:
输入: 4
输出: "1211"

"""


class Solution(object):
    def countAndSay(self, n):
        """
        :param n: int
        :return: str
        """
        if n == 1:
            return '1'
        before_say = self.countAndSay(n-1) + '0'
        count = 0
        now_say = ''
        now_number = before_say[0]
        for number in before_say:
            if number == now_number:
                count = count + 1
            else:
                now_say = now_say + str(count) + now_number
                now_number = number
                count = 1
        return now_say


if __name__ == "__main__":
    test_n = 5
    solution = Solution()
    count_say = solution.countAndSay(test_n)
    print(count_say)
