'''
Programa: cv2_visao.py
Programa para demonstrar o uso da biblioteca OpenCV para processamento de imagens.
'''
import cv2
import os

# Função para simular um processamento de imagem
def processamento():
    # Carregar uma imagem
    imagem = cv2.imread('imagem_exemplo.jpg')

    # Verificar se a imagem foi carregada corretamente
    if imagem is None:
        print("Erro ao carregar a imagem.")
        return

    # Exibir a imagem original
    cv2.imshow('Imagem Original', imagem)

    # Converter a imagem para escala de cinza
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Exibir a imagem em escala de cinza
    cv2.imshow('Imagem em Escala de Cinza', cinza)

    # Aguardar até que uma tecla seja pressionada e fechar as janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Função para exibir mensagem de término
def termino():
    print("Processamento concluído.")

# Função principal para testar o processamento de imagens
def main():
    os.system("cls" if os.name == "nt" else "clear")  # Limpa a tela
    processamento()
    termino()

if __name__ == "__main__":
    main()

