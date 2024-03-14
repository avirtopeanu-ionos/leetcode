"""
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

from typing import List
import math


sentinel = b'' # 0 byte value


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) > len(set(nums)):
            return True

        seen = {}
        
        for n in nums:
            if n in seen:
                return True
            seen[n] = sentinel

        return False


if __name__ == "__main__":
    print(Solution().containsDuplicate(
        [1,2,3,1]
    ))
    print(Solution().containsDuplicate(
        [1,2,3,4]
    ))
    print(Solution().containsDuplicate(
        [1,1,1,3,3,4,3,2,4,2]
    ))