class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        while l<r
        [3,4,5,6,1,2]
        l=0
        r=5
        m=2
        5>2
        l=m+1
        [3,5]
        m=4
        1<2
        r=m
        [3,4]
        m=3
        6>2
        m=l+1
        [4,4]
        return nums[l]



        '''
        l=0
        n=len(nums)
        h=n-1
        while l<h:
            mid=l+(h-l)//2
            if nums[mid]>nums[h]:
                l=mid+1
            else:
                h=mid
        return nums[l]
            











