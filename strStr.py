"""
question:

example:

"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :param haystack: str
        :param needle: str
        :return: int
        """
        start_index = 0
        haystack_len = len(haystack)
        needle_len = len(needle)
        if needle_len == 0:
            return 0
        while start_index + needle_len <= haystack_len:
            if haystack[start_index:start_index+needle_len] == needle:
                return start_index
            else:
                start_index = start_index + 1
        if start_index + needle_len > haystack_len or needle_len > haystack_len:
            return -1


if __name__ == "__main__":
    test_haystack = "mississippi"
    test_needle = "issipi"
    solute = Solution()
    start_index = solute.strStr(test_haystack, test_needle)
    print(start_index)
