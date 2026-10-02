class Solution(object):
    def maxProduct(self, nums):
        current_max = current_min = max_pro = nums[0]
        
        for num in nums[1:]:
            if num < 0:
                current_max, current_min = current_min, current_max
            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)
            max_pro = max(max_pro, current_max)
        return max_pro