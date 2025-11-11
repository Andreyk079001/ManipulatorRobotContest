from abc import ABC, abstractmethod

class IManipulator(ABC):
    @abstractmethod
    def connect(self): pass

    @abstractmethod
    def get_control(self): pass

    @abstractmethod
    def move_to(self, position, orientation, velocity, acceleration): pass

    @abstractmethod
    def get_coordinates(self): pass

    @abstractmethod
    def stream_velocity(self, linear_vel, angular_vel): pass

    @abstractmethod
    def stop(self): pass