"""
question:
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list

example:
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.

说明：
给定的 n 保证是有效的。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        """遍历链表，将节点指针存到数组中，然后再执行删除操作"""
        if head is None:
            return None
        node = []
        p = head
        while p is not None:
            node.append(p)
            p = p.next
        node_len = len(node)
        prev_node = node_len - n - 1
        current_node = node_len - n
        if prev_node < 0:
            return head.next
        node[prev_node].next = node[current_node].next
        return head

    def remove_nth_from_end_2(self, head: ListNode, n: int) -> ListNode:
        """使用快慢双指针，起始时中间间隔n个节点, 注意起始位置虚节点的使用"""
        dummy = ListNode(0)
        dummy.next = head
        index = 0
        slow = dummy
        fast = dummy
        while fast is not None:
            if index > n:
                slow = slow.next
            index += 1
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next


def create_list_node(values: list):
    head = ListNode(0)
    p = head
    if values is not None:
        for value in values:
            node = ListNode(value)
            p.next = node
            p = node
    return head.next


def link_node_show(list_node: ListNode):
    p = list_node
    while p is not None:
        print('%s-->' % p.val)
        p = p.next


if __name__ == "__main__":
    values = [1, 2]
    head = create_list_node(values)
    n = 2
    solution = Solution()
    # 方法一：
    # result = solution.remove_nth_from_end(head, n)

    # 方法二：
    result = solution.remove_nth_from_end_2(head, n)

    link_node_show(result)
