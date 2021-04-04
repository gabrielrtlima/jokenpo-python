from random import choice

print('-'*70+'\nBem vindo ao PEDRA, PAPEL E TESOURA (.py)\n'+'-'*70)

while True:
    start = input('\nDigite 1 se deseja iniciar o jogo\nDigite 2 se deseja saber como funciona\nDigite 3 para saber mais informacoes sobre o desenvolvedor\n')
    if start == '1':
        gameObjects = ['pedra', 'papel', 'tesoura']
        objEscolhido = input('Você deseja escolher pedra, papel ou tesoura?\n')
        objEscolhido = objEscolhido.upper()
        scrEscolhido = choice(gameObjects).upper()
        print('Você escolheu {} e a maquina escolheu: {}'.format(objEscolhido, scrEscolhido))
        if objEscolhido == scrEscolhido:
            print('EMPATE!')
        elif objEscolhido == 'PEDRA' and scrEscolhido == 'PAPEL':
            print('Você perdeu! :(')
        elif objEscolhido == 'PAPEL' and scrEscolhido == 'PEDRA':
            print('Você ganhou! :)')
        elif objEscolhido == 'TESOURA' and scrEscolhido == 'PEDRA':
            print('Você perdeu! :(')
        elif objEscolhido == 'TESOURA' and scrEscolhido == 'PAPEL':
            print('Você ganhou! :)')
        elif objEscolhido == 'PAPEL' and scrEscolhido == 'TESOURA':
            print('Você perdeu! :(')
        elif objEscolhido =='PEDRA' and scrEscolhido == 'TESOURA':
            print('Você ganhou! :)')
    elif start == '2':
        print('A máquina irá sortear um objeto e comparar com o seu para saber quem ganhou\n'+'-'*70+'\nO jogo funciona da seguinte forma:\nPEDRA GANHA DE TESOURA\nPEDRA PERDE DE PAPEL\nTESOURA GANHA DE PAPEL\n'+'-'*70)

    else:
        print('-'*70+'\nScript desenvolvido por Gabriel\ngithub@gabrielrtlima\ngabriel.rtlima@upe.br\ninstagram@gabrielrtl\n'+'-'*70)
    
    restart = input('\n\nSe deseja iniciar um novo jogo digite 1\nSe deseja sair digite 2\n')
    if restart == '1':
        continue
    else:
        print('Goodbye! :)')
        break