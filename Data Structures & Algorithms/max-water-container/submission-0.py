class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        l=0
        r=n-1
        maxi=0
        ans=0
        while l<r:

            mini=min(heights[l],heights[r])
            ans=max(ans, ((r-l)*mini))
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return ans

