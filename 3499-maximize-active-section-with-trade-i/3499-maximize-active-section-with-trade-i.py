class Solution:

    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        zeros = [len(x) for x in f"1{s}1".split("1") if x]
        max_delta = max(
            [zeros[i] + zeros[i + 1] for i in range(len(zeros) - 1)], default=0
        )
        return s.count("1") + max_delta