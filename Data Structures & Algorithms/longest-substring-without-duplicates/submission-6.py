class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=1
        ans=0
        n=len(s)
        if s=="":
            return 0
        else:
            seen=s[l]
            while r<n:
                if s[r] not in seen:
                    seen+= s[r]
                    r+=1
                
                else:
                    ans=max(ans,len(seen))
                    l+=1
                    r= l+1
                    seen=s[l]
            ans=max(ans,len(seen))
        return ans