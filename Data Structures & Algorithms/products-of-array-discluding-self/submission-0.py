from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Step 1: Initialize output array with 1s
        # output[i] will eventually store product except nums[i]
        output = [1] * n

        # Step 2: Compute prefix products (left side)
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # Step 3: Compute suffix products (right side)
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output
