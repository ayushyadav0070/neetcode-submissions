class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        ans=0
        n=len(s)
        seen= []
        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.append(s[r])
            ans = max (ans, r-l+1)
        return ans
                













        # ans=0
        # n=len(s)
        # if s=="":
        #     return 0
        # else:
        #     seen=s[l]
        #     while r<n:
        #         if s[r] not in seen:
        #             seen+= s[r]
        #             r+=1
                
        #         else:
        #             ans=max(ans,len(seen))
        #             l+=1
        #             r= l+1
        #             seen=s[l]
        #     ans=max(ans,len(seen))
        # return ans