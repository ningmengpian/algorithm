"""
问题：
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs

示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.
"""

from list_node import ListNode, ListNodeFunction


def swap_pairs(line_list):
    """
    :param line_list: List[ListNode]
    :return: List[ListNode]
    """
    if not line_list:
        return line_list

    # 新增临时头节点，用于标记链表
    head = ListNode(0)
    head.next = line_list

    # 相邻两节点交换
    first_node = head
    second_node = head.next
    while second_node and second_node.next:
        first_node.next = second_node.next
        second_node.next = second_node.next.next
        first_node.next.next = second_node
        first_node = second_node
        second_node = second_node.next
    return head.next


if __name__ == "__main__":
    list_val = [1, 2, 3, 4, 5, 6]
    list_f = ListNodeFunction()
    line_list = list_f.create_back(list_val)
    ans = swap_pairs(line_list)
    list_f.output(ans)
