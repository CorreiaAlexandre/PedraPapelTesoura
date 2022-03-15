# Escolha do nome
jogador_01 = input("Entre com seu nome, primeiro jogador: ")
jogador_02 = input("Entre com seu nome, segundo jogador: ") 
pontos_jog1 = 0
pontos_jog2 = 0

print()
# Boas-vindas 
print(f'Ola {jogador_01} jogador 1')
print(f'Ola {jogador_02} jogador 2')
print()  
print(""" Suas Opcoes : 
[0] pedra
[1] papel
[2] tesoura """)

# Logica do jogo com repeticao
while True:
    jog1 = int(input(f'Qual e sua jogada {jogador_01}, ? ' ))
    jog2 = int(input(f'Qual e a sua jogada {jogador_02}, ? ' ))
    print()

    #pedra > tesoura
    #tesoura > papel
    #papel > pedra

    if jog1 == 0:
        print('O jog1 escolheu: Pedra')
        if jog2 == 0:
            print("Empate!")
        elif jog2 == 1:
            print("Jog2 vence,parabens")
            pontos_jog2 += 1
        elif jog2 == 2:
            print("jog1 vence, parabens")
            pontos_jog1 += 1
        else:
            print("Operacao invalida")

    elif jog1 == 1:
        print('O jog1 escolheu: Papel')
        if jog2 == 0:
            print("jog1 venceu,parabens")
            pontos_jog1 += 1
        elif jog2 == 1:
            print("Empate!")
        elif jog2 == 2:
            print("jog2 vence, parabens")
            pontos_jog2 += 1
        else:
            print("Operacao invalida")

    elif jog1 == 2:
        print('O jog1 escolheu: Tesoura')
        if jog2 == 0:
            print("Jog2 venceu")
            pontos_jog2 += 1
        elif jog2 == 1:
            print("jog1 venceu")
            pontos_jog1 += 1
        elif jog2 == 2:
            print("Empate!")
        else:
            print("Operacao invalida")
    else:
        print("Operacao invalida")

    if (pontos_jog1 >= 2) | (pontos_jog2 >= 2):
        if pontos_jog1 >= 2:
            print('Jogador 1 venceu a partida!')
        else:
            print('Jogador 2 venceu a partida!')

        jogar_novamente = input("Jogar novamente? (s/n):")
        if jogar_novamente.lower() != "s":
            break
        else:
            pontos_jog1, pontos_jog2 = 0, 0
print(" Ok, ate a proxima")   


