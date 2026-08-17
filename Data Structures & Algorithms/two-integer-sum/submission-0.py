class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in nums:
                if nums.index(difference) == i:
                    continue
                answer = [i, nums.index(difference)]
                return sorted(answer)