from abc import ABC, abstractmethod

class IIndicator(ABC):
    @abstractmethod
    def on(self): pass

    @abstractmethod
    def off(self): pass

    @abstractmethod
    def blink(self, frequency_hz: float): pass