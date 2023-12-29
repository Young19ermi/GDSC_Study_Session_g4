class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_coordniate = []
        n = len(points)
        for i in range(n):
            x_coordniate.append(points[i][0])
        x_coordniate.sort()
        
        # for i in range(len(x_coordniate)-1,-1,-1):
        #     diff += x_coordniate[i] - x_coordniate[i-1]
        #     mini = max(diff, mini)
        # return mini
        diff = 0 
        d = []
        mini = float("-inf")
        for i in range(0,len(x_coordniate)-1):
            diff += x_coordniate[i+1] - x_coordniate[i]
            d.append(x_coordniate[i+1] - x_coordniate[i])
            mini = max(diff, mini)
        
        return max(d)





