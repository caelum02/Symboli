from abc import ABC, abstractmethod

class Symbol(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def toTex():
        pass

    def __repr__(self):
        return self.toTex()
