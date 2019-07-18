"""
question:
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays

example:
示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5
"""


class Solution(object):
    def findMedianSortedArray(self, nums1, nums2):
        """
        :param nums1: List[int]
        :param nums2: List[int]
        :return: float
        """

        merge_array = []
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        all_array_len = len(nums1) + len(nums2)
        mid_right = all_array_len // 2
        index = 0
        nums1_index = 0
        nums2_index = 0
        while index <= mid_right:
            if nums1_index == nums1_len:
                end_index = nums2_index + mid_right - index + 1
                merge_array = merge_array + nums2[nums2_index:end_index]
                break
            if nums2_index == nums2_len:
                end_index = nums1_index + mid_right - index + 1
                merge_array = merge_array + nums1[nums1_index:end_index]
                break
            if nums1[nums1_index] < nums2[nums2_index]:
                merge_array.append(nums1[nums1_index])
                nums1_index = nums1_index + 1
            else:
                merge_array.append(nums2[nums2_index])
                nums2_index = nums2_index + 1
            index = index + 1
        if all_array_len % 2 == 0:
            return (merge_array[mid_right-1]+merge_array[mid_right])/2.0
        return merge_array[mid_right]


if __name__ == "__main__":
    test_nums1 = [1, 2]
    test_nums2 = [3, 4]

    solution = Solution()
    median = solution.findMedianSortedArray(test_nums1, test_nums2)
    print(median)
