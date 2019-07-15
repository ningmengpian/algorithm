"""
question:
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs

example:
示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
"""


class Solution(object):
    def climb_stairs(self, i, n):
        # 方法一：暴力求解
        if i > n:
            return 0
        if i == n:
            return 1
        return self.climb_stairs(i+1, n) + self.climb_stairs(i+2, n)

    def optimize_climb_stairs(self, i, n, memo):
        # 方法二：对方法一进行优化，存储递归值
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i]:
            return memo[i]
        memo[i] = self.optimize_climb_stairs(i+1, n, memo) + \
                  self.optimize_climb_stairs(i+2, n, memo)
        print(memo)
        return memo[i]

    def dynamic_climb_stairs(self, n):
        # 方法三：动态规划
        if n == 1:
            return 1

        dy = [0 for i in range(n+1)]
        dy[1] = 1
        dy[2] = 2
        index = 3
        while index <= n:
            dy[index] = dy[index-1] + dy[index-2]
            index = index + 1
        return dy[n]

    def fib(self, n):
        # 方法四：斐波拉契
        if n == 1:
            return 1

        first = 1
        second = 2
        index = 3
        while index <= n:
            third = first + second
            first = second
            second = third
            index = index + 1
        return second


    def climbStairs(self, n):
        """
        :param n: int
        :return: int
        """
        # 方法一：
        # return self.climb_stairs(0, n)

        # 方法二：
        # memo = [0 for i in range(n)]
        # return self.optimize_climb_stairs(0, n, memo)

        # 方法三：
        # return self.dynamic_climb_stairs(n)

        # 方法四：
        return self.fib(n)


if __name__ == "__main__":
    test_n = 5
    solution = Solution()
    way_number = solution.climbStairs(test_n)
    print(way_number)
