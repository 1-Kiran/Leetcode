class Solution(object):
    def majorityElement(self, nums):
        seen={}
        for num in nums:
            seen[num]=seen.get(num,0)+1
        return max(seen,key=seen.get)
