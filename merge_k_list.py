"""
问题：合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists

示例:
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 创建链表
def create_line_list(list_val):
    line_list = ListNode(0)
    now_node = line_list
    for item in list_val:
        new_node = ListNode(item)
        now_node.next = new_node
        now_node = new_node
    return line_list.next


class Solution:
    """
    暴力求解
    1、遍历k个链表，并将其值存入列表中；
    2、对列表进行排序；
    3、再将列表转换为链表
    """
    def merge_k_list_violence(self, lists):
        """
        :param lists: List[Node]
        :return: ListNode
        """
        ans_line_list = ListNode(0)
        now_node = ans_line_list
        ans_list = []
        for k_list in lists:
            while k_list:
                ans_list.append(k_list.val)
                k_list = k_list.next
        # 排序并转换为链表
        for item in sorted(ans_list):
            item_node = ListNode(item)
            now_node.next = item_node
            now_node = item_node
        return ans_line_list.next

    # TODO：添加分治法和逐一比较法


if __name__ == "__main__":
    list_1 = create_line_list([1, 2, 3, 4, 5, 6])
    list_2 = create_line_list([3, 4, 6, 7])
    list_3 = create_line_list([5, 6, 8, 9])
    lists = [list_1, list_2, list_3]

    solution = Solution()
    # 暴力求解
    ans_line_list = solution.merge_k_list_violence(lists)

    # 结果输出
    while ans_line_list:
        print(ans_line_list.val)
        ans_line_list = ans_line_list.next
