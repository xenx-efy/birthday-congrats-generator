from abc import ABC, abstractmethod
from typing import Any
import enum
import random


@enum.unique
class CongratulationType(enum.Enum):
    DEFAULT_CONGRATS = enum.auto()
    BIRTHDAY_CONGRATS = enum.auto()


class Congratulation:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: str) -> None:
        self.parts.append(part)

    def list_parts(self) -> str:
        return '\n'.join(self.parts)


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


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


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


class DefaultCongratsData(CongratsData):
    @staticmethod
    def get_intros() -> set:
        return {
            'Поздравляю!',
            'Мои поздравления!',
            'С праздником!'
        }

    @staticmethod
    def get_wishes_intros() -> set:
        return {
            'В этот прекрасный день хочется пожелать',
            'Пусть',
            'Пускай жизнь будет полна',
            'Желаю',
            'Я желаю тебе',
            'Желаю тебе',
        }

    @staticmethod
    def get_enumerations() -> set:
        return {
            'силы духа',
            'упорства',
            'настойчивости',
            'решительности',
            'неординарности',
            'оригинальности',
            'целеустремленности',
            'независимости',
            'уверенности',
            'терпения',
            'жизнелюбия',
            'любознательности',
            'энтузиазма',
            'мудрости',
            'обаяния',
            'спокойствия',
            'притягательности',
            'легкости',
            'удачи',
            'радости',
            'вдохновения',
            'любви',
            'оптимизма',
            'чуткости',
            'активных и насыщенных дней',
            'безоблачного счастья',
            'бескорыстной дружбы',
            'бесценного вкуса жизни',
            'благополучия во всем',
            'бодрости духа',
            'больших успехов',
            'важных и желанных событий',
            'веры в хорошее',
            'весёлых и вкусных пиров',
            'вечной молодости',
            'внимания и заботы',
            'возможности почаще расслабиться',
            'волшебных рассветов',
            'восхитительных закатов',
            'всего наилучшего — и по высшему классу',
            'дерзких планов',
            'доброты и нежности',
            'добрых слов',
            'дома, где любят и ждут',
            'душевного спокойствия',
            'душевной красоты',
            'желания идти вперёд',
            'замечательных друзей',
            'интересных бесед',
            'интересных идей',
            'исполнения всех желаний',
            'исполнения желаний',
            'комфорта и уюта',
            'красивых минут',
            'красивых чувств',
            'крепкого здоровья',
            'крепкого здоровья',
            'кругосветных путешествий',
            'ласки и заботы',
            'ласковой песни прибоя',
            'лёгкого отношения к жизни потрясающих сюрпризов',
            'максимум позитива',
            'много поводов отлично повеселиться',
            'мудрости и опыта',
            'настойчивости и упорства',
            'настоящих друзей',
            'нескучной повседневности',
            'огонька и задора',
            'отличного настроения',
            'отличной формы',
            'побольше свободного времени',
            'подарков и побольше',
            'понимания и поддержки',
            'понимания и тепла',
            'понимания своей уникальности',
            'превосходного самочувствия',
            'превосходных новостей',
            'прекрасного праздника!',
            'прекрасных встреч',
            'приятных людей рядом',
            'приятных открытий',
            'радостей жизни',
            'радужной мечты',
            'свежего ветра',
            'светлой судьбы',
            'сияющего солнца',
            'сказочных мгновений',
            'славы и признания',
            'столько денег, сколько захочется',
            'творчества и созидания',
            'тёплого отношения окружающих',
            'только счастливых случаев',
            'уверенности в себе',
            'увлекательного общения',
            'увлекательной жизни',
            'увлекательных воспоминаний',
            'удачи во всех начинаниях',
            'улыбок фортуны',
            'успехов в работе',
            'фантастического везения',
            'фейерверка эмоций',
            'хорошего настроения',
            'хороших фильмов и книг',
            'хрустальных надежд',
            'цветущих садов и пения птиц',
            'чистого неба',
            'чувства полёта',
            'чувства юмора',
            'широких возможностей',
            'ярких ощущений',
            'ясной улыбки',
            'незабываемых моментов',
        }

    @staticmethod
    def get_prose() -> set:
        return {
            'Чтобы каждое начатое дело заканчивалось успешно',
            'Пусть всё, что казалось несбыточным, сбудется, и самое желанное пусть произойдет',
            'Пусть жизнь наполнится яркими красками, счастливыми моментами и большими купюрами',
            'Пусть удача и везение всегда идут с тобой рядом по жизни',
            'Пусть солнышко сияет в твоих глазах и не покидает тебя в минуты отчаяния',
            'Пусть тебя окружают только добрые люди, верные и преданные друзья, пусть любовь будет взаимной, а жизнь − '
            'радостной, несмотря на непогоду в душе и на улице',
            'Пускай все мечты реализуются легко и просто',
            'Желаю по жизни идти с солнечным настроением и искренней улыбкой, встречать верных друзей и хороших '
            'людей на пути',
            'Жизнь пусть будет наполнена добром и счастьем',
            'Чтобы сбывались самые заветные мечты, а в доме царили уют и гармония',
            'Пусть жизнь будет долгой и гладкой, полной ярких и запоминающихся событий',
            'Пусть жизнь будет наполнена прекрасными моментами',
            'Пусть не будет места для уныния и печалей',
            'Пусть каждый день будет наполнен теплом, и желания сбываются при одной мысли о них',
            'Больше силы, чувств и смелости, чтобы сбывались даже самые необычные желания',
            'Пусть гармония и удача станут твоими повседневными спутниками, и все всегда получается легко '
            'и непринужденно',
        }

    @staticmethod
    def get_endings() -> set:
        return {
            'Всего доброго',
            'До свидания',
            'Еще раз поздравляю',
            'Всех благ',
            'Увидимся'
        }


class BirthdayCongratsData(DefaultCongratsData):
    def get_intros(self) -> set:
        return {
            'С днем рождения!',
            'От всей души поздравляю с днем рождения!',
            'Поздравляю с днем рождения!',
            'В этот замечательный день позволь поздравить тебя с твоим праздником — днем рождения!',
            'С днем рождения поздравляю!',
            'От всей души прими мои самые искренние поздравления с днём рождения!',
            'Принимай поздравления с днём рождения!',
            'Поздравляю!',
            'Хочу пожелать тебе в этот день всего самого хорошего!',
        }


# todo add implementation
class TextGeneratorConfig:
    pass


builder = BirthdayCongratsBuilder()
director = CongratsBuilderDirector()
director.builder = builder

director.build_long_congrats()

congratulation = builder.congratulation.list_parts()

print(congratulation)
