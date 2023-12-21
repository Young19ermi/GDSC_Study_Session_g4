class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        hash = defaultdict(list)
        for i in range(len(mat)):
            
            for j in range(len(mat[0])):
                hash[i+j].append(mat[i][j])
        temp = []
        for item in hash.keys():
            if item % 2 == 0:
                while hash[item]: # cause the item needs not to be empty
                    temp.append(hash[item].pop())
            else:
                for val in hash[item]:
                    temp.append(val)
        
        return temp
# pattern = defaultdict(list)

#         for i in range(len(mat)):
#             for j in range(len(mat[i])):
#                 pattern[i+j].append(mat[i][j])
#         ans = []
#         for k in pattern.keys():
#             if k % 2 == 0:
#                 while pattern[k]:
#                     ans.append(pattern[k].pop()) 
#             else:
#                 for v in pattern[k]:
#                     ans.append(v)
        
#         return ans
            
                
           

