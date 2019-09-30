"""链表"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNodeFunction:
    """链表常用方法"""

    def insert_front(self, line_list, data):
        # 从头部插入数值
        if not line_list:
            return line_list
        head = line_list
        new_node = ListNode(data)
        new_node.next = head
        line_list = new_node
        return line_list

    def insert_back(self, line_list, data):
        # 从尾部插入数值
        if not line_list:
            return line_list
        # 寻找最后一个节点
        pre_node = line_list
        while pre_node.next:
            pre_node = pre_node.next
        new_node = ListNode(data)
        pre_node.next = new_node
        return line_list

    def create_front(self, list_val):
        # 头插法新建链表
        head = ListNode(0)
        for val in list_val:
            new_node = ListNode(val)
            new_node.next = head.next
            head.next = new_node
        return head.next

    def create_back(self, list_val):
        # 尾插法新建链表
        head = now_node = ListNode(0)
        for val in list_val:
            new_node = ListNode(val)
            now_node.next = new_node
            now_node = new_node
        return head.next

    def delete_back(self, line_list):
        # 删除尾节点
        if not line_list or line_list.next is None:
            return None
        now_node = line_list
        while now_node.next.next:
            now_node = now_node.next
        now_node.next = None
        return line_list

    def reversal(self, line_list):
        # 链表翻转,使用头插法将链表节点逐一重新插入
        if not line_list or line_list.next is None:
            return line_list
        head = line_list
        now_node = line_list.next
        head.next = None
        while now_node:
            temp_node = now_node
            now_node = now_node.next
            temp_node.next = head
            head = temp_node
        return head

    def is_empty(self, line_list):
        # 判空
        if line_list is None:
            return True
        else:
            return False

    def output(self, line_lists):
        # 打印链表
        while not self.is_empty(line_lists):
            print('%s,' % line_lists.val, end='')
            line_lists = line_lists.next
        print('')


if __name__ == "__main__":
    list_val = [1, 2, 3, 5, 6, 7, 9]
    line_list = ListNodeFunction()

    # 头插法新建链表
    front_list = line_list.create_front(list_val)
    print("头插法新建链表：")
    line_list.output(front_list)

    # 头插
    new_list = line_list.insert_front(front_list, 45)
    print("头插：")
    line_list.output(new_list)

    # 尾插法新建链表
    back_list = line_list.create_back(list_val)
    print("尾插法新建链表：")
    line_list.output(back_list)

    # 尾插
    new_back_list = line_list.insert_back(back_list, 23)
    print("尾插：")
    line_list.output(new_back_list)

    # 删除尾节点
    delete_list = line_list.delete_back(back_list)
    print("删除尾节点：")
    line_list.output(back_list)

    # 链表翻转
    reversal_list = line_list.reversal(front_list)
    print("链表翻转：")
    line_list.output(reversal_list)
