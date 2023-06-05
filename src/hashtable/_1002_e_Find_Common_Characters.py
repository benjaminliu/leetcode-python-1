from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        map = [0] * 26
        for c in words[0]:
            map[ord(c) - ord('a')] += 1

        for i in range(1, len(words)):
            newMap = [0] * 26

            for c in words[i]:
                newMap[ord(c) - ord('a')] += 1

            for j in range(len(map)):
                if map[j] > newMap[j]:
                    map[j] = newMap[j]

        res = []
        for i in range(len(map)):
            while map[i] > 0:
                res.append(str(chr(i + ord('a'))))
                map[i] -= 1

        return res


words = ["aba", "aca"]
Solution().commonChars(words)
