class Solution(object):
    def maxAbsoluteSum(self, nums):
        current_min = current_max = nums[0]
        min_sum = max_sum = nums[0]

        for num in nums[1:]:
            current_max = max(num, num + current_max)
            current_min = min(num, num + current_min)

            max_sum = max(max_sum, current_max)
            min_sum = min(min_sum, current_min)

        return max(abs(min_sum), abs(max_sum))