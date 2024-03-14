class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mostRightPosOfChar = {}
        left = 0
        maxLength = 0

        for right, char in enumerate(s):
            if char in mostRightPosOfChar and mostRightPosOfChar[char] >= left:
                # Second time we encountered this character.
                # Move our left tracker to the previous encounter + 1
                left = mostRightPosOfChar[char] + 1
            mostRightPosOfChar[char] = right
            maxLength = max(maxLength, right - left + 1)

        return maxLength


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
    print(Solution().lengthOfLongestSubstring("aab"))
    print(Solution().lengthOfLongestSubstring("vdvf"))

