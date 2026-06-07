"""
Programa: gan_realista.py

Exemplo didático de um Generator simples usando PyTorch.
Observação: o termo correto é GAN, não GAMS.
GAN = Generative Adversarial Network.
"""
import os
from pathlib import Path

import torch
import torch.nn as nn
from PIL import Image


class Generator(nn.Module):
    def __init__(self) -> None:
        super().__init__()

        self.model = nn.Sequential(
            nn.Linear(100, 256),
            nn.ReLU(),
            nn.Linear(256, 784),
            nn.Tanh()
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.model(x)


def gerar_imagem() -> None:
    print("Gerando imagem usando uma GAN simples...")

    generator = Generator()
    noise = torch.randn(1, 100)

    fake_image = generator(noise)

    fake_image = fake_image.view(28, 28)

    fake_image = (fake_image + 1) / 2
    fake_image = fake_image.detach().numpy() * 255
    fake_image = fake_image.astype("uint8")

    imagem = Image.fromarray(fake_image)

    caminho_saida = Path("imagem_gerada.png")
    imagem.save(caminho_saida)

    print(f"Imagem salva em: {caminho_saida}")


def main() -> None:
    os.system("cls" if os.name == "nt" else "clear")
    gerar_imagem()


if __name__ == "__main__":
    main()