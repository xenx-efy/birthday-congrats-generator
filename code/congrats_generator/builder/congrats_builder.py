from abc import ABC, abstractmethod
from typing import Any


class CongratsBuilder(ABC):
    @property
    @abstractmethod
    def congratulation(self) -> None:
        pass

    def generate_intro(self, generator_config: Any) -> None:
        pass

    def generate_enumeration(self, generator_config: Any) -> None:
        pass

    def generate_prose(self, generator_config: Any) -> None:
        pass

    def generate_ending(self, generator_config: Any) -> None:
        pass
