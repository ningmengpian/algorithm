"""
question:
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
如果不存在最后一个单词，请返回 0 。
说明：一个单词是指由字母组成，但不包含任何空格的字符串。
链接：https://leetcode-cn.com/problems/length-of-last-word

example:
输入: "Hello World"
输出: 5
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :param s: str
        :return: int
        """
        # 注意首位空格符
        last_word_len = 0
        s = s.strip()
        s_len = len(s)
        for index in range(s_len-1, -1, -1):
            if s[index] == ' ':
                break
            last_word_len = last_word_len + 1
        return last_word_len

        # s = s[::-1].lstrip()
        # for temp in s:
        #     if temp == ' ':
        #         break
        #     last_word_len = last_word_len + 1
        # return last_word_len


if __name__ == "__main__":
    test_s = "Hello world "
    solution = Solution()
    last_word_len = solution.lengthOfLastWord(test_s)
    print(last_word_len)
