from abc import abstractmethod, ABC


class CongratulationInterface(ABC):
    @abstractmethod
    def congratulate(self):
        pass
