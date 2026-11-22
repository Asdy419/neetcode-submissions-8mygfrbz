class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        anchor = 0
        searcher = 0

        dictionary = {}
        for i in s1:
            dictionary[i] = dictionary.get(i, 0) + 1
        
        window_dict = {}

        while searcher < len(s2):
            if sum(window_dict.values()) < len(s1):
                window_dict[s2[searcher]] = window_dict.get(s2[searcher], 0) + 1
                searcher += 1

            else:
                if window_dict[s2[anchor]] > 1:
                    window_dict[s2[anchor]] -= 1
                else:
                    del window_dict[s2[anchor]]
                anchor += 1
            
            if window_dict == dictionary:
                return True

        return False
