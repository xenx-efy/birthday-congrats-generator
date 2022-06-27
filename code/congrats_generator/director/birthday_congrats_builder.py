import random

from ..builder.congrats_builder import CongratsBuilder
from ..model.congratulation import Congratulation
from ..data.birthday_congrats_data import BirthdayCongratsData


class BirthdayCongratsBuilder(CongratsBuilder):
    def __init__(self) -> None:
        self._congratulation = None
        self._data = BirthdayCongratsData()
        self.reset()

    def reset(self) -> None:
        self._congratulation = Congratulation()

    @property
    def congratulation(self) -> Congratulation:
        return self._congratulation

    def generate_intro(self, generator_config) -> None:
        intros = self._data.get_intros()
        chosen_intro = random.choice([*intros])
        self._congratulation.add(chosen_intro)

    def generate_enumeration(self, generator_config) -> None:
        wishes_enumerations = self._data.get_enumerations()

        wishes_intro = random.choice([*self._data.get_wishes_intros()])
        wishes = ', '.join(random.choices([*wishes_enumerations], k=4))

        self._congratulation.add(f'{wishes_intro} {wishes}.')

    def generate_prose(self, generator_config) -> None:
        prose_wishes = self._data.get_prose()
        chosen_prose = random.choice([*prose_wishes])
        self._congratulation.add(f'{chosen_prose}.')

    def generate_ending(self, generator_config) -> None:
        endings = self._data.get_endings()
        chosen_ending = random.choice([*endings])
        self._congratulation.add(f'{chosen_ending}.')
