"""
question:
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
链接：https://leetcode-cn.com/problems/remove-element

example:
给定 nums = [3,2,2,3], val = 3,
函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
你不需要考虑数组中超出新长度后面的元素。

"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :param nums: List[int]
        :param val: int
        :return: int
        """
        nums_len = len(nums)
        positive_index = 0
        reversed_index = nums_len - 1
        while positive_index <= reversed_index:
            if nums[positive_index] == val:
                nums[positive_index] = nums[reversed_index]
                reversed_index = reversed_index - 1
            else:
                positive_index = positive_index + 1
        return reversed_index + 1


if __name__ == "__main__":
    test_list = [1, 2, 3, 5, 4]
    test_val = 2
    solution = Solution()
    new_list_len = solution.removeElement(test_list, test_val)
    result_list = test_list[0:new_list_len]
    print(result_list, new_list_len)
