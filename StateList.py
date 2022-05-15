from State import State

class Acordado(State):
    def Execute(self):
        print('Acordado')

class Trabalhando(State):
    def Execute(self):
        print('Trabalhando')

class Descansando(State):
    def Execute(self):
        print('Descansando')

class Dormindo(State):
    def Execute(self):
        print('Dormindo')