class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sIdx = len(s) - 1
        tIdx = len(t) - 1

        sSkip = 0
        tSkip = 0
        while sIdx >= 0 or tIdx >= 0:
            while sIdx >= 0:
                if s[sIdx] == "#":
                    sSkip += 1
                    sIdx -= 1
                elif sSkip > 0:
                    sSkip -= 1
                    sIdx -= 1
                else:
                    break

            while tIdx >= 0:
                if t[tIdx] == "#":
                    tSkip += 1
                    tIdx -= 1
                elif tSkip > 0:
                    tSkip -= 1
                    tIdx -= 1
                else:
                    break

            sChar = None if sIdx < 0 else s[sIdx]
            tChar = None if tIdx < 0 else t[tIdx]

            if sChar != tChar:
                return False

            sIdx -= 1
            tIdx -= 1

        return sIdx == tIdx
