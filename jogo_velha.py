# -*- coding: utf-8 -*-
from tabuleiro_screen import TabuleiroScreen
from tabuleiro import Tabuleiro
from jogador import Jogador
from jogador_ia import JogadorIA
from jogador_humano import JogadorHumano

class JogoVelha:
    def __init__(self):
        self.screen = TabuleiroScreen()
        self.tabuleiro = Tabuleiro()

        # Jogadores: humano X começa (índice 0), IA 0 (índice 1)
        self.jogadores = [
            JogadorHumano(self.tabuleiro, self.screen.buttons, Tabuleiro.JOGADOR_X),
            JogadorIA(self.tabuleiro, Tabuleiro.JOGADOR_0)
        ]

        self.id_jogador_corrente = 0  # começa pelo humano (X)
        self.jogador_corrente = self.jogadores[self.id_jogador_corrente]

    def troca_jogador(self):
        self.id_jogador_corrente = (self.id_jogador_corrente + 1) % 2
        self.jogador_corrente = self.jogadores[self.id_jogador_corrente]

    def wait_quit_event(self):
        self.screen.wait_quit_event()

    def acabou_jogo(self):
        vencedor = self.tabuleiro.tem_campeao()
        if vencedor == Tabuleiro.JOGADOR_X:
            self.screen.resultado_txt = "X vencedor!"
            return True
        elif vencedor == Tabuleiro.JOGADOR_0:
            self.screen.resultado_txt = "0 vencedor!"
            return True
        return False

    def start(self):
        acabou_jogo = False
        contador = 0

        while True:
            x, y = self.jogador_corrente.getJogada()
            self.screen.update_text_button(x, y, self.jogador_corrente.tipo)
            self.tabuleiro.matriz[x][y] = self.jogador_corrente.tipo

            contador += 1

            acabou_jogo = self.acabou_jogo()

            if (not acabou_jogo) and (contador == 9):
                self.screen.resultado_txt = "Deu velha!"
                acabou_jogo = True

            self.screen.desenha_tabuleiro()

            if acabou_jogo:
                break

            self.troca_jogador()
