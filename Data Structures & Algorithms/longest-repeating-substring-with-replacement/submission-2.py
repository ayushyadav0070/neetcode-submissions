class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq={}
        n=len(s)
        l=0
        ans=0
        maxfreq=0
        for r in range(n):
            freq[s[r]]=freq.get(s[r],0)+1
            maxfreq= max(maxfreq, freq[s[r]])
            while (r-l+1)-maxfreq>k:
                freq[s[l]]-=1
                l+=1
            ans= max(ans,r-l+1)
        return ans


        