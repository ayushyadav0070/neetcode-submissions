class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        for i in rsnge(nums)
            i->0:
            preMul[i]=1
            i->!0:
            preMul[i]=preMul[i-1]*(i-1)
        for i in rsnge(nums)
            i->n-1:
            postMul[i]=1
            i->!0:
            postMul[i]=postMul[i+1]*(i+1)
        ans=[]
        for i in range(nums):
            ans[i]=preMul[i]*postMul[i]


        '''
        ans=[1]*len(nums)
        n= len(nums)
        premul = [1] * n
        postmul = [1] * n
        for i in range(n):
            if i==0:
                premul[i]=1
            if i!=0:
                premul[i]=premul[i-1]*nums[i-1]
        for i in range(n-1,-1,-1):
            if i==n-1:
                postmul[i]=1
            if i!=n-1:
                postmul[i]= postmul[i+1]*nums[i+1]
        for i in range(n):
            ans[i]=(premul[i]*postmul[i])
        return ans
            
