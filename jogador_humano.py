# -*- coding: utf-8 -*-
import pygame
import sys
from typing import Tuple

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorHumano(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, _buttons: list, tipo: int):
        super().__init__(tabuleiro, tipo)
        self.buttons = _buttons

    def getJogada(self) -> Tuple[int, int]:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for l in range(3):
                        for c in range(3):
                            b = self.buttons[l][c]
                            if b.rect.collidepoint(pygame.mouse.get_pos()):
                                if self.tabuleiro.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                                    return (l, c)
