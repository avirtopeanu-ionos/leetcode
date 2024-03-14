
"""
Input:
    nums = [2,7,11,15]
    target = 9

Output:
    [0,1] (indices of nums that add up to target)
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {}
        for idx, i in enumerate(nums):
            want = target - i
            if want in num_to_idx:
                return [num_to_idx[want], idx]
            num_to_idx[i] = idx

def main():
    sol = Solution()
    r = sol.twoSum([2, 7, 11, 15], 9)
    print(r) 

if __name__ == "__main__":
    main()
