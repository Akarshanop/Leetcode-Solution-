class Solution(object):
    def maxProfit(self, prices):
        max_profit=0
        i,j = 0,1
        for j in range(len(prices)):
            if prices[i]<prices[j]:
                profit=prices[j]-prices[i]
                max_profit=max(max_profit,profit)
            elif prices[j]-prices[i]-max_profit<0:
                i=j
        return max_profit

solution= Solution()
print(solution.maxProfit([7,1,5,3,6,4]))