from ..meta.singleton import SingletonMeta


class CongratsData(metaclass=SingletonMeta):
    @staticmethod
    def get_intros() -> set:
        pass

    @staticmethod
    def get_wishes_intros() -> set:
        pass

    @staticmethod
    def get_enumerations() -> set:
        pass

    @staticmethod
    def get_prose() -> set:
        pass

    @staticmethod
    def get_endings() -> set:
        pass
