class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        c=0
        m_s=sum(arr[:k])
        if m_s>=k*threshold:
            c+=1
        for i in range(k,len(arr)):
            m_s=m_s-arr[i-k]+arr[i]
            if m_s>=k*threshold:
                c+=1
        return c