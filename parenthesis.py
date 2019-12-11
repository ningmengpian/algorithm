"""
question：
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

example：
例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""

class Solution:
    def generate_parenthesis(self, n):
        """
        :param n: int
        :return: List(str)
        """
        """
        动态规划：
        求解第n组括号的组合情况时，将第N个括号拿出来，其左括号在所有情况中都作为第一个字符存在，
        那么剩下的n-1组括号要么在第N个括号的里面，要么在第N个括号的外面（右侧），此时有：
        "(" + 【i=p时所有括号的排列组合】 + ")" + 【i=q时所有括号的排列组合】，p+q=n-1。
        当p从0取到n-1，q从n-1取到0，就完成了所有情况的遍历
        """
        if n == 0:
            return []
        total_l = []
        # 0组括号记为None
        total_l.append([None])
        # 1组括号为“"()"
        total_l.append(['()'])
        # 计算第i组括号的组合形式
        for index_n in range(2, n + 1):
            # 求第n-1组的第j种组合情况
            temp = []
            for j in range(index_n):
                mider = total_l[j]    # p从1到i-1
                right = total_l[index_n-j-1]    # q从i-1到1
                for k1 in mider:
                    for k2 in right:
                        if k1 == None:
                            k1 = ''
                        if k2 == None:
                            k2 = ''
                        el = '(' + k1 + ')' + k2
                        temp.append(el)
            total_l.append(temp)
        return total_l


if __name__ == "__main__":
    solute = Solution()
    result = solute.generate_parenthesis(5)
    for temp in result[5]:
        print(temp)
