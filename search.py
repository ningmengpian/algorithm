"""
question:
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array

example:

示例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

示例 2:
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
"""


class Solution:

    def search(self, nums, target):
        """
        :param nums: list[int]
        :param target: int
        :return: int
        搜索旋转排序数组
        """
        # 使用二分查找
        rotation = 0
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = left + (right - left + 1) // 2
            if nums[middle] < nums[middle - 1]:
                rotation = middle - 1
                break
            else:
                if nums[left] < nums[middle]:
                    left = middle + 1
                else:
                    right = middle - 1
        if len(nums) > 0 and target >= nums[0]:
            left = 0
            right = rotation
            while left < right:
                middle = left + (right - left + 1) // 2
                if target == nums[middle]:
                    return middle
                elif target < nums[middle]:
                    right = middle
                else:
                    left = middle
        else:
            left = rotation
            right = len(nums) - 1
            while left < right:
                middle = left + (right - left + 1) // 2
                if target == nums[middle]:
                    return middle
                elif target < nums[middle]:
                    right = middle
                else:
                    left = middle
        return -1

    # def search_2(self, nums, target):
    #


if __name__ == "__main__":
    solution = Solution()
    nums = [4, 5, 6, 7, 8, 9, 0, 1, 2]
    target = 3
    result = solution.search(nums, target)
    print(result)
