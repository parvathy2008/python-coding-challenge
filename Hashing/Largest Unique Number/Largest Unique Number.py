from collections import defaultdict
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        counter=defaultdict(int)
        for i in nums:
            counter[i] = counter[i]+1
        result =-1
        for num, count in counter.items():
            if count == 1:
                result = max(result, num)
        return result
