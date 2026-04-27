class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = {} # keep track of freq
        bucket = [[] for _ in range(len(nums) + 1)] 
        # create a bucket that has max index value 
        # of len(nums) + 1

        for number in nums: # update counts in the dict
            freq_count[number] = 1 + freq_count.get(number, 0)

        for number, count_val in freq_count.items(): # update bucket
            # index of bucket is equal to count vals of max len(num)
            bucket[count_val].append(number)

        result = []
        for count_val in range(len(bucket) - 1, 0, -1):
            for num in bucket[count_val]:
                result.append(num)
                if len(result) == k:
                    return result
