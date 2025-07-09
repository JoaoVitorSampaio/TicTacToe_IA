# -*- coding: utf-8 -*-

from typing import Optional, Tuple
from tabuleiro import Tabuleiro

class Jogador:
    def __init__(self, tabuleiro: Tabuleiro, tipo: int):
        self.tabuleiro = tabuleiro
        self.tipo = tipo

    def getJogada(self) -> Optional[Tuple[int, int]]:
        pass
