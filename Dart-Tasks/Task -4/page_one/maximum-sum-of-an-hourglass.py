class Solution:
    def maxSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        sums = 0
        def maxim(i,j):
            return sum(mat[i-1][j-1:j+2]) + mat[i][j] + sum(mat[i+1][j-1:j+2])
        for i in range(1,n-1):
            
            for j in range(1,m-1):
                sums = max(sums, maxim(i,j))
        return sums

                