"""
question:
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

example:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        动态规划：前段序列之和的最大值若小于零则对最终结果无增益，应舍去后从当前元素开始重新求解
        :param nums: List[int]
        :return: int
        """
        ans = nums[0]
        sum = 0
        for now_index in range(0, len(nums)):
            if sum > 0:
                sum = sum + nums[now_index]
            else:
                sum = nums[now_index]
            ans = max(ans, sum)
        return ans


if __name__ == "__main__":
    # 测试数据不能为空
    test_data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution = Solution()
    ans = solution.maxSubArray(test_data)
    print(ans)
