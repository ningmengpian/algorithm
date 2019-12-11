"""
question:
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-sudoku

example:
示例 1:

输入:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: true
"""


class Solution:

    def is_valid_sudoku(self, board):
        """
        :param board: List[List[str]]
        :return: bool
        """
        # 遍历求解、哈希映射
        rows = [{} for i in range(9)]
        columns = [{} for j in range(9)]
        boxes = [{} for index in range(9)]

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value != '.':
                    value = int(value)
                    index = (i // 3) * 3 + (j // 3)

                    rows[i][value] = rows[i].get(value, 0) + 1
                    columns[j][value] = columns[j].get(value, 0) + 1
                    boxes[index][value] = boxes[index].get(value, 0) + 1
                    if rows[i][value] > 1 or columns[j][value] > 1 or boxes[
                        index][value] > 1:
                        return False
        return True


if __name__ == "__main__":
    solution = Solution()
    board = \
        [
          ["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]
        ]
    result = solution.is_valid_sudoku(board)
    print(result)
