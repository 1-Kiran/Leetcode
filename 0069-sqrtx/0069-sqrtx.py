class Solution(object):
    def mySqrt(self, x):
        r=x
        if x<2:
            return x
        while r*r>x:
            r=(r+x//r)//2
        return r