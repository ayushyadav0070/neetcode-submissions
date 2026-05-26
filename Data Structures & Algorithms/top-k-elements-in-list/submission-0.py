class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n= len(nums)
        freq={}
        for num in nums:
            freq[num]= freq.get(num,0)+1
        ans=[]
        for i in range(k):
            key = max(freq, key = freq.get)
            ans.append(key)
            freq.pop(key)
        return ans

