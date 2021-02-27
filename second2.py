from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()
        self.nums = nums
        for i in range(len(nums) + 1):
            self.length = i
            self.back_track(0, 0)
        return self.res

    def back_track(self, index, curr_len, temp=[]):
        if curr_len == self.length:
            self.res.append(list(temp))
            return
        for i in range(index, len(self.nums)):
            temp.append(self.nums[i])
            self.back_track(index + 1, curr_len + 1, temp)
            temp.pop()
