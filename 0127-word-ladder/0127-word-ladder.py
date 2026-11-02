from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        s=set(wordList)
        if endWord not in s:
            return 0
        queue=deque([(beginWord,1)])
        alpha='abcdefghijklmnopqrstuvwxyz'
        while queue:
            word,step=queue.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                fl=word[:i]
                ll=word[i+1:]
                for ch in alpha:
                    nw=fl+ch+ll
                    if nw in s:
                        s.remove(nw)
                        queue.append((nw,step+1))
        return 0