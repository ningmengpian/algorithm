"""
question:
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
说明 :
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

example:
给定这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5
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
    def reverse_k_group(self, head, k):
        """
        :param head: ListNode
        :param k: int
        :return: ListNode
        """
        # 尝试使用快慢指针, 慢指针指向待交换的起始节点的前一个节点，快指针指向待交换的节点的最后一个节点
        if k == 1 or head is None:
            return head
        mark_node = ListNode(0)
        mark_node.next = head
        slow = head
        fast = head.next
        start = mark_node
        while fast is not None:
            k_count = 1
            while k_count < k and fast is not None:
                   fast = fast.next
                   k_count += 1
            if k_count == k:
                while slow.next != fast:
                    temp_node = slow.next
                    slow.next = temp_node.next
                    temp_node.next = start.next
                    start.next = temp_node
            start = slow
            slow = slow.next
            if fast is not None:
                fast = fast.next
        return mark_node.next


if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list_node = create_link_list(test_list)

    solute = Solution()
    result = solute.reverse_k_group(list_node, 9)
    temp = result
    while temp is not None:
        print(temp.val)
        temp = temp.next
