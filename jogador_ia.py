# -*- coding: utf-8 -*-
from random import randint
from typing import Optional, Tuple

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, tipo: int):
        super().__init__(tabuleiro, tipo)

    def getJogada(self) -> Optional[Tuple[int, int]]:
        matriz = self.tabuleiro.matriz

        lista = []
        for l in range(3):
            for c in range(3):
                if matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    lista.append((l, c))

        # R1: Se houver linha, coluna ou diagonal com duas marcas e uma casa vazia
        for emptySpot in lista:
            x, y = emptySpot

            # Horizontal
            row = [matriz[x][i] for i in range(3)]
            if (row.count(Tabuleiro.JOGADOR_0) == 2 or row.count(Tabuleiro.JOGADOR_X) == 2) and \
                row.count(Tabuleiro.DESCONHECIDO) == 1:
                return emptySpot

            # Vertical
            col = [matriz[i][y] for i in range(3)]
            if (col.count(Tabuleiro.JOGADOR_0) == 2 or col.count(Tabuleiro.JOGADOR_X) == 2) and \
                col.count(Tabuleiro.DESCONHECIDO) == 1:
                return emptySpot

            # Diagonal principal
            if x == y:
                diag = [matriz[i][i] for i in range(3)]
                if (diag.count(Tabuleiro.JOGADOR_0) == 2 or diag.count(Tabuleiro.JOGADOR_X) == 2) and \
                    diag.count(Tabuleiro.DESCONHECIDO) == 1:
                    return emptySpot

            # Diagonal secundária
            if x + y == 2:
                diag = [matriz[i][2 - i] for i in range(3)]
                if (diag.count(Tabuleiro.JOGADOR_0) == 2 or diag.count(Tabuleiro.JOGADOR_X) == 2) and \
                    diag.count(Tabuleiro.DESCONHECIDO) == 1:
                    return emptySpot

        # R2: Se houver uma jogada que crie duas possibilidades de vitória (duas ameaças)
        for emptySpot in lista:
            x, y = emptySpot

            # Testa colocar a peça temporariamente
            matriz[x][y] = Tabuleiro.JOGADOR_0

            threats = 0

            # Conta se há linhas com 2 peças e 1 espaço livre após a jogada

            # Horizontal
            row = [matriz[x][i] for i in range(3)]
            if row.count(Tabuleiro.JOGADOR_0) == 2 and row.count(Tabuleiro.DESCONHECIDO) == 1:
                threats += 1

            # Vertical
            col = [matriz[i][y] for i in range(3)]
            if col.count(Tabuleiro.JOGADOR_0) == 2 and col.count(Tabuleiro.DESCONHECIDO) == 1:
                threats += 1

            # Diagonal principal
            if x == y:
                diag = [matriz[i][i] for i in range(3)]
                if diag.count(Tabuleiro.JOGADOR_0) == 2 and diag.count(Tabuleiro.DESCONHECIDO) == 1:
                    threats += 1

            # Diagonal secundária
            if x + y == 2:
                diag = [matriz[i][2 - i] for i in range(3)]
                if diag.count(Tabuleiro.JOGADOR_0) == 2 and diag.count(Tabuleiro.DESCONHECIDO) == 1:
                    threats += 1

            # Desfaz a jogada temporária
            matriz[x][y] = Tabuleiro.DESCONHECIDO

            if threats >= 2:
                return emptySpot

        # R3: Se o centro estiver livre
        if matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)

        # R4: Se oponente marcou canto, marcar canto oposto
        if matriz[0][0] == Tabuleiro.JOGADOR_X and matriz[2][2] == Tabuleiro.DESCONHECIDO:
            return (2, 2)
        if matriz[0][2] == Tabuleiro.JOGADOR_X and matriz[2][0] == Tabuleiro.DESCONHECIDO:
            return (2, 0)
        if matriz[2][0] == Tabuleiro.JOGADOR_X and matriz[0][2] == Tabuleiro.DESCONHECIDO:
            return (0, 2)
        if matriz[2][2] == Tabuleiro.JOGADOR_X and matriz[0][0] == Tabuleiro.DESCONHECIDO:
            return (0, 0)

        # R5: Marcar um canto vazio
        lista_de_cantos = [(0, 0), (2, 2), (0, 2), (2, 0)]
        cantos_vazios = [pos for pos in lista_de_cantos if matriz[pos[0]][pos[1]] == Tabuleiro.DESCONHECIDO]

        if cantos_vazios:
            return cantos_vazios[randint(0, len(cantos_vazios)-1)]

        # R6: Escolher posição aleatória
        if lista:
            return lista[randint(0, len(lista)-1)]

        return None
        # Se não houver jogada possível, retorna None
        # Isso pode acontecer se o tabuleiro estiver cheio ou se não houver jogadas válidas