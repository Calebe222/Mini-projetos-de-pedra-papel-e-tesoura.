print("---------------------------------------------------")
print(" ---- Jogo pedra, papel e tesoura  (2 jogadores) ---- ")
print("---------------------------------------------------")
print("Bem vindos! Cada jogador deve escolher uma das opcoes:")

opcoes_validas = ("pedra", "papel", "tesoura")
print(f"Opcoes validas: {opcoes_validas}")
print("-" * 25) # imprime uma linha de separacao

jogada_jogador1_inicial  = input("Jogador 1, faca sua jogada: ")
jogada_jogador2_inicial  = input("Jogador 2, faca sua jogada: ")

# Tratamento de dados de entrada 

jogada_jogador1 = jogada_jogador1_inicial.lower().strip()
jogada_jogador2 = jogada_jogador2_inicial.lower().strip()

print("-" * 25) # imprime uma linha de separacao
print(f"Jogador 1 jogou: {jogada_jogador1}")
print(f"Jogador 2 jogou: {jogada_jogador2}")
print("-" * 25) # imprime uma linha de separacao


if jogada_jogador1 not in opcoes_validas or jogada_jogador2 not in opcoes_validas:
    print("Jogada invalida! As opcoes validas sao: pedra, papel ou tesoura.")

elif jogada_jogador1 == jogada_jogador2:
    print("Empate! Ninguem venceu desta vez.")

elif (jogada_jogador1 == "pedra" and jogada_jogador2 == "tesoura") or \
    (jogada_jogador1 == "papel" and jogada_jogador2 == "pedra") or \
    (jogada_jogador1 == "tesoura" and jogada_jogador2 == "papel"):
    print("Jogador 1 venceu! Parabens!")

else: 
    print("Jogador 2 venceu! Parabens!")

print("---------------------------------------------------")
print(" ---- Fim do jogo ---- ")


