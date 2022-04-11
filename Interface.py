from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QToolButton,
    QWidget, QDialog, QFileDialog, QMessageBox)
import sys
import requests
import os
from bs4 import BeautifulSoup
from PIL import Image

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Baixa Imagens Roms")
        self.setFixedSize(500, 250)
        self.setToolTip("Janela Principal")
        self.setAutoFillBackground(True)
        self.setStyleSheet('background-color: #81CAB2;')

        self.set_form()

    def set_form(self):

        self.label1 = QLabel('Pasta das Roms: ',self)
        self.label1.setGeometry(QRect(30, 60, 100, 16))   

        self.lineEdit1 = QLineEdit(self)
        self.lineEdit1.setGeometry(QRect(140, 60, 290, 22))
        self.lineEdit1.setReadOnly(True)
        self.lineEdit1.setStyleSheet('background-color: white;')
        self.lineEdit1.setPlaceholderText('Escolha a pasta onde estão salvas as Roms')

        self.toolButton1 = QToolButton(self)
        self.toolButton1.setGeometry(QRect(440, 60, 22, 22))
        self.toolButton1.clicked.connect(self.browsefiles1)

        self.label2 = QLabel('Pasta das Imagens: ',self)
        self.label2.setGeometry(QRect(30, 92, 100, 16))

        self.lineEdit2 = QLineEdit(self)
        self.lineEdit2.setGeometry(QRect(140, 92, 290, 22))
        self.lineEdit2.setReadOnly(True)
        self.lineEdit2.setStyleSheet('background-color: white;')
        self.lineEdit2.setPlaceholderText('Escolha a pasta onde serão salvas as imagens')

        self.toolButton2 = QToolButton(self)
        self.toolButton2.setGeometry(QRect(440, 92, 22, 22))     
        self.toolButton2.clicked.connect(self.browsefiles2)

        self.label3 = QLabel('Nome do Console: ',self)
        self.label3.setGeometry(QRect(30, 124, 100, 16))

        self.lineEdit3 = QLineEdit(self)
        self.lineEdit3.setGeometry(QRect(140, 124, 290, 22))
        self.lineEdit3.setStyleSheet('background-color: white;')
        self.lineEdit3.setPlaceholderText('Digite o nome do console. Ex: Snes, PSone, Mame')

        self.pushButton = QPushButton('Coletar Imagens',self)
        self.pushButton.setGeometry(QRect(220, 160, 121, 24))
        self.pushButton.clicked.connect(consulta_imagens)

    def browsefiles1(self):
        global fname
        fname = str(QFileDialog.getExistingDirectoryUrl(self))
        fname = fname.replace("PySide6.QtCore.QUrl('file:///", '').replace('/', '\\').replace("')", '')
        self.lineEdit1.setText(fname)

    def browsefiles2(self):
        global fname2
        fname2 = str(QFileDialog.getExistingDirectory(self))
        fname2 = fname2.replace("PySide6.QtCore.QUrl('file:///", '').replace('/', '\\').replace("')", '')
        self.lineEdit2.setText(fname2)

def getdata(url):
    r = requests.get(url)
    return r.text

def consulta_imagens():
    lista_roms = os.listdir(fname)

    for i in range(len(lista_roms)):
        lista_roms[i] = lista_roms[i].replace(" ", "+").replace('.zip', "")

    for i in range(len(lista_roms)):
        jogo = lista_roms[i]
        lista_imagens = []

        htmldata = getdata("https://www.google.com/search?q="+lista_roms[i]+"+snes&tbm=isch")
        soup = BeautifulSoup(htmldata, 'html.parser')

        for item in soup.find_all('img'):
            lista_imagens.append(item['src'])

        Image_url = lista_imagens[1]
        im = Image.open(requests.get(Image_url, stream=True).raw)
        im.save(fname2+"\\"+lista_roms[i].replace("+", " ")+".png")

def executa():
    myApp = QApplication.instance()

    if myApp is None:
        myApp = QApplication(sys.argv)

    janela = Window()
    janela.show()
    myApp.exec_()

executa()