class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict  = [0] * 26

        for c in magazine:
            dict[ord(c) - ord('a')] += 1

        for c in ransomNote:
            key = ord(c) - ord('a')
            if dict[key] == 0:
                return False

            dict[key] -= 1

        return True