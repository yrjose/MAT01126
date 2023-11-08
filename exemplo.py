import cv2
import numpy as np

# Url na imagem a ser lida
# url = 'https://github.com/fazedo/MAT01126/raw/main/Parafuso/G1/imagem_G1_01.jpg'
# url = 'https://github.com/fazedo/MAT01126/raw/main/Parafuso/G2/imagem_G2_10.jpg'
# url = 'https://github.com/fazedo/MAT01126/raw/main/Parafuso/G2/imagem_G2_13.jpg'
url = './Parafuso/G1/imagem_G1_01.jpg'  # imagem local

# Tenta abrir o objeto de captura de vídeo a partir da URL fornecida
# imagem_original = cv2.imread('./Parafuso/G1/imagem_G1_01.jpg')  # alternativamente
cap = cv2.VideoCapture(url)


def mostra_imagem(img: cv2.Mat | np.ndarray):
    cv2.imshow('Imagem', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Verifica se a captura foi bem-sucedida
if cap.isOpened():
    # Lê a imagem
    ret, imagem_original = cap.read()
    cap.release()  # Libera o objeto de captura de vídeo

    # Obtém as dimensões da imagem original
    altura, largura, canais = imagem_original.shape
    # Observe a órdem

    print(f"As dimensões da imagem são: largura={largura}, altura={altura} e canais={canais}")

    # Define um fator para reduzir o tamanho da imagem (altere se necessário)
    fator_reducao = 3

    # Calcula as novas dimensões para a imagem
    nova_altura = altura // fator_reducao
    nova_largura = largura // fator_reducao

    # Redimensiona a imagem
    imagem = cv2.resize(imagem_original, (nova_largura, nova_altura))

    # Exibe a imagem redimensionada
    mostra_imagem(imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Vamos inserir um retângulo
    P_1r = (0.25, 0.38)  # Posições relativas
    P_2r = (0.45, 0.45)  # Isso nos permite mudar a resolução da imagem

    dimensoes = imagem.shape
    P_1a = tuple(int(x * y) for x, y in zip(dimensoes, P_1r))
    P_2a = tuple(int(x * y) for x, y in zip(dimensoes, P_2r))

    cor = (0, 255, 100)  # Verde claro
    espessura = 1

    cv2.rectangle(imagem, P_1a, P_2a, cor, espessura)  # Altera o objeto imagem.
    mostra_imagem(imagem)

    # Mostra um corte
    corte = imagem[P_1a[1]:P_2a[1], P_1a[0]:P_2a[0], :]
    mostra_imagem(corte)
else:
    print("Erro ao ler a URL")
