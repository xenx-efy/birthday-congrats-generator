import random

from ..data.birthday_congrats_data import BirthdayCongratsData
from ..model.congratulation import Congratulation
from .congrats_builder import CongratsBuilder


class BirthdayCongratsBuilder(CongratsBuilder):
    def __init__(self) -> None:
        self._congratulation = None
        self._data = BirthdayCongratsData()
        self.reset()

    def reset(self) -> None:
        self._congratulation = Congratulation()

    @property
    def congratulation(self) -> Congratulation | None:
        return self._congratulation

    def generate_intro(self, generator_config) -> None:
        intros = self._data.get_intros()
        chosen_intro = random.choice([*intros])
        if self._congratulation is not None:
            self._congratulation.add(chosen_intro)

    def generate_enumeration(self, generator_config) -> None:
        wishes_enumerations = self._data.get_enumerations()

        wishes_intro = random.choice([*self._data.get_wishes_intros()])
        wishes = ", ".join(random.choices([*wishes_enumerations], k=4))

        if self._congratulation is not None:
            self._congratulation.add(f"{wishes_intro} {wishes}.")

    def generate_prose(self, generator_config) -> None:
        prose_wishes = self._data.get_prose()
        chosen_prose = random.choice([*prose_wishes])
        if self._congratulation is not None:
            self._congratulation.add(f"{chosen_prose}.")

    def generate_ending(self, generator_config) -> None:
        endings = self._data.get_endings()
        chosen_ending = random.choice([*endings])
        if self._congratulation is not None:
            self._congratulation.add(f"{chosen_ending}.")
