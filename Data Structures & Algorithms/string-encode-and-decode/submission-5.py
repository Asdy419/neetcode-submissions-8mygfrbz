class Solution:

    def encode(self, strs: List[str]) -> str:
        new_list = []
        for i in strs:
            new_list.append(i)
            new_list.append('漢')
        return ''.join(new_list)

    def decode(self, s: str) -> List[str]:
        words = []
        word = ""

        for i in s:
            if i == '漢':
                words.append(word)
                word = ""
                continue
            word += i
        return words