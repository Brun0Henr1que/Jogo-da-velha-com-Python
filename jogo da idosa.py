from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys


class Jan(QMainWindow):  # classe que recebe a janela principal
    def __init__(self):  # metodo construtor
        super().__init__()  # herdar superclasse

        # variaveis que são usadas durante o programa
        self.ct = 0
        self.x = 0
        self.OO = 0

        # configurações da janela
        self.base = QWidget()
        self.setFixedSize(760, 800)
        self.setCentralWidget(self.base)
        self.formlayout = QFormLayout()
        self.hlayout = QHBoxLayout()
        self.glayout = QGridLayout()
        self.base.setLayout(self.formlayout)
        self.glayout.setVerticalSpacing(30)
        self.glayout.setHorizontalSpacing(30)

        # fontes
        self.font = QFont()
        self.font.setPixelSize(30)
        self.font.setBold(True)

        self.font_G = QFont()
        self.font_G.setPixelSize(90)
        self.font_G.setBold(True)

        self.font_p = QFont()
        self.font_p.setPixelSize(15)

        # label inicial
        self.label = QLabel("JOGO DA VELHA")
        self.label.setFont(self.font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("background-color: none")
        self.hlayout.addWidget(self.label)

        # adicionando
        self.formlayout.addRow(self.hlayout)
        self.formlayout.addRow(self.glayout)

        # botoes (1 linha)
        self.btn1 = QPushButton("")
        self.btn1.setFixedSize(230, 200)
        self.glayout.addWidget(self.btn1, 1, 1)
        self.btn2 = QPushButton("")
        self.btn2.setFixedSize(230, 200)
        self.glayout.addWidget(self.btn2, 1, 2)
        self.btn3 = QPushButton("")
        self.btn3.setFixedSize(230, 200)
        self.glayout.addWidget(self.btn3, 1, 3)

        # botoes (2 linha)
        self.btn4 = QPushButton("")
        self.btn4.setFixedSize(230, 200)
        self.glayout.addWidget(self.btn4, 2, 1)
        self.btn5 = QPushButton("")
        self.btn5.setFixedSize(230, 200)
        self.glayout.addWidget(self.btn5, 2, 2)
        self.btn6 = QPushButton("")
        self.btn6.setFixedSize(230, 200)
        self.glayout.addWidget(self.btn6, 2, 3)

        # botoes (3 linha)
        self.btn7 = QPushButton("")
        self.btn7.setFixedSize(230, 200)
        self.glayout.addWidget(self.btn7, 3, 1)
        self.btn8 = QPushButton("")
        self.btn8.setFixedSize(230, 200)
        self.glayout.addWidget(self.btn8, 3, 2)
        self.btn9 = QPushButton("")
        self.btn9.setFixedSize(230, 200)
        self.glayout.addWidget(self.btn9, 3, 3)

        # botão reiniciar
        self.btn10 = QPushButton("REINICIAR")
        self.btn10.clicked.connect(self.retry)
        self.glayout.addWidget(self.btn10, 4, 2)

        # lista com botoes
        self.botoes = [self.btn1,
                       self.btn2,
                       self.btn3,
                       self.btn4,
                       self.btn5,
                       self.btn6,
                       self.btn7,
                       self.btn8,
                       self.btn9]

        # usando a lista para definir cor e fonte para os botoes
        for i in range(0, 9):
            self.botoes[i].setStyleSheet("color: black")
            self.botoes[i].setFont(self.font_G)

        # placar
        self.label1 = QLabel('''PLACAR
X: 
O: ''')
        self.glayout.addWidget(self.label1, 4, 1)
        self.label1.setFont(self.font_p)
        self.label1.setStyleSheet("background-color : none")

        # conexão botão-função
        self.btn1.clicked.connect(self.a)
        self.btn2.clicked.connect(self.b)
        self.btn3.clicked.connect(self.c)
        self.btn4.clicked.connect(self.d)
        self.btn5.clicked.connect(self.e)
        self.btn6.clicked.connect(self.f)
        self.btn7.clicked.connect(self.g)
        self.btn8.clicked.connect(self.h)
        self.btn9.clicked.connect(self.i)

    # seção de funções-parametro
    def a(self):
        return self.clicar(self.btn1)

    def b(self):
        return self.clicar(self.btn2)

    def c(self):
        return self.clicar(self.btn3)

    def d(self):
        return self.clicar(self.btn4)

    def e(self):
        return self.clicar(self.btn5)

    def f(self):
        return self.clicar(self.btn6)

    def g(self):
        return self.clicar(self.btn7)

    def h(self):
        return self.clicar(self.btn8)

    def i(self):
        return self.clicar(self.btn9)

# funções clicar e retry
    def clicar(self, b):
        # incrementa o contador
        self.ct += 1
        # seleciona X ou O
        if self.ct % 2 == 1:
            b.setText("X")
        else:
            b.setText("O")
        # Desliga o botao
        b.setEnabled(False)
        # chama a função de checar a vitória
        self.vit()

    def retry(self):
        # zera o contador
        self.ct = 0
        # reinicia os botoes
        for i in range(0, 9):
            self.botoes[i].setText("")
            self.botoes[i].setEnabled(True)
            self.botoes[i].setStyleSheet("color: black")

    #  condição de vitória
    def vit(self):
        # checa se o texto do botão é diferente de "" (vazio)
        if self.btn1.text() != "" and self.btn2.text() != "" and self.btn3.text() != "":
            # checa se os textos são iguais
            if self.btn1.text() == self.btn2.text() and self.btn1.text() == self.btn3.text():
                # desliga os botoes
                for i in range(0, 9):
                    self.botoes[i].setEnabled(False)
                # checa qual player fez o ponto
                if self.btn1.text() == "X":
                    # incrementa o contador de vitórias do X
                    self.x += 1
                else:
                    # incrementa o contador de vitórias do O
                    self.OO += 1
                # chama a função ganhador
                self.ganhador(self.btn1, self.btn2, self.btn3)

        # checa se o texto do botão é diferente de "" (vazio)
        if self.btn4.text() != "" and self.btn5.text() != "" and self.btn6.text() != "":
            # checa se os textos são iguais
            if self.btn4.text() == self.btn5.text() and self.btn4.text() == self.btn6.text():
                # desliga os botoes
                for i in range(0, 9):
                    self.botoes[i].setEnabled(False)
                # checa qual player fez o ponto
                if self.btn4.text() == "X":
                    # incrementa o contador de vitórias do X
                    self.x += 1
                else:
                    # incrementa o contador de vitórias do O
                    self.OO += 1
                # chama a função ganhador
                self.ganhador(self.btn4, self.btn5, self.btn6)

        # checa se o texto do botão é diferente de "" (vazio)
        if self.btn7.text() != "" and self.btn8.text() != "" and self.btn9.text() != "":
            # checa se os textos são iguais
            if self.btn7.text() == self.btn8.text() and self.btn7.text() == self.btn9.text():
                # desliga os botoes
                for i in range(0, 9):
                    self.botoes[i].setEnabled(False)
                # checa qual player fez o ponto
                if self.btn7.text() == "X":
                    # incrementa o contador de vitórias do X
                    self.x += 1
                else:
                    # incrementa o contador de vitórias do O
                    self.OO += 1
                # chama a função ganhador
                self.ganhador(self.btn7, self.btn8, self.btn9)

        # checa se o texto do botão é diferente de "" (vazio)
        if self.btn1.text() != "" and self.btn4.text() != "" and self.btn7.text() != "":
            # checa se os textos são iguais
            if self.btn1.text() == self.btn4.text() and self.btn1.text() == self.btn7.text():
                # desliga os botoes
                for i in range(0, 9):
                    self.botoes[i].setEnabled(False)
                # checa qual player fez o ponto
                if self.btn1.text() == "X":
                    # incrementa o contador de vitórias do X
                    self.x += 1
                else:
                    # incrementa o contador de vitórias do O
                    self.OO += 1
                # chama a função ganhador
                self.ganhador(self.btn1, self.btn4, self.btn7)

        # checa se o texto do botão é diferente de "" (vazio)
        if self.btn2.text() != "" and self.btn5.text() != "" and self.btn8.text() != "":
            # checa se os textos são iguais
            if self.btn2.text() == self.btn5.text() and self.btn2.text() == self.btn8.text():
                # desliga os botoes
                for i in range(0, 9):
                    self.botoes[i].setEnabled(False)
                # checa qual player fez o ponto
                if self.btn2.text() == "X":
                    # incrementa o contador de vitórias do X
                    self.x += 1
                else:
                    # incrementa o contador de vitórias do O
                    self.OO += 1
                # chama a função ganhador
                self.ganhador(self.btn2, self.btn5, self.btn8)

        # checa se o texto do botão é diferente de "" (vazio)
        if self.btn3.text() != "" and self.btn6.text() != "" and self.btn9.text() != "":
            # checa se os textos são iguais
            if self.btn3.text() == self.btn6.text() and self.btn3.text() == self.btn9.text():
                # desliga os botoes
                for i in range(0, 9):
                    self.botoes[i].setEnabled(False)
                # checa qual player fez o ponto
                if self.btn3.text() == "X":
                    # incrementa o contador de vitórias do X
                    self.x += 1
                else:
                    # incrementa o contador de vitórias do O
                    self.OO += 1
                # chama a função ganhador
                self.ganhador(self.btn3, self.btn6, self.btn9)

        # checa se o texto do botão é diferente de "" (vazio)
        if self.btn1.text() != "" and self.btn5.text() != "" and self.btn9.text() != "":
            # checa se os textos são iguais
            if self.btn1.text() == self.btn5.text() and self.btn1.text() == self.btn9.text():
                # desliga os botoes
                for i in range(0, 9):
                    self.botoes[i].setEnabled(False)
                # checa qual player fez o ponto
                if self.btn1.text() == "X":
                    # incrementa o contador de vitórias do X
                    self.x += 1
                else:
                    # incrementa o contador de vitórias do O
                    self.OO += 1
                # chama a função ganhador
                self.ganhador(self.btn1, self.btn5, self.btn9)

        # checa se o texto do botão é diferente de "" (vazio)
        if self.btn3.text() != "" and self.btn5.text() != "" and self.btn7.text() != "":
            # checa se os textos são iguais
            if self.btn3.text() == self.btn5.text() and self.btn3.text() == self.btn7.text():
                # desliga os botoes
                for i in range(0, 9):
                    self.botoes[i].setEnabled(False)
                # checa qual player fez o ponto
                if self.btn3.text() == "X":
                    # incrementa o contador de vitórias do X
                    self.x += 1
                else:
                    # incrementa o contador de vitórias do O
                    self.OO += 1
                # chama a função ganhador
                self.ganhador(self.btn3, self.btn5, self.btn7)

    # Função ganhador para mudar cor dos botoes e atualizar o placar
    def ganhador(self, m, n, k):
        # muda a cor dos três botoes
        m.setStyleSheet("color: red")
        n.setStyleSheet("color: red")
        k.setStyleSheet("color: red")
        # atualiza o placar
        self.label1.setText('''PLACAR:
X: {}
O: {}'''.format(self.x, self.OO))


app = QApplication(sys.argv)  # instanciando a aplicação em uma variavel
jan = Jan()  # instanciando a classe em uma variavel
jan.show()  # mostrando a janela
app.exec()  # mostrando a aplicação
