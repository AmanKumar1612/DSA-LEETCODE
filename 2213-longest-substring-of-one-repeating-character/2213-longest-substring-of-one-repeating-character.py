class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.s = list(s)
        # 4 * n capacity ensures safe node indexing for segment trees
        self.max_len = [0] * (4 * self.n)
        self.pref_len = [0] * (4 * self.n)
        self.suff_len = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1)

    def merge(self, node: int, l: int, r: int, mid: int):
        left_node = 2 * node
        right_node = 2 * node + 1
        left_len = mid - l + 1
        right_len = r - mid

        # Base non-overlapping lengths
        self.pref_len[node] = self.pref_len[left_node]
        self.suff_len[node] = self.suff_len[right_node]
        self.max_len[node] = max(self.max_len[left_node], self.max_len[right_node])

        # Merge across boundary if characters match
        if self.s[mid] == self.s[mid + 1]:
            # Extend prefix if left range is completely uniform
            if self.pref_len[left_node] == left_len:
                self.pref_len[node] = left_len + self.pref_len[right_node]

            # Extend suffix if right range is completely uniform
            if self.suff_len[right_node] == right_len:
                self.suff_len[node] = right_len + self.suff_len[left_node]

            # Check boundary merge length
            self.max_len[node] = max(
                self.max_len[node],
                self.suff_len[left_node] + self.pref_len[right_node]
            )

    def build(self, node: int, l: int, r: int):
        if l == r:
            self.max_len[node] = 1
            self.pref_len[node] = 1
            self.suff_len[node] = 1
            return
        
        mid = (l + r) // 2
        self.build(2 * node, l, mid)
        self.build(2 * node + 1, mid + 1, r)
        self.merge(node, l, r, mid)

    def update(self, node: int, l: int, r: int, idx: int, char: str):
        if l == r:
            self.s[idx] = char
            return
        
        mid = (l + r) // 2
        if idx <= mid:
            self.update(2 * node, l, mid, idx, char)
        else:
            self.update(2 * node + 1, mid + 1, r, idx, char)
            
        self.merge(node, l, r, mid)


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        st = SegmentTree(s)
        ans = []
        
        for char, idx in zip(queryCharacters, queryIndices):
            st.update(1, 0, len(s) - 1, idx, char)
            # Root node (index 1) maintains max length for full range [0, n - 1]
            ans.append(st.max_len[1])
            
        return ans