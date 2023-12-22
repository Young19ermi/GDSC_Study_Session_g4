class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        x = arr[0]
        n = len(arr)
        maxim = max(arr)
        y = arr.index(maxim)
        if y == n-1 or y == 0:
            return False
        
        
        # for i in range(y+1):
        #     if arr[i] == arr[i+1]:
        #         return False    
        #     elif x > arr[i]:
        #         return False
        #     elif arr == sorted(arr):
        #         return False
        # return False
             
        # maxim = max(arr)
        # y = arr.index(maxim)
        # i = 0
        # while i < y:
        #     if arr[i] > arr[i+1]:
        #         return False

        for i in range(y):
            if arr[i] >= arr[i+1]:
                return False
        for i in range(y, len(arr)-1):
            if arr[i] <= arr[i+1]:
                return False
       
        return True



        

        