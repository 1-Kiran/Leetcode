class Solution(object):
    def findMaxAverage(self, nums, k):
        w_s=m_s=sum(nums[:k])
        for i in range(k,len(nums)):
            w_s=w_s-nums[i-k]+nums[i]
            m_s=max(m_s,w_s)
        return m_s/float(k)