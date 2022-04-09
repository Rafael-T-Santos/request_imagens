import requests
import os
from bs4 import BeautifulSoup
from PIL import Image

def getdata(url):
    r = requests.get(url)
    return r.text

lista_snes = os.listdir('Roms')

for i in range(len(lista_snes)):
    lista_snes[i] = lista_snes[i].replace(" ", "+").replace('.zip', "")

for i in range(len(lista_snes)):
    jogo = lista_snes[i]
    lista_imagens = []

    htmldata = getdata("https://www.google.com/search?q="+lista_snes[i]+"+snes&tbm=isch")
    soup = BeautifulSoup(htmldata, 'html.parser')

    for item in soup.find_all('img'):
        lista_imagens.append(item['src'])

    Image_url = lista_imagens[1]
    im = Image.open(requests.get(Image_url, stream=True).raw)
    im.save(r"imagens\\"+lista_snes[i].replace("+", " ")+".png")

