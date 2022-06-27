from .director.birthday_congrats_builder import BirthdayCongratsBuilder
from .director.congrats_builder_director import CongratsBuilderDirector
from .type.congratulation import CongratulationType


def generate_birthday_congratulation():
    builder = BirthdayCongratsBuilder()
    director = CongratsBuilderDirector()
    director.builder = builder

    director.build_long_congrats()

    return builder.congratulation.list_parts()


congrats = {
    CongratulationType.BIRTHDAY_CONGRATS: generate_birthday_congratulation
}


def generate_congratulation(congrats_type: CongratulationType):
    return congrats[congrats_type]()
