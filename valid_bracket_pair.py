"""
判断有效括号对
question：
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

example：
示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""


class Solution:

    def is_valid(self, s: str) -> bool:
        bracket_pair = {')': '(', '}': '{', ']': '['}
        left_bracket = ['(', '{', '[']
        right_bracket = [')', '}', ']']
        bracket_queue = []
        subscript = 0
        for character in s:
            if character in left_bracket:
                bracket_queue.append(character)
                subscript = subscript + 1
            elif character in right_bracket:
                if (subscript > 0) and (bracket_pair[character] ==
                                        bracket_queue[subscript - 1]):
                    bracket_queue.pop()
                    subscript = subscript - 1
                else:
                    return False
            else:
                return False
        if subscript != 0:
            return False
        return True


if __name__ == '__main__':
    s = '([)]'
    s_2 = '()[]{}'
    s_3 = ']'
    bracket_pair = Solution()
    result = bracket_pair.is_valid('')
    print(result)
