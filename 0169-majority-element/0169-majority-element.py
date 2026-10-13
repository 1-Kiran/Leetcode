class Solution(object):
    def majorityElement(self, nums):
        seen={}
        for num in nums:
            seen[num]=seen.get(num,0)+1
        major=float('-inf')
        pre=0
        for num in seen.keys():
            if major<seen[num]:
                major=seen[num]
                pre=num
        return pre
