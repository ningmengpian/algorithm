"""
question:
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

example:
示例 1:
输入: 1->1->2
输出: 1->2

"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :param head: ListNode
        :return: ListNode
        """
        if head is None or head.next is None:
            return head
        p = head
        next_p = head.next
        while next_p is not None:
            if p.val == next_p.val:
                p.next = next_p.next
            else:
                p = next_p
            next_p = next_p.next
        return head


def create_node(node_val):
    head = ListNode(0)
    p = head
    for val in node_val:
        new_node = ListNode(val)
        p.next = new_node
        p = new_node
    return head


if __name__ == "__main__":
    test_data = [1, 2, 2, 3, 5, 5, 6, 6]
    list_node = create_node(test_data)

    solution = Solution()
    result = solution.deleteDuplicates(list_node.next)
    p = result
    while p is not None:
        print('%s->' % p.val)
        p = p.next
