class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        min_price=prices[0]
        max_pro=0
        for price in prices:
            min_price= min(min_price, price)
            max_pro= max(max_pro, (price-min_price))
        return max_pro











        # maxi=0
        # for l in range(n):
        #     r=l+1
        #     while r<n:
        #         if prices[l]<prices[r]:
        #             w=prices[r]-prices[l]
        #             maxi=max(maxi,w)
        #             r+=1
        #         else:
        #             r+=1
        # return maxi


