class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mini = {}
        for i in t:
            mini[i]= mini.get(i, 0) + 1
        
        compare = {}

        

        anchor = 0
        searcher = 0

        record_a, record_s = 0, len(s) + 1


        valid = False


        need = len(mini)
        have = 0

        while searcher < len(s) or need == have:
            if not need == have:
                compare[s[searcher]] = compare.get(s[searcher], 0) + 1
                if s[searcher] in mini and compare[s[searcher]] == mini[s[searcher]]:
                    have+=1
                searcher += 1
            else:
                if s[anchor] in mini and compare[s[anchor]] == mini[s[anchor]]:
                    have-=1
                if searcher - anchor < record_s - record_a:
                    record_a, record_s = anchor, searcher
                if compare[s[anchor]] > 1:
                    compare[s[anchor]] -= 1
                else:
                    del compare[s[anchor]]
                anchor += 1
        
        if record_s == len(s) + 1:
            return ""
        else:
            return s[record_a:record_s]
