# MAT01126
Repositório para compartilhar o material da disciplina de Algoritmos e Estrutura de Dados.

Possui, por objetivo, a implementação de código que possa reconhecer, a partir de imagens, peças (parafusos, arruelas e porcas) dispostos em uma folha de ofício A4 (210 x 297 mm).

Para este fim utilizaremos técnicas de visão computacional, com o OpenCV.

## Apresentação do trabalho

### Fluxo do programa
* O programa a ser desenvolvido recebe imagens como dados de entrada e deve produzir uma lista com a contagem de cada uma das peças.
* O fluxo do programa seguirá os seguintes passos:

1. Pré-processamento:
    1. Leitura da imagem.
    2. Converter para escala de cinza.
    3. Reduzir a resolução.
    4. Normalização das imagens. Rotações, correções de perspectiva, etc.
2. Processamento:
    1. Detectar as peças.
    2. Normalizações.
    3. Selecionar informações relevantes para identificação.
3. Identificação da peça e produção de resultados.

### Desenvolvimento
* O desenvolvimento irá considerar os seguintes princípios:
1. Todos irão participar.
2. Algumas etapas do fluxo podem ser simplificadas ou mesmo omitidas numa primeira fase.
3. Obter uma versão funcional para as imagens mais simples.
4. Identificar quais passos são mais desafiadores e quais etapas geram mais erros.
5. Analisar a necessidade de aprimorar cada uma das fases, isto é, não perder tempo em trechos de programa, que podem não se mostrar críticos.
6. Documentar bem o código à medida que se avança. Isso facilitará a compreensão e manutenção do código.


## Instalação

Antes de mais nada, é necessário:

1. Instalar o [Python](https://www.python.org/downloads/) (versão 3.11)
2. Instalar o [Git](https://git-scm.com/downloads)
3. Possuir uma conta no GitHub
4. Ter um editor de código

### Configuração

1. Clone o repositório
   ```sh
   git clone
    ```
2. Instale Pipenv, caso não tenha
   ```sh
   pip install pipenv
   ```
3. Instale as dependências
   ```sh
    pipenv install
    ```

**"Programming is learned by writing programs. In this, programming is similar to other endeavors with a practical component. You cannot learn to swim, to play a musical instrument, or to drive a car just from reading a book — you must practice."**

— Bjarne Stroustrup, *Programming Principles and Practice Using C++*
