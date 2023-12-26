class Solution(object):
    def sortPeople(self, names, arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    names[j], names[j+1] = names[j+1], names[j]
        return names
        # n = len(nums)         
        # for i in range(n-1):             
        #     for j in range(0, n-i-1):                 
        #         if nums[j] > nums[j+1]:                     
        #             nums[j],nums[j+1] = nums[j+1],nums[j]                                  
        #     return nums

        # res= []
        # maximum = max(array)
        # minimum = min(array)
        # range = maximum - minimum  
        # print(range)
        # countme = [0] * range
        # for num in array:
        #     countme[num] += 1
        # for i in range(len(countme))
        
        # # for i in range(len(array)-1):
        # #     countme[array[i]] += 1
        # print(countme)

