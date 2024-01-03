class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # the_pairs = 0
        # nums.sort()
        # count = filter(list(nums, key == lambda x: x[j] + x[i] < target for (i,j) in nums))
        # return count
        #nums.sort()
        
        the_res = set()
        for i in range(0,len(nums)):
            curr = nums[i]
            for j in range(1, len(nums)):
                if curr + nums[j] < target and i<j:
                    the_res.add((i,j))  
                   
        
        return len(the_res)

