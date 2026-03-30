# https://leetcode.com/problems/word-break-ii/description/?utm_source=chatgpt.com

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}   

        def dfs(start):
            # 문자열 끝까지 왔으면 문장 1개 완성
            if start == len(s):
                return[""]
            
            # 이미 계산한 위치면 재사용
            if start in memo:
                return memo[start]
            
            res = []

            for word in wordDict:
                if s[start:start + len(word)] == word:
                    tails = dfs(start + len(word))

                    for tail in tails:
                        if tail == "":
                            res.append(word)
                        else:
                            res.append(word + " " + tail)
                        
            memo[start] =res
            return res
        return dfs(0)