class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        maxi=0
        for l in range(n):
            r=l+1
            while r<n:
                if prices[l]<prices[r]:
                    w=prices[r]-prices[l]
                    maxi=max(maxi,w)
                    r+=1
                else:
                    r+=1
        return maxi


