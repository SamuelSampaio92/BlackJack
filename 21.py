import random

def distribuir_carta():
    return random.randint(1, 11)

def calcular_pontuacao(cartas):
    # Ajusta o valor do Ás (11 para 1) se a pontuação ultrapassar 21
    if sum(cartas) > 21 and 11 in cartas:
        cartas[cartas.index(11)] = 1
    return sum(cartas)

def exibir_cartas(jogador, cartas, total):
    print(f"{jogador} tem as cartas: {cartas} | Pontuação: {total}")

def jogo_21():
    print("\nBem-vindo ao Jogo 21!")
    jogador_cartas = [distribuir_carta(), distribuir_carta()]
    computador_cartas = [distribuir_carta(), distribuir_carta()]

    jogador_pontuacao = calcular_pontuacao(jogador_cartas)
    computador_pontuacao = calcular_pontuacao(computador_cartas)

    # Turno do jogador
    while jogador_pontuacao < 21:
        exibir_cartas("Jogador", jogador_cartas, jogador_pontuacao)
        continuar = input("Deseja pegar outra carta? (s/n): ").lower()
        if continuar == 's':
            jogador_cartas.append(distribuir_carta())
            jogador_pontuacao = calcular_pontuacao(jogador_cartas)
        else:
            break

    # Turno do computador
    while computador_pontuacao < 17:
        computador_cartas.append(distribuir_carta())
        computador_pontuacao = calcular_pontuacao(computador_cartas)

    # Resultado final
    print("\n--- Resultado Final ---")
    exibir_cartas("Jogador", jogador_cartas, jogador_pontuacao)
    exibir_cartas("Computador", computador_cartas, computador_pontuacao)

    if jogador_pontuacao > 21:
        print("Você estourou 21! Você perdeu!")
    elif computador_pontuacao > 21 or jogador_pontuacao > computador_pontuacao:
        print("Parabéns, você venceu!")
    elif jogador_pontuacao == computador_pontuacao:
        print("Empate!")
    else:
        print("O Computador venceu. Tente novamente!")

def main():
    while True:
        jogo_21()
        resposta = input("\nVocê deseja jogar novamente? (s/n): ").lower()
        if resposta != 's':
            print("Obrigado por jogar! Até a próxima.")
            break

# Executar o jogo
if __name__ == "__main__":
    main()
