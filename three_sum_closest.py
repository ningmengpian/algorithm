"""
question:
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它
们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest

example:
给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""


class Solution(object):
    def three_sum_closet(self, nums, target):
        """
        思想：首先对序列进行排序，然后每次固定序列的一个元素，并使用双指针分别指向固定元素
        的后一个元素及末尾元素，计算当前三个数的和并与目标值进行比较，记录两者差值，若差值
        更小则更新差值；若三个数的和比目标值大，则右侧指针向前移动一位，若小于目标值则左侧
        指针向后移动一位，若相等则返回当前差值加固定值。
        :param nums: List[int]
        :param target: int
        :return: int
        """
        nums_len = len(nums)

        nums_sort = sorted(nums)
        index = 0
        min_val = nums_sort[0] + nums_sort[1] + nums_sort[2] - target

        while index < nums_len - 2:
            left_index = index + 1
            right_index = nums_len - 1
            while left_index < right_index:
                sum_val = nums_sort[index] + nums_sort[left_index] + \
                          nums_sort[right_index]
                dif_val = sum_val-target
                min_val = min_val if abs(dif_val) > abs(min_val) else dif_val
                if sum_val < target:
                    left_index += 1
                elif sum_val > target:
                    right_index -= 1
                else:
                    return sum_val
            index += 1
        return min_val + target


if __name__ == "__main__":
    test_nums = [0, 0, 0]
    test_target = 1

    solution = Solution()
    sum_closet = solution.three_sum_closet(test_nums, test_target)
    print(sum_closet)
