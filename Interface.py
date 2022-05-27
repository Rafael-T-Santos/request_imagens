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
import xml.etree.ElementTree as ET 

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Baixa Imagens Roms")
        self.setFixedSize(500, 250)
        self.setToolTip("Janela Principal")
        self.setAutoFillBackground(True)
        self.setStyleSheet('background-color: #81CAB2;')

        self.set_form()
        self.set_icon()

    def set_icon(self):
        appIcon = QIcon(r"img/icon.png")
        self.setWindowIcon(appIcon)

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
        self.pushButton.clicked.connect(self.consulta_imagens)

        self.label4 = QLabel('Qt. Roms: ',self)
        self.label4.setGeometry(QRect(30, 200, 50, 16))

        self.lineEdit4 = QLineEdit(self)
        self.lineEdit4.setGeometry(QRect(90, 200, 30, 16))
        self.lineEdit4.setReadOnly(True)
        self.lineEdit4.setStyleSheet('background-color: white;')

        self.label5 = QLabel('Qt. Imgs: ',self)
        self.label5.setGeometry(QRect(30, 220, 50, 16))

        self.lineEdit5 = QLineEdit(self)
        self.lineEdit5.setGeometry(QRect(90, 220, 30, 16))
        self.lineEdit5.setReadOnly(True)
        self.lineEdit5.setStyleSheet('background-color: white;')

    def browsefiles1(self):
        global fname
        fname = str(QFileDialog.getExistingDirectoryUrl(self))
        fname = fname.replace("PySide6.QtCore.QUrl('file:///", '').replace('/', '\\').replace("')", '')
        self.lineEdit1.setText(fname)
        self.lineEdit4.setText(str(len(os.listdir(fname))))

    def browsefiles2(self):
        global fname2
        fname2 = str(QFileDialog.getExistingDirectory(self))
        fname2 = fname2.replace("PySide6.QtCore.QUrl('file:///", '').replace('/', '\\').replace("')", '')
        self.lineEdit2.setText(fname2)
        self.lineEdit5.setText(str(len(os.listdir(fname2))))

    def consulta_imagens(self):
        lista_roms = os.listdir(fname)
        lista_xml = os.listdir(fname)

        for i in range(len(lista_roms)):
            lista_roms[i] = lista_roms[i].replace(" ", "+").replace('.zip', "")

        for i in range(len(lista_roms)):
            lista_imagens = []

            htmldata = requests.get("https://www.google.com/search?q="+lista_roms[i]+"+snes&tbm=isch").text
            soup = BeautifulSoup(htmldata, 'html.parser')

            for item in soup.find_all('img'):
                lista_imagens.append(item['src'])

            Image_url = lista_imagens[1]
            im = Image.open(requests.get(Image_url, stream=True).raw)
            im.save(fname2+"\\"+lista_roms[i].replace("+", " ")+"-image"+".png")
            
        self.lineEdit5.setText(str(len(os.listdir(fname2))))
        cria_xml(lista_xml)        

def cria_xml(lista_xml):
    gamelist = ET.Element('gameList')

    for i in range(len(lista_xml)):
        extensao = lista_xml[i][-4:]
        nome_arquivo = lista_xml[i].replace(extensao, "")
        game = ET.SubElement(gamelist, 'game') 
        path = ET.SubElement(game, 'path') 
        name = ET.SubElement(game, 'name') 
        image = ET.SubElement(game, 'image')
        lang = ET.SubElement(game, 'lang')
        path.text = "./"+lista_xml[i]
        name.text = nome_arquivo
        image.text = "./images/"+nome_arquivo+"-image.png"
        lang.text = "en"
  
    b_xml = ET.tostring(gamelist) 
    with open(fname+"\\gamelist.xml", "wb") as f: 
        f.write(b_xml)

def executa():
    myApp = QApplication.instance()

    if myApp is None:
        myApp = QApplication(sys.argv)

    janela = Window()
    janela.show()
    myApp.exec()

executa()
