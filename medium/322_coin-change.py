class Solution(object):
    def coinChange(self, moedas, valorDesejado):
        dp = [float('2147483648')] * (valorDesejado + 1)
        dp[0] = 0

        for m in moedas:
            for x in range(m, valorDesejado + 1):
                dp[x] = min(dp[x], dp[x - m] + 1)

        return dp[valorDesejado] if dp[valorDesejado] != float('2147483648') else -1


solucao = Solution()
moedas = list(map(int, input("").split(",")))
valorDesejado = int(input(""))

resultado = solucao.coinChange(moedas, valorDesejado)
print(resultado)