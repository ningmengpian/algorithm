"""
question:
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条
垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴
共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。
输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water

example:
示例:
输入: [1,8,6,2,5,4,8,3,7]
输出: 49
"""


class Solution(object):
    def maxArea(self, height):
        """
        思想：使用双指针方法。容器的面积受矩形区域的长宽影响，其长为包含的元素的间距个数，
        最大为包含所有元素，其宽受限于两个边界元素的最小值，因此使用俩个指针分别指向第一个
        和最后一个元素，计算其容量，然后移动指向值较小的指针指向下一个元素，直到两指针相遇。
        :param height: List[int]
        :return: int
        """

        height_len = len(height)
        lef = 0
        rig = height_len - 1
        max_area = 0
        while lef < rig:
            if height[lef] < height[rig]:
                width = height[lef]
                lef += 1
            else:
                width = height[rig]
                rig -= 1
            area = (rig - lef + 1) * width
            max_area = max_area if max_area > area else area
        return max_area


if __name__ == '__main__':
    test_data = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    solution = Solution()

    ans = solution.maxArea(test_data)
    print(ans)
