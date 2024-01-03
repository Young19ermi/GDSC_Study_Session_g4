class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        sum = 0
        count = 0
        costs.sort()
        if costs[0] > coins:
            return 0
        for i in range(len(costs)):
            sum += costs[i]
            if sum > coins:
                break
            else:
                count += 1
            #count += 1
            
        return count 
        #return count

#             if costs[0] > coins:
#                 return 0
#                 break
#             elif sum < coins:
#                 sum += costs[i]
#                 count += 1
#             else:
#                 pass
                
#         return count


# [1,1,2,3,5,6]
 # elif sum == coins:
            #     return count
            # elif i == len(costs)-1 and sum < coins:
            #     return i+1        
            

        