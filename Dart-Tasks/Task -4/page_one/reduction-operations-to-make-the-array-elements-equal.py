class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        num = list(set(nums))
        num.sort()
        countme = Counter(nums)
        print(countme)
        # for n in nums:
        #     countme[n]= nums.count(n)
        count = 0
        for i in range(len(num)):
            count += i * countme[num[i]]
        return count





