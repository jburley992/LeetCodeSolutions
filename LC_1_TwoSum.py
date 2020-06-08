    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Concepts:
        
        # Arrays
        # Hash Tables
        # Mathematical Intuition
        
        # Why:
        # Fortune 500s ask it
        
        # [2, 2, 4]
        
        # Naive:
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[i + 1::]):
                if x + y == target:
                    return [i, i + j + 1]
        
        # Optimal:
        memo = {}
        
        for i, x in enumerate(nums):
            complement = target - x
            if complement in memo:
                return [i, memo[complement]]
            memo[x] = i