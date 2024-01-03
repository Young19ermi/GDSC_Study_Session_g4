class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:
        nums.sort()
        res = 0
        right = len(nums) - 1
        left = 0
        while left <= right:
            if nums[left] + nums[right] <= limit:
                left += 1
            res += 1
            right -= 1
        return res
        """
        for right in range(1,len(nums)):
            total = nums[left] + nums[right]
            while 
            if total > limit:
                total-=nums[left]
                left += 1
            elif total == limit or total < limit:
                res += 1
                right += 1
                left +=1
                if res == limit:
                    break
        return res
        
        nums.sort()
        res = 0
        left = 0 
        right = len(nums) -1
        while left < right:
            total = nums[left] + nums[right]
            if total > limit:
                right -=1
            elif total < = limit:
                res += 1
                right -= 1
                if res == limit:
                    break
        return res            

        """