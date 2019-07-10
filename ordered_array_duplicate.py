"""
question:
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array

说明：
为什么返回数值是整数，但输出的答案是数组呢?
请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

example:
给定数组 nums = [1,1,2],
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
你不需要考虑数组中超出新长度后面的元素。

"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :param nums: List[int]
        :return: int
        """
        nums_len = len(nums)
        new_index = 0
        for now_index in range(1, nums_len):
            if nums[new_index] != nums[now_index]:
                new_index = new_index + 1
                nums[new_index] = nums[now_index]
        if nums_len == 0:
            return 0
        return new_index + 1


if __name__ == "__main__":
    test_data = []
    solution = Solution()
    new_list_len = solution.removeDuplicates(test_data)
    print(test_data, new_list_len)
