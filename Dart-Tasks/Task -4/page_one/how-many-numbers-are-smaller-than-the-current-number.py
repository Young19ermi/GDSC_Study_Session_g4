class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 101  # Since the constraints specify that nums[i] will be between 0 and 100
        for num in nums:
            count[num] += 1
        for i in range(1, 101):
            count[i] += count[i-1]
        res = []
        for num in nums:
            if num == 0:
                res.append(0)
            else:
                res.append(count[num-1])
        return res






        """
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        sorted_nums = sorted(nums)
        rank = {}
        prev = sorted_nums[0]
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in rank:
                rank[sorted_nums[i]] = i
        res = []
        for num in nums:
            res.append(rank[num])
        return res


        
        count = {}
        for i in range(0,len(nums)-1):
            for j in range(1, len(nums)-1):
                if nums[i] < nums[j]:
                    count[nums[j]] += 1
                    i+=1
                else:
                    count[nums[i]] += 1
                    j+=1
            for val in count.values():
                res= []
                res.append(val)
        return res
        """




        