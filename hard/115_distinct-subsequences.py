import math

class Solution:
    def numDistinct(self, texto_s: str, texto_t: str) -> int:
        n_s, n_t = len(texto_s), len(texto_t)
        INF_NEGATIVO = -10**9
        pontuacao = [[INF_NEGATIVO] * (n_t + 1) for _ in range(n_s + 1)]
        contagem = [[0] * (n_t + 1) for _ in range(n_s + 1)]
        pontuacao[0][0] = 0
        contagem[0][0] = 1

        for i in range(1, n_s + 1):
            pontuacao[i][0] = 0
            contagem[i][0] = 1

        for i in range(1, n_s + 1):
            for j in range(1, n_t + 1):
                opcao_ignorar = pontuacao[i - 1][j]
                opcao_corresponder = (
                    pontuacao[i - 1][j - 1] + 1
                    if texto_s[i - 1] == texto_t[j - 1]
                    else INF_NEGATIVO
                )
                melhor = opcao_ignorar if opcao_ignorar > opcao_corresponder else opcao_corresponder
                pontuacao[i][j] = melhor

                qtd = 0
                if opcao_ignorar == melhor:
                    qtd += contagem[i - 1][j]
                if texto_s[i - 1] == texto_t[j - 1] and opcao_corresponder == melhor:
                    qtd += contagem[i - 1][j - 1]
                contagem[i][j] = qtd

        return contagem[n_s][n_t]
