"""
合并有序链表
question:
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

examples:
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

def create_link_list(list_number):
    link_list = ListNode(0)
    now_node = link_list
    for temp in list_number:
        new_node = ListNode(temp)
        now_node.next = new_node
        now_node = new_node
    return link_list.next


class Solution:
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_now_node = l1
        l2_now_node = l2
        result = ListNode(0)
        now_node = result
        while (l1_now_node is not None) and (l2_now_node is not None):
            if l1_now_node.val < l2_now_node.val:
                now_node.next = l1_now_node
                now_node = l1_now_node
                l1_now_node = l1_now_node.next
            else:
                now_node.next = l2_now_node
                now_node = l2_now_node
                l2_now_node = l2_now_node.next
        if l1_now_node is None:
            now_node.next = l2_now_node
        else:
            now_node.next = l1_now_node
        return result.next


if __name__ == '__main__':
    l1 = [1, 2, 3, 4]
    l2 = [2, 3, 4, 5, 6, 7]
    l1_link_list = create_link_list(l1)
    l2_link_list = create_link_list(l2)

    link_list = Solution()
    re = link_list.merge_two_lists(l1_link_list, l2_link_list)
    now_node = re
    while now_node:
        print(now_node.val)
        now_node = now_node.next

