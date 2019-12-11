"""
question:
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words

example:
示例 1：
输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。

示例 2：
输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]
"""


class Solution:

    def find_sub_string(self, s, words):
        """
        :param s: str
        :param words: list[str]
        :return: list[int]

        思想：
        1.对s滑动截取长度为words字符总长的子串sub_str;
        2.并将子串按words元素长度划分为字符串列表sub;
        3.比较sub于words元素是否相同,若相同记下sub_str在s中的起始下标，否则对s滑动截取下一个子串
        """
        words_len = len(words)
        if s is not None and words_len > 0:
            element = len(words[0])
            str_len = words_len * element
            s_len = len(s)
        else:
            return []

        if str_len > s_len:
            return []
        result = []
        for index in range(0, s_len-str_len+1):
            sub_str = s[index:index+str_len]
            sub = []
            for sub_index in range(0, str_len, element):
                sub.append(sub_str[sub_index:sub_index+element])
            for temp in words:
                if temp in sub:
                    sub.remove(temp)
                else:
                    break
            if len(sub) == 0:
                result.append(index)
        return result


if __name__ == "__main__":
    solute = Solution()
    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "good"]
    result = solute.find_sub_string(s, words)
    print(result)
