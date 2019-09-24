
class BaseTree():
    def __init__(self, value, leafs=None, parent=None):
        self.value = value
        self.leafs = leafs
        self.parent = parent

class GeneratedTree(BaseTree):
    def __init__(self, generator, state=None):
        
        value, leafs = generator(state)


