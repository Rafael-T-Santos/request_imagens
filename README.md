# request_imagens
Script para coletar imagens de jogos

Utilizadas as bibliotecas:
requests: Efetuar a requisição dos dados do site
beautifulsoup4: Fazer a extração dos dados
Pillow: Manipular e salvar as imagens
os: Listar o nome dos arquivos para serem pesquisados
PySide6: Criação de interface gráfica

* Código fonte disponivel no arquivo Interface.py
  Ao executar o código uma interface gráfica é criada mostrando os campos:
    * Pasta das Roms: Local onde devem estar todas as ROMS que deseja pesquisar imagens, esse campo não é editável, para escolher a pasta basta clicar no botão logo a direita do campo.
    * Pasta das Imagens: Local de destino das imagens, o campo também não é editável, basta clicar no botão logo a direita  escolher onde as imagens serão salvas.
    * Nome do Console: Esse campo é digitável e deve-se digitar o nome do console a qual pertence a imagem, lembre-se que essa consulta é feita no google imagens então coloca apenas o nome do console aqui para que não haja problemas futuros.
    * Coletar Imagens: Botão responsável por coletar as informações passadas anteriormente e fazer a consulta de imagens.

A consulta salva a primeira imagem resultante da pesquisa da página do Google Imagens


# Como Instalar ?

* Efetuar o download do Python em https://www.python.org/downloads/ e instalar, lembrar de marcar a caixa "ADD Python to PATH"
* Com o python instalado, efetuar o download dos arquivos Interface.py e requirements.txt
* Abrir a pasta onde os arquivos se encontram segurar o SHIFT e clicar com o botão direito em uma area qualquer da pasta, nas opções que aparecerem clicar em "Abrir janela de comando aqui" ou "Abrir janela do PowerShell aqui", isso fará com que se abra uma janela de comando exatamente na pasta onde se encontram os arquivos.
* Na janela de comando aberta digitar "pip install -r requirements.txt" sem as aspas, e pressionar ENTER, isso fará com que sejam instaladas as bibliotecas utilizadas no projeto.
* Se todos os passos foram executados corretamente você já deve conseguir executar o arquivo Interface.py apenas dando dois cliques no mesmo.


![Tela Inicial](img/inicial.jpg?raw=true "Tela Inicial")
