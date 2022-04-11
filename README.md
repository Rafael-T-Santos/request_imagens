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
