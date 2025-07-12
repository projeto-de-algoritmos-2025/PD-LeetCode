from functools import cache

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        @cache
        def dp(i: int, tempo: int) -> int:
            if i == len(satisfaction):
                return 0

            nao_usa = dp(i + 1, tempo)
            usa = satisfaction[i] * tempo + dp(i + 1, tempo + 1)

            return max(usa, nao_usa)

        return dp(0, 1)
