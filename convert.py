"""
question:
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);

example:
示例 1:
输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"

示例 2:
输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:
L     D     R
E   O E   I I
E C   I H   N
T     S     G

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-conversion
"""



class Solution(object):
    def convert(self, s, num_rows):
        """
        :param s: str
        :param num_rows: int
        :return: str
        """
        s_len = len(s)
        if s_len == 0 or num_rows == 1:
            return s
        z_len = 2 * num_rows - 2
        z_group_count = s_len // z_len + 1
        row_index = 1
        z_array = '#'

        while row_index <= num_rows:
            group_index = 1
            while group_index <= z_group_count:
                index = (group_index - 1) * z_len + row_index
                if index <= s_len:
                    print(s[index-1])
                    z_array = z_array + s[index-1]
                if row_index != 1 and row_index != num_rows:
                    next_index = index + z_len - 2 * (row_index - 1)
                    if next_index <= s_len:
                        print(s[next_index-1])
                        z_array = z_array + s[next_index-1]
                group_index += 1
            row_index += 1
        return z_array[1:len(z_array)]


if __name__ == "__main__":
    test_s = "PAYPALISHIRING"
    test_nums = 3

    solution = Solution()
    ans = solution.convert(test_s, test_nums)
    print(ans)
