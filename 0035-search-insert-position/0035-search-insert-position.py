class Solution(object):
    def searchInsert(self, n, target):
        l=0
        r=len(n)-1
        while l<=r:
            mid=(l+r)//2
            if n[mid]==target:
                return mid
            elif n[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return l