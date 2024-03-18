def get_counts(s: str) -> dict[str, int]:
    ks = {}
    for c in s:
        if c not in ks:
            ks[c] = 0
        ks[c] += 1

    return ks


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return get_counts(s) == get_counts(t)

if __name__ == "__main__":
    print(Solution().isAnagram("ananas", "nanasa"))