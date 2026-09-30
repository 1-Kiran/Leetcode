class Solution(object):
    def maxProfit(self, prices):
        buy=prices[0]
        sel=0
        for i in range(1, len(prices)):
            if prices[i]<buy:
                buy=prices[i]
            else:
                sel=max(sel, prices[i]-buy)
        return sel
        