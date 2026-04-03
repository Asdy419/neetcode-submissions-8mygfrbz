class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        annograms = []
        return_list = []

        for annogram in strs:
            entry = {character: 0 for character in annogram}
            for character in annogram:
                entry[character] += 1
            
            if entry not in annograms:
                annograms.append(entry)
                return_list.append([annogram])
            
            else:
                place = annograms.index(entry)
                return_list[place].append(annogram)
            
        return return_list