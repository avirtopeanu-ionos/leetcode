from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in ans:
                ans[sorted_word].append(word)
            else:
                ans[sorted_word] = [word]
        return list(ans.values())


if __name__ == "__main__":
    print(Solution().groupAnagrams(
        ["eat","tea","tan","ate","nat","bat"]
    ))
    print(Solution().groupAnagrams(
        ["eat","eat"]
    ))