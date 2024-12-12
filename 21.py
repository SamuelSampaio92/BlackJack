import random

def distribuir_carta():
    return random.randint(1, 11)

def calcular_pontuacao(cartas):
    if sum(cartas) > 21 and 11 in cartas:
        cartas[cartas.index(11)] = 1
    return sum(cartas)

def exibir_cartas(jogador, cartas, total):
    print(f"{jogador} tem as cartas: {cartas} | Pontuação: {total}")

def obter_resposta_valida(mensagem):
    while (resposta := input(mensagem).strip().lower()) not in ('s', 'n'):
        print("Por favor, digite apenas 's' para sim ou 'n' para não.")
    return resposta

def obter_valor_aposta(fichas):
    while True:
        try:
            aposta = int(input(f"Quantas fichas você quer apostar? (1 a {fichas}): "))
            if 1 <= aposta <= fichas:
                return aposta
        except ValueError:
            pass
        print(f"Aposta inválida! Você tem {fichas} fichas disponíveis.")

def jogo_21(fichas):
    print("\nBem-vindo ao Jogo 21!")
    aposta = obter_valor_aposta(fichas)

    jogador_cartas = [distribuir_carta(), distribuir_carta()]
    computador_cartas = [distribuir_carta(), distribuir_carta()]

    while (jogador_pontuacao := calcular_pontuacao(jogador_cartas)) < 21:
        exibir_cartas("Jogador", jogador_cartas, jogador_pontuacao)
        if obter_resposta_valida("Pegar outra carta? (s/n): ") == 's':
            jogador_cartas.append(distribuir_carta())
        else:
            break

    while (computador_pontuacao := calcular_pontuacao(computador_cartas)) < 17:
        computador_cartas.append(distribuir_carta())

    print("\n--- Resultado Final ---")
    exibir_cartas("Jogador", jogador_cartas, jogador_pontuacao)
    exibir_cartas("Computador", computador_cartas, computador_pontuacao)

    if jogador_pontuacao > 21 or (computador_pontuacao <= 21 and computador_pontuacao > jogador_pontuacao):
        print("Você perdeu!")
        return fichas - aposta
    elif jogador_pontuacao == computador_pontuacao:
        print("Empate!")
        return fichas
    else:
        print("Você venceu!")
        return fichas + aposta

def main():
    fichas = 100
    print(f"Você começa o jogo com {fichas} fichas.")

    while True:
        while fichas > 0 and obter_resposta_valida("\nVocê deseja jogar? (s/n): ") == 's':
            fichas = jogo_21(fichas)
            print(f"\nVocê agora tem {fichas} fichas.")

        if fichas <= 0:
            print("\nVocê ficou sem fichas!")

        if obter_resposta_valida("Deseja comprar mais fichas e reiniciar o jogo? (s/n): ") == 's':
            fichas = 100
            print("\nVocê recebeu 100 fichas para continuar jogando.")
        else:
            break

    print("--- Obrigado por jogar! ---")

if __name__ == "__main__":
    main()
