class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = nums[0]
        b = float("inf")
        # if nums[::-1] == sorted(nums):
        #     return False
        for c in range(1,len(nums)):
            if a > nums[c]:
                a = nums[c]
            elif nums[c] > a and nums[c] < b:
                b = nums[c]
            elif nums[c] > b:
                return True
        return False