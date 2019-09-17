"""
question:
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
注意：
答案中不可以包含重复的四元组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum

example:
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution:
    """遍历求解，提交后超时"""
    def four_sum(self, nums, target):
        two_sum = {}
        four_index = set()
        list_len = len(nums)
        first_index = 0
        key = 1

        # 求两数之和
        while first_index < list_len - 1:
            second_index = first_index + 1
            while second_index < list_len:
                temp_sum = nums[first_index] + nums[second_index]
                index = [first_index, second_index]
                two_sum[key] = [temp_sum, index]
                key += 1
                second_index += 1
            first_index += 1

        # 求四数之和
        key_first = 1
        while key_first < key - 1:
            key_second = key_first + 1
            while key_second < key:
                first_two_sum = two_sum[key_first]
                second_two_sum = two_sum[key_second]
                if set(first_two_sum[1]).isdisjoint(set(second_two_sum[1])) \
                        and first_two_sum[0] + second_two_sum[0] == target:
                    temp_index = (nums[first_two_sum[1][0]],
                                  nums[first_two_sum[1][1]],
                                  nums[second_two_sum[1][0]],
                                  nums[second_two_sum[1][1]])
                    # 排序，方便去重
                    temp_index = sorted(temp_index)
                    temp_index = tuple(temp_index)
                    four_index.add(temp_index)
                key_second += 1
            key_first += 1

        # 结果去重
        four_result = []
        for temp_index in four_index:
            four_result.append(list(temp_index))

        return four_result

    def four_sum_2(self, nums, target):
        """固定两个数的和，然后使用两指针寻找另外两个数, 并利用有序数组优化查找"""
        nums_len = len(nums)
        # 排序
        nums.sort()
        four_result = set()

        # 固定两个数的和寻找另外两个数
        for first in range(nums_len-3):
            for second in range(first+1, nums_len-2):
                left = second + 1
                right = nums_len - 1
                while left < right:
                    four_sum = nums[first] + nums[second] + nums[left] + nums[right]
                    if target == four_sum:
                        four_result.add((nums[first], nums[second], nums[left],
                                         nums[right]))
                        left += 1
                        right -= 1
                    elif target < four_sum:
                        right -= 1
                    else:
                        left += 1

        # 去重
        result = []
        for temp in four_result:
            result.append(list(temp))

        return result


if __name__ == "__main__":
    test_list = [1, 0, -1, 0, -2, 2]
    target = 0
    solution = Solution()

    # 方法一
    result = solution.four_sum(test_list, target)

    # 方法二
    result = solution.four_sum_2(test_list, target)
    for val in result:
        print(val)
