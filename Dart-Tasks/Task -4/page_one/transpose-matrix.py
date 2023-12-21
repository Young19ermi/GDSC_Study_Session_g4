class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        ans = []
     
        for j in range(len(matrix[0])):
            temp = []
            for i in range(len(matrix)):
                temp.append(matrix[i][j])
               
            ans.append(temp)
        return ans       
                
        