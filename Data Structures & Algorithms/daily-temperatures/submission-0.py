class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pending = []

        answers = [0] * len(temperatures)
        for i, v in enumerate(temperatures):
            while pending and v > temperatures[pending[-1]]:
                j = pending.pop()
                answers[j] = i-j
            pending.append(i)
        return answers