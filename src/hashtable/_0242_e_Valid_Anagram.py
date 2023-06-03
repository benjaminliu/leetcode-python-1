class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = [0] * 26

        for c in s:
            map[ord(c) - ord('a')] += 1

        for c in t:
            map[ord(c) - ord('a')] -= 1

        for i in range(26):
            if map[i] != 0:
                return False

        return True
