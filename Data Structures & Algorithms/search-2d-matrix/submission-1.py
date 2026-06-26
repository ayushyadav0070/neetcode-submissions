class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==0:
            return False
        l=0
        m=len(matrix)
        n=len(matrix[0])
        h=m*n-1
        while l<=h:
            mid = l+(h-l)//2
            r=mid//n
            c=mid%n
            e=matrix[r][c]
            if e==target:
                return True
            elif e<target:
                l=mid+1
            else:
                h=mid-1
        return False