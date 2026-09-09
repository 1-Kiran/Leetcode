class Solution(object):
    def minSubArrayLen(self, target, nums):
        l=0
        current_sum=0
        min_len=float('inf')
        for i in range(len(nums)):
            current_sum+=nums[i]
            while current_sum>=target:
                min_len=min(min_len,i-l+1)
                current_sum-=nums[l]
                l+=1
        return 0 if min_len==float('inf') else min_len