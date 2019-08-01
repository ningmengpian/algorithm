"""
question:
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number

example:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution(object):
    def letter_combination(self, digits):
        """
        思想：排列组合
        :param digits: str
        :return: List[str]
        """
        if len(digits) == 0:
            return []
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        ans = []

        def combination(combination_str, digits):
            if len(digits) == 0:
                ans.append(combination_str)
            else:
                for letter_temp in phone[digits[0]]:
                    combination(combination_str+letter_temp, digits[1:])
        combination('', digits)
        return ans


if __name__ == "__main__":
    test_digits = ''

    solution = Solution()
    ans = solution.letter_combination(test_digits)
    print(ans)
