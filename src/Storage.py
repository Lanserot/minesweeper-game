class Storage:

    def __init__(self):
        self.rendererClass = None
        self.logicClass = None
        self.gameLogicClass = None
        self.memoryClass = None

    def get_memory_class(self):
        return self.memoryClass

    def get_renderer_class(self):
        return self.rendererClass

    def get_logic_class(self):
        return self.logicClass

    def getGameLogicClass(self):
        return self.gameLogicClass
