import random
from typing import Any

from .congrats_builder import CongratsBuilder
from ..data.default_congrats_data import DefaultCongratsData
from ..model.congratulation import Congratulation


class ShotCongratsBuilder(CongratsBuilder):
    def __init__(self) -> None:
        self._congratulation = None
        self._data = DefaultCongratsData()
        self.reset()

    def reset(self) -> None:
        self._congratulation = Congratulation()

    @property
    def congratulation(self) -> Congratulation:
        return self._congratulation

    def generate_enumeration(self, generator_config: Any) -> None:
        enums = self._data.get_enumerations()
        shot = random.choice([*enums])
        self._congratulation.add(shot)
