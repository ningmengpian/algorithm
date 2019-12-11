"""
question:
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须原地修改，只允许使用额外常数空间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation

example:
以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution:

    def next_permutation(self, nums):
        """
        :param nums: list[int]
        :return: None Do not return anything, modify nums in-place instead.
        思想：
        1.从后往前找最长降序序列，获取该最长序列的前一个数的位置i；
        2.从后往前遍历，将位置i的值与第一个比它大的值交换；
        3.将位置i后的降序序列进行反转。
        """
        nums_len = len(nums)
        change_i = -1
        for i in range(nums_len-2, -1, -1):
            if nums[i] < nums[i+1]:
                change_i = i
                break
        if change_i > -1:
            for j in range(nums_len-1, change_i, -1):
                if nums[change_i] < nums[j]:
                    temp = nums[j]
                    nums[j] = nums[change_i]
                    nums[change_i] = temp
                    break
        for i in range(1, (nums_len-change_i)//2+1):
            temp = nums[change_i+i]
            nums[change_i+i] = nums[nums_len-i]
            nums[nums_len-i] = temp
        print(nums)


if __name__ == "__main__":
    solution = Solution()
    solution.next_permutation([1, 3, 2])



