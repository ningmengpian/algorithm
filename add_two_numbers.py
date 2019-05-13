"""
question：
给出两个非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，
并且它们的每个节点只能存储一位数字。如果，我们将这两个数相加起来，则会返回一个新的链表来表
示它们的和。您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

example：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

"""


class ListNode:

    def __init__(self, x):
        self.value = x
        self.next = None


class Solution:

    def add_two_numbers(self, number_1, number_2):
        """
        :type number_1: listNode
        :type number_2: listNode
        :rtype: listNode
        """

        next_1 = number_1
        next_2 = number_2
        result = ListNode(0)
        now_node = result
        carry = 0
        while next_1 is not None or next_2 is not None:
            now_place_sum = 0
            next_1_value = 0
            next_2_value = 0
            if next_1 is not None:
                next_1_value = next_1.value
            if next_2 is not None:
                next_2_value = next_2.value
            now_place_sum = next_1_value + next_2_value + carry
            now_place_value = now_place_sum % 10
            carry = now_place_sum // 10
            new_node = ListNode(now_place_value)
            now_node.next = new_node
            now_node = new_node
            if next_1 is not  None:
                next_1 = next_1.next
            if next_2 is not None:
                next_2 = next_2.next
        if carry > 0:
            now_node.next = ListNode(1)
        return result.next


def create_listnode(list_number):
    listnode_number = ListNode(0)
    now_node = listnode_number
    if list_number is not None:
        for value in list_number:
            new_node = ListNode(value)
            now_node.next = new_node
            now_node = new_node
    return listnode_number.next


if __name__ == '__main__':
    number_1 = create_listnode([2, 4, 3])
    number_2 = create_listnode([5, 6, 4])
    solution = Solution()
    result = solution.add_two_numbers(number_1, number_2)
    now_result = result
    while now_result:
        print(now_result.value)
        now_result = now_result.next
