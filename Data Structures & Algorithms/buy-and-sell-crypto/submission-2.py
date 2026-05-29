class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        l=0
        maxi=0
        r=1
        while r<n:
            if prices[l]<prices[r]:
                maxi=max(maxi,(prices[r]-prices[l]))
                r+=1
            else:
                l=r
                r+=1
            
        return maxi
















        # min_price=prices[0]
        # max_pro=0
        # for price in prices:
        #     min_price= min(min_price, price)
        #     max_pro= max(max_pro, (price-min_price))
        # return max_pro











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


