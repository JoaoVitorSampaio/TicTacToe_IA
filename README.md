# 🎮 Jogo da Velha com IA

## 📚 Visão Geral

Este repositório contém a implementação prática do **Jogo da Velha (Tic-Tac-Toe)** desenvolvida para a disciplina **Estrutura de Dados** na **Universidade Federal da Paraíba**.  

O projeto inclui:

- **Interface gráfica** desenvolvida com **Pygame** 🎨  
- Implementação de um **Jogador Inteligente (IA)** baseado em regras estratégicas  
- Partida entre **Humano x IA** ou **IA x IA**  
- Código modular e bem estruturado

---

## 🎯 Objetivos

- ✅ Praticar conceitos de Estrutura de Dados aplicados a jogos  
- ✅ Desenvolver raciocínio lógico e estratégico  
- ✅ Criar um sistema especialista capaz de jogar de forma inteligente  
- ✅ Implementar interface gráfica interativa  

---

## 🤖 Inteligência Artificial

A IA implementa as seguintes **regras estratégicas** (em ordem de prioridade):

1. **R1:** Se o jogador ou o oponente tiver duas marcações em sequência, marque o quadrado restante para vencer ou bloquear.  
2. **R2:** Se houver uma jogada que crie duas sequências de duas marcações, execute-a.  
3. **R3:** Se o quadrado central estiver livre, ocupe-o.  
4. **R4:** Se o oponente tiver marcado um dos cantos, ocupe o canto oposto.  
5. **R5:** Se houver algum canto livre, ocupe-o.  
6. **R6:** Caso contrário, escolha qualquer casa livre aleatoriamente.  

Estas regras tornam a IA **competitiva e difícil de vencer**. 🔥

---

## 💻 Linguagens e Tecnologias

- **Python 3** → linguagem principal  
- **Pygame** → interface gráfica e interação  
- **VS Code** → ambiente de desenvolvimento  

<div style="display: inline_block"><br>
  <img align="center" alt="Python" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" />
  <img align="center" alt="Pygame" height="50" width="50" src="![image](https://github.com/user-attachments/assets/6c905354-d3c1-4aa5-bce3-3d61b9f64572)" />
  <img align="center" alt="VSCode" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" />
</div>

---

## 🛠️ Como Rodar

### 1. Clone o Repositório

```
git clone https://github.com/JoaoVitorSampaio/TicTacToe_IA.git
cd TicTacToe_IA
```

### 2. Crie um Ambiente Virtual (opcional, mas recomendado)

Windows:
``` 
python -m venv venv
.\venv\Scripts\activate
```

Linux/macOS: 
``` 
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as Dependências
```
pip install pygame
```

### 4. Execute o Jogo
```
python main.py
```
