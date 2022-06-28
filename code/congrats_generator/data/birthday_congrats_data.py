from ..data.default_congrats_data import DefaultCongratsData


class BirthdayCongratsData(DefaultCongratsData):
    def get_intros(self) -> set:
        return {
            "С днем рождения!",
            "От всей души поздравляю с днем рождения!",
            "Поздравляю с днем рождения!",
            "В этот замечательный день позволь поздравить тебя с твоим праздником — днем рождения!",
            "С днем рождения поздравляю!",
            "От всей души прими мои самые искренние поздравления с днём рождения!",
            "Принимай поздравления с днём рождения!",
            "Поздравляю!",
            "Хочу пожелать тебе в этот день всего самого хорошего!",
        }
