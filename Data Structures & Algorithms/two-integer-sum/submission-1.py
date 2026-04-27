class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checkSum = {}

        for index, value in enumerate(nums):
            complement = target - value

            if complement in checkSum:
                return [checkSum[complement], index]
                
            checkSum[value] = index

        return []