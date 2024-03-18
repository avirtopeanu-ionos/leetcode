def getMatching(paren: str) -> str:
    if paren == '(':
        return ')'

    if paren == '[':
        return ']'

    if paren == '{':
        return '}'

class Solution:
    def isValid(self, s: str) -> bool:
        seen = []

        for c in s:
            if len(seen) == 0:
                seen.append(c)
                continue

            # Opening? Add to stack
            if c in ['(', '[', '{']:
                seen.append(c)

            # Closing? Pop and check last.
            if c in [')', ']', '}']:
                popped = seen.pop()
                if c != getMatching(popped):
                    return False

        return len(seen) == 0

if __name__ == "__main__":
    print(Solution().isValid("[]()"))
    print(Solution().isValid("[[]"))
    print(Solution().isValid("(]()"))


