"""
排序算法简单实现
"""

class Sort(object):
    def selection_sort(self, ary):
        """
        选择排序思想：
        step1:从未排序的序列中找到最小（大）值，将其存放到排序序列的首位置；
        step2:从剩余的未排序序列中找到最小（大）值，将其存放到已排序序列的末尾。
        :param ary: List[int]
        :return: List[int]
        """
        ary_len = len(ary)
        i = 0
        while i < ary_len - 1:
            k = i
            j = i + 1
            while j < ary_len:
                if ary[j] < ary[k]:
                    k = j
                j += 1
            temp = ary[i]
            ary[i] = ary[k]
            ary[k] = temp

            i += 1
        return ary

    def bubble_sort(self, ary):
        """
        冒泡排序思想：多次循环未排序的序列，在每次循环中依次比较序列中相邻两项的值，
        将较大（小）的值向后交换
        :param ary: List[int]
        :return: List[int]
        """
        ary_len = len(ary)
        i = 0
        while i < ary_len - 1:
            j = 0
            while j < ary_len - i - 1 and ary[j] > ary[j+1]:
                temp = ary[j]
                ary[j] = ary[j+1]
                ary[j+1] = temp
                j += 1
            i += 1
        return ary

    def insert_sort(self, ary):
        """
        插入排序思想：
        step1:将序列第一个元素视为已被排序；
        step2:选取一个未排序序列中的值（默认为首个未被排序值），然后从后向前遍历已排序序列，
        将选取的值插入到大于等于它的值的前面（即第j项若大于第j-1项，则交换位置），直到选取
        的值更大为止
        :param ary: List[int]
        :return: List[int]
        """
        ary_len = len(ary)
        i = 0
        while i < ary_len - 1:
            j = i + 1
            while j > 0 and ary[j] < ary[j-1]:
                temp = ary[j-1]
                ary[j-1] = ary[j]
                ary[j] = temp
                j -= 1
            i += 1
        return ary

    def shell_sort(self, ary):
        """
        希尔排序思想：希尔排序为插入排序的优化，其可增大被比较的两个元素的距离。
        step1：通过希尔增量将序列划分为多组，将每组进行插入排序；
        step2：按照一定规则缩小希尔增量（此处取gap/=2）,直至增量为1，此时只需对整个序列
        进行微调即可。
        :param ary: List[int]
        :return: List[int]
        """
        ary_len = len(ary)
        gap = ary_len // 2
        while gap > 0:
            i = gap
            while i < ary_len:
                pre_index = i
                while pre_index >= gap and ary[pre_index] < ary[pre_index-gap]:
                    temp = ary[pre_index]
                    ary[pre_index] = ary[pre_index-gap]
                    ary[pre_index-gap] = temp
                    pre_index -= gap
                i += 1
            gap = gap // 2
        return ary


    def merge(self, left_ary, right_ary):
        """
        function：用于归并两个待排序序列
        :param left_ary:
        :param right_ary:
        :return:
        """
        left_ary_len = len(left_ary)
        right_ary_len = len(right_ary)
        result = []
        left_index = 0
        right_index = 0
        for index in range(0, left_ary_len+right_ary_len):
            if left_index >= left_ary_len:
                result.append(right_ary[right_index])
                right_index += 1
            elif right_index >= right_ary_len:
                result.append(left_ary[left_index])
                left_index += 1
            elif left_ary[left_index] > right_ary[right_index]:
                result.append(right_ary[right_index])
                right_index += 1
            else:
                result.append(left_ary[left_index])
                left_index += 1
        return result


    def merge_sort(self, ary):
        """
        归并排序思想：
        step1将序列划分为若干子序列，并将子序列进行排序；
        step2将排好序的子序列两两归并，直至归并为一个有序序列；
        :param ary: List[int]
        :return: List[int]
        """
        import copy

        ary_len = len(ary)
        if ary_len < 2:
            return ary
        mid = (ary_len + 1) // 2
        left_ary = copy.deepcopy(ary[0:mid])
        right_ary = copy.deepcopy(ary[mid:ary_len])
        print(ary)
        return self.merge(self.merge_sort(left_ary), self.merge_sort(right_ary))


    def quick(self, ary, left, right):
        """
        :param ary: List[int]
        :param left: int
        :param right: int
        :return: List[int]
        """
        fiducial_val = ary[left]
        left_index = left
        right_index = right
        while left_index < right_index:
            while ary[right_index] > fiducial_val and left_index < right_index:
                right_index -= 1
            while ary[left_index] <= fiducial_val and left_index < right_index:
                left_index += 1
            if left_index != right_index:
                temp = ary[left_index]
                ary[left_index] = ary[right_index]
                ary[right_index] = temp
            else:
                ary[left] = ary[left_index]
                ary[left_index] = fiducial_val
        return left_index

    def quick_sort(self, ary, left, right):
        """
        快速排序思想：在待排序列中选取一个元素作为基准值（一般为序列第一个元素），从序列
        两端同时进行遍历，将左端大于基准值的元素与右端小于等于基准值的元素交换，直至相遇，然后
        把相遇位置的值与基准值进行交换，完成一趟快排。根据基准值位置将序列分为两个子序列再次
        进行快排，直至无子序列。
        :param arry:
        :return:
        """
        ary_len = len(ary)
        if ary_len == 0:
            return None
        fiducial_index = self.quick(ary, left, right)
        if fiducial_index > left:
            self.quick_sort(ary, left, fiducial_index-1)
        if fiducial_index < right:
            self.quick_sort(ary, fiducial_index+1, right)
        return ary

    def count_sort(self, ary):
        """
        计数排序思想：将取值范围固定的序列值作为新数组的下标，统计序列中元素值出现的次数并
        存入该元素值作为下标的新数组元素中
        :param ary: List[int]
        :return: List[int]
        """
        ary_len = len(ary)
        if ary_len < 1:
            return ary

        max_val = ary[0]
        min_val = ary[0]
        # step1 查找序列最大值及最小值
        for temp in ary:
            if max_val < temp:
                max_val = temp
            if min_val > temp:
                min_val = temp

        # step2 新建存储元素值出现次数的数组并遍历统计元素值出现次数
        count_len = max_val - min_val + 1
        count_val = [0] * count_len
        for temp in ary:
            count_val[temp-min_val] += 1

        # step3 遍历输出数组中统计值不为零的下标，即已排好序的数组
        ans = []
        index = 0
        while index < count_len:
            while count_val[index] > 0:
                ans.append(index)
                count_val[index] -= 1
            index += 1
        return ans

    def radix_sort(self, ary):
        """
        基数排序思想：基数排序是非比较排序方法中的一种，按照数的位数从低位到高位依次按计数
        排序方法进行排序。
        注意python浅拷贝对改变多维列表的影响
        :param ary: List[int]
        :return: List[int]
        """
        ary_len = len(ary)
        if ary_len < 2:
            return ary

        # step1 查找序列最大值,并求出序列元素的最高位数
        max_val = ary[0]
        for temp in ary:
            if max_val < temp:
                max_val = temp
        digits = len(str(max_val))

        # step2 循环元素位数及序列，实现排序
        for digit in range(digits, -1, -1):
            digit_sort = [[] for i in range(10)]
            for temp in ary:
                temp_str = str(temp)
                if len(temp_str) >= digit:
                    sort_index = int(temp_str[digit-1])
                else:
                    sort_index = 0
                digit_sort[sort_index].append(temp)

            index = 0
            for sort_temp in digit_sort:
                digit_index = 0
                while digit_index < len(sort_temp):
                    ary[index] = sort_temp[digit_index]
                    index += 1
                    digit_index += 1
        return ary

    def heap_sort(self, ary):
        """
        堆排序思想：利用二叉树的性质可将树存储于数组中，父结点及子节点的关系如下：若数组
        下标从0开始，父结点下标为n，则其左右子节点的小标分别为（2*n+1）、（2*n+2）。利用
        二叉树的性质可将序列构造为父结点与子节点之间满足某种关系的二叉树，即最大堆或最小堆，
        然后输出并移除根节点（此时为最大值或最小值），重复以上操作，对剩下的序列值重新构建
        最大堆，直到序列长度为1，此时完成排序。
        :param ary: List[int]
        :return: List[int]
        """
        ary_len = len(ary)
        index = ary_len - 1
        while index > 0:
            # 计算最后一个节点的父结点，即最后一个非叶子节点
            last_parent_node = (index-1) // 2
            # 遍历所有非叶子节点，构造最大堆
            for node_index in range(last_parent_node, -1, -1):
                left_node = 2 * node_index + 1
                right_node = 2 * node_index + 2
                larger_index = left_node
                if right_node <= index and ary[left_node] < ary[right_node]:
                    larger_index = right_node
                if ary[node_index] < ary[larger_index]:
                    temp = ary[node_index]
                    ary[node_index] = ary[larger_index]
                    ary[larger_index] = temp
            # 交换序列第一个元素及最后一个元素的值，并使序列长度减1（此时根节点为序列的最大值）
            temp = ary[0]
            ary[0] = ary[index]
            ary[index] = temp
            index -= 1
        return ary


if __name__ == "__main__":
    test_ary = [1, 24, 16, 37, 0, 1, 0]

    sort = Sort()

    # 选择排序
    # selection_ans = sort.selection_sort(test_ary)
    # print(selection_ans)

    # 冒泡排序
    # bubble_ans = sort.bubble_sort(test_ary)
    # print(bubble_ans)

    # 插入排序
    # insert_ans = sort.insert_sort(test_ary)
    # print(insert_ans)

    # 希尔排序
    # shell_ans = sort.shell_sort(test_ary)
    # print(shell_ans)

    # 归并排序
    # merge_ans = sort.merge_sort(test_ary)
    # print(merge_ans)

    # 快排
    # quick_sort = sort.quick_sort(test_ary, 0, len(test_ary)-1)
    # print(quick_sort)

    # 计数排序
    # count_sort = sort.count_sort(test_ary)
    # print(count_sort)

    # 基数排序
    # radix_sort = sort.radix_sort(test_ary)
    # print(radix_sort)

    # 堆排序
    heap_sort = sort.heap_sort(test_ary)
    print(heap_sort)
