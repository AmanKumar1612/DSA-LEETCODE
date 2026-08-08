class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)
        
        # last_pos[j] = maximum starting index in word1 such that
        # word2[j:] is a subsequence of word1[last_pos[j]:]
        last_pos = [-1] * m
        
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last_pos[j] = i
                j -= 1
        
        result = []
        j = 0
        changed = False
        
        for i in range(n):
            if j == m:
                break
                
            is_match = word1[i] == word2[j]
            can_change = not changed and (j + 1 == m or i + 1 <= last_pos[j + 1])
            
            if is_match or can_change:
                if not is_match:
                    changed = True
                result.append(i)
                j += 1
                
        return result if len(result) == m else []