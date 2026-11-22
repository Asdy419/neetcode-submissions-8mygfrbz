class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        DICT = {}


        anchor = 0
        searcher = 0
        best = 0
        longest = 0
        while searcher < len(s):
            if searcher - anchor - longest > k:
                DICT[s[anchor]] -= 1
                anchor += 1
            else:
                DICT[s[searcher]] = DICT.get(s[searcher], 0) + 1
                searcher += 1

            longest = max(DICT.values(), default = 0)
            if searcher - anchor - longest <= k:
                best = max(best, searcher - anchor)

        return best