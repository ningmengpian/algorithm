"""
question:
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array

example:
示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""


class Solution:

    def search_element_index(self, nums, target, left_flag):
        # 用于控制寻找target的左边界点，让下一次循环的数组位于中间节点的左侧
        left = 0
        right = len(nums)
        while left < right:
            middle = (right + left) // 2
            if nums[middle] > target or (left_flag and nums[middle] == target):
                right = middle
            else:
                left = middle + 1
        return left

    def search_range(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        # 采用二分查找
        start = self.search_element_index(nums, target, True)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        return [start, self.search_element_index(nums, target, False) - 1]


if __name__ == "__main__":
    solution = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    result = solution.search_range(nums, target)
    print(result)
