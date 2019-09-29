"""
question：实现字符串正则匹配
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/regular-expression-matching

eg.
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
"""

def is_match(s: str, p: str) -> bool:
    """
    使用回溯法求解
    1、规律字符中不包含星号。采用从左到右依次匹配的方法确定是否可匹配；
    2、规律字符中包含“星号。星号应出现在首字符之后，星号之前的字符匹配情况可分为四种，
    a.匹配0次；b.匹配1次；c.匹配n次(至少一次)；d.不匹配；匹配0次时忽略规律字符中的当前星号即可
    """
    if not p:
        return not s

    first_match = bool(s) and p[0] in {s[0], '.'}

    if len(p) >= 2 and p[1] == '*':
        return is_match(s, p[2:]) or first_match and is_match(s[1:], p)
    else:
        return first_match and is_match(s[1:], p[1:])


if __name__ == "__main__":
    test_s = 'mississippi'
    test_p = 'mis*is*p*.'
    result = is_match(test_s, test_p)
    print(result)
