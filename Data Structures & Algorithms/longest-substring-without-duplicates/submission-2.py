class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        anchor = 0
        searcher = 0

        found = set()
        longest = 0
        while searcher < len(s):
            if s[searcher] not in found:
                found.add(s[searcher])
                searcher+=1
            else:
                found.remove(s[anchor])
                anchor +=1
            longest = max(longest, len(found))
        return longest


