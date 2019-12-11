"""
question:
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum

example:
示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]

示例 2:
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

import copy


class Solution:

    def combination_sum(self, candidates, target):
        """
        :param candidates: List[int]
        :param target: int
        :return: List[List[int]]
        """
        all_ans = []
        candidates = sorted(candidates)
        end_flag = 1

        for temp in candidates:
            if temp <= target:
                all_ans.append([[temp], target - temp])
        while end_flag:
            ans_len = len(all_ans)
            end_val = 0
            for ans_index in range(ans_len):
                new_ans_temp = copy.deepcopy(all_ans[ans_index])
                ans_temp = all_ans[ans_index]
                if ans_temp[1] >= candidates[0]:
                    end_val += 1
                    if ans_temp[0][len(ans_temp[0])-1] <= candidates[0]:
                        ans_temp[0].append(candidates[0])
                        ans_temp[1] = ans_temp[1] - candidates[0]
                    else:
                        ans_temp[1] = -1
                    index = 1
                    while index < len(candidates) and new_ans_temp[1] >= \
                            candidates[index]:
                        if new_ans_temp[0][len(new_ans_temp[0])-1] <= \
                                candidates[index]:
                            add_temp = copy.deepcopy(new_ans_temp)
                            add_temp[0].append(candidates[index])
                            add_temp[1] = add_temp[1] - candidates[index]
                            all_ans.append(add_temp)
                        index += 1
            if end_val == 0:
                end_flag = 0
        # 移除总和不为sum的组合数
        ans = []
        for temp in all_ans:
            if temp[1] == 0:
                ans.append(temp[0])
        return ans


if __name__ == "__main__":
    solution = Solution()
    candidates = [7, 3, 2]
    target = 18
    result = solution.combination_sum(candidates, target)
    print(result)
