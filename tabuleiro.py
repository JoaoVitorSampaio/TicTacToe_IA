# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [
            [Tabuleiro.DESCONHECIDO for _ in range(3)]
            for _ in range(3)
        ]

    def tem_campeao(self, debug=False):
        if debug:
            print("\ntabuleiro:")
            for linha in self.matriz:
                print(linha)

        # Verificar linhas e colunas
        for i in range(3):
            # Linhas
            if sum(self.matriz[i]) == Tabuleiro.JOGADOR_0 * 3:
                return Tabuleiro.JOGADOR_0
            if sum(self.matriz[i]) == Tabuleiro.JOGADOR_X * 3:
                return Tabuleiro.JOGADOR_X

            # Colunas
            soma_coluna = sum(self.matriz[j][i] for j in range(3))
            if soma_coluna == Tabuleiro.JOGADOR_0 * 3:
                return Tabuleiro.JOGADOR_0
            if soma_coluna == Tabuleiro.JOGADOR_X * 3:
                return Tabuleiro.JOGADOR_X

        # Diagonal principal
        diag_principal = sum(self.matriz[i][i] for i in range(3))
        if diag_principal == Tabuleiro.JOGADOR_0 * 3:
            return Tabuleiro.JOGADOR_0
        if diag_principal == Tabuleiro.JOGADOR_X * 3:
            return Tabuleiro.JOGADOR_X

        # Diagonal secundária
        diag_secundaria = sum(self.matriz[i][2 - i] for i in range(3))
        if diag_secundaria == Tabuleiro.JOGADOR_0 * 3:
            return Tabuleiro.JOGADOR_0
        if diag_secundaria == Tabuleiro.JOGADOR_X * 3:
            return Tabuleiro.JOGADOR_X

        return Tabuleiro.DESCONHECIDO
