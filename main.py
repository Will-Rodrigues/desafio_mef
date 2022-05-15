from Maquina import Maquina
from StateList import *
from Transition import *

if __name__ == "__main__":
    maquina = Maquina()

    maquina.MEF.states['Acordado'] = Acordado()
    maquina.MEF.states['Descansando'] = Descansando()
    maquina.MEF.states['Trabalhando'] = Trabalhando()
    maquina.MEF.states['Dormindo'] = Dormindo()
    maquina.MEF.transitions['08:00'] = Transition('Trabalhando')
    maquina.MEF.transitions['12:00'] = Transition('Descansando')
    maquina.MEF.transitions['13:00'] = Transition('Trabalhando')
    maquina.MEF.transitions['18:00'] = Transition('Descansando')
    maquina.MEF.transitions['22:00'] = Transition('Dormindo')

    while True:
        quest = input('Digite o comando (ou "ajuda" para a lista de comandos):')

        if quest == 'ajuda':
            print('transições - Mostra as transições possíveis')
            print('estados - mostra os estados possíveis')
            print('sair - para encerrar a aplicação')
            print('nome do estado atual - para obter a transições possíveis')
        
        if quest == 'transições':
            print('Essas são a transições possíveis:')
            for transitions in maquina.MEF.transitions:
                print(transitions)

        if quest == 'estados':
            print('Esses são os estados possíveis:')

        if quest == 'sair':
            quit()

        if quest in maquina.MEF.transitions:
            maquina.MEF.Transition(quest)
            maquina.MEF.Execute()

        if quest == type(maquina.MEF.currentState).__name__:
            print('Essas são a transições possíveis:')
            for transitions in maquina.MEF.transitions:
                print(transitions)
