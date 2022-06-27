from ..builder.congrats_builder import CongratsBuilder


class CongratsBuilderDirector:
    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> CongratsBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: CongratsBuilder) -> None:
        self._builder = builder

    def build_short_congrats(self):
        pass

    def build_long_congrats(self):
        self.builder.generate_intro(None)
        self.builder.generate_enumeration(None)
        self.builder.generate_prose(None)
        self.builder.generate_ending(None)
