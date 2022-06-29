from ..builder.congrats_builder import CongratsBuilder


class CongratsBuilderDirector:
    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> CongratsBuilder | None:
        return self._builder

    @builder.setter
    def builder(self, builder: CongratsBuilder) -> None:
        self._builder = builder

    def build_shot_congrats(self):
        if self.builder is not None:
            self.builder.generate_enumeration(None)

    def build_long_congrats(self):
        if self.builder is not None:
            self.builder.generate_intro(None)
            self.builder.generate_enumeration(None)
            self.builder.generate_prose(None)
            self.builder.generate_ending(None)
