class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        map = {}
        maxLen, left = 0, 0

        for right, cur in enumerate(fruits):
            map[cur] = map.get(cur, 0) + 1
            while len(map) > 2:
                count = map.get(fruits[left])
                if count == 1:
                    del map[fruits[left]]
                else:
                    map[fruits[left]] = count - 1
                left += 1
            maxLen = max(maxLen, right - left + 1)

        return maxLen
