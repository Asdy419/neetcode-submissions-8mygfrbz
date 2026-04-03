class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {num: 0 for num in s}
        t_map = {num: 0 for num in t}

        for i_s in s:
            s_map[i_s] += 1

        for i_t in t:
            t_map[i_t] += 1
        
        print(s_map, t_map)
        if s_map == t_map:
            return True

        
        return False
