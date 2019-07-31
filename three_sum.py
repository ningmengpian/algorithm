"""
question:
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得
a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum

example:
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution(object):
    def three_sum(self, nums):
        """
        :param nums: List[int]
        :return: List[List[int]]
        """
        nums_len = len(nums)
        now_index = 0
        ans_list = []

        # step1 排序
        nums_sort = sorted(nums)

        # step2 遍历有序列表
        while now_index < nums_len - 2 and nums_sort[now_index] <= 0:
            left_index = now_index + 1
            right_index = nums_len - 1
            while left_index < right_index:
                sum_val = nums_sort[now_index] + nums_sort[left_index] + \
                      nums_sort[right_index]
                if sum_val > 0:
                    right_index -= 1
                elif sum_val < 0:
                    left_index += 1
                else:
                    ans_list.append(
                        [nums_sort[now_index], nums_sort[left_index],
                         nums_sort[right_index]])
                    left_index += 1
                    right_index -= 1
                    while (left_index < nums_len and
                           nums_sort[left_index-1] == nums_sort[left_index]):
                        left_index += 1
                    while (right_index > 0 and
                           nums_sort[right_index+1] == nums_sort[right_index]):
                        right_index -= 1

            now_index += 1
            while (now_index < nums_len - 2 and
                   nums_sort[now_index] == nums_sort[now_index - 1]):
                now_index += 1
        return ans_list


if __name__ == "__main__":
    test_nums = [-2, 0, 0, 2, 2]
    solution = Solution()
    ans_list = solution.three_sum(test_nums)
    print(ans_list)

