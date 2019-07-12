"""
question:
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。

example:
输入: [1,3,5,6], 5
输出: 2

"""


class Solution(object):
    def searchIndex(self, nums, target, l_index, r_index):
        if l_index == r_index:
            if target == nums[l_index]:
                return l_index
            elif target < nums[l_index]:
                return l_index
            else:
                return l_index + 1
        mid_index = (r_index - l_index + 1)//2 + l_index
        print(mid_index)
        if target == nums[mid_index]:
            return mid_index
        elif target < nums[mid_index]:
            return self.searchIndex(nums, target, l_index, mid_index-1)
        else:
            return self.searchIndex(nums, target, mid_index, r_index)

    def searchInsert(self, nums, target):
        """
        :param nums:
        :param target:
        :return:
        """
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        return self.searchIndex(nums, target, 0, nums_len-1)


if __name__ == "__main__":
    test_nums = [2, 7, 8, 9, 10]
    test_target = 11
    solution = Solution()
    target_insert_index = solution.searchInsert(test_nums, test_target)
    print(target_insert_index)
