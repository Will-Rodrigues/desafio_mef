class MEF(object):
    def __init__(self, maquina):
        self.maquina = maquina
        self.states = {}
        self.transitions = {}
        self.currentState = None
        self.transition = None

    def setState(self, stateName):
        self.currentState = self.states[stateName]

    def Transition(self, transitionName):
        self.transition = self.transitions[transitionName]

    def Execute(self):
        if (self.transition):
            self.transition.Execute()
            self.setState(self.transition.toState)
            self.transition = None
        self.currentState.Execute()