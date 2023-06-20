class Solution:
    def swap(self, res: [], left: int, right: int):
        while left < right:
            tmp = res[left]
            res[left] = res[right]
            res[right] = tmp
            left += 1
            right -= 1

    def reverseWords(self, s: str) -> str:
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] == ' ':
                start += 1
            else:
                break

        while start < end:
            if s[end] == ' ':
                end -= 1
            else:
                break

        res = []

        while end >= start:
            if s[end] == ' ' and res[len(res) - 1] == ' ':
                ...
            else:
                res.append(s[end])
            end -= 1

        start = 0
        for i in range(0, len(res)):
            if res[i] == ' ':
                end = i - 1
                self.swap(res, start, end)
                start = i + 1

        self.swap(res, start, len(res) - 1)

        return ''.join(res)


print(Solution().reverseWords("the sky is blue"))
