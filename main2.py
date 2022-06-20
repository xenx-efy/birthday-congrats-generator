from abc import ABC, abstractmethod
from typing import Any


class Congratulation:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"{''.join(self.parts)}")


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
        self.builder.generate_intro(None)

    def build_long_congrats(self):
        pass


class BirthdayCongratsBuilder(CongratsBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._congratulation = Congratulation()

    @property
    def congratulation(self) -> Congratulation:
        return self._congratulation

    def generate_intro(self, generator_config) -> None:
        pass

    def generate_enumeration(self, generator_config) -> None:
        pass

    def generate_prose(self, generator_config) -> None:
        pass

    def generate_ending(self, generator_config) -> None:
        pass


class CongratsData:
    @staticmethod
    def get_intros() -> set:
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


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DefaultCongratsData(CongratsData, metaclass=SingletonMeta):
    @staticmethod
    def get_intros() -> set:
        return {
            'Поздравляю!',
            'Мои поздравления!',
            'С праздником!'
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
            'чтобы каждое начатое дело заканчивалось успешно',
            'Пусть всё, что казалось несбыточным, сбудется, и самое желанное пусть произойдет!',
            'Пусть жизнь наполнится яркими красками, счастливыми моментами и большими купюрами!',
            'Пусть удача и везение всегда идут с тобой рядом по жизни.',
            'Пусть солнышко сияет в твоих глазах и не покидает тебя в минуты отчаяния!',
            'Пусть тебя окружают только добрые люди, верные и преданные друзья, пусть любовь будет взаимной, а жизнь − '
            'радостной, несмотря на непогоду в душе и на улице.',
            'Пускай все мечты реализуются легко и просто.',
            'Желаю по жизни идти с солнечным настроением и искренней улыбкой, встречать верных друзей и хороших людей на пути.',
            'Жизнь пусть будет наполнена добром и счастьем!',
            'Чтобы сбывались самые заветные мечты, а в доме царили уют и гармония.',
            'Пусть жизнь будет долгой и гладкой, полной ярких и запоминающихся событий!',
            'Пусть жизнь будет наполнена прекрасными моментами.',
            'Пусть не будет места для уныния и печалей!',
            'Пусть каждый день будет наполнен теплом, и желания сбываются при одной мысли о них.',
            'Больше силы, чувств и смелости, чтобы сбывались даже самые необычные желания!',
            'Пусть гармония и удача станут твоими повседневными спутниками, и все всегда получается легко и непринужденно!',
        }

    @staticmethod
    def get_endings() -> set:
        return {
            'Всего доброго!',
            'До свидания.',
            'Еще раз поздравляю.',
            'Всех благ!',
            'Увидимся.'
        }


class CongratsDataDecorator(CongratsData):
    _congrats_data: CongratsData = None

    def __init__(self, congrats_data: CongratsData) -> None:
        self._congrats_data = congrats_data

    @property
    def congrats_data(self) -> CongratsData:
        return self._congrats_data

    def get_intros(self) -> set:
        return self._congrats_data.get_intros()

    def get_enumerations(self) -> set:
        return self._congrats_data.get_enumerations()

    def get_prose(self) -> set:
        return self._congrats_data.get_prose()

    def get_endings(self) -> set:
        return self._congrats_data.get_endings()


class BirthdayCongratsDataDecorator(CongratsDataDecorator):
    def get_intros(self) -> set:
        return self._congrats_data.get_intros().union({
            'С днем рождения!',
            'От всей души поздравляю с днем рождения!',
            'Поздравляю с днем рождения!',
            'В этот замечательный день позволь поздравить тебя с твоим праздником — днем рождения!',
            'С днем рождения поздравляю!',
            'От всей души прими мои самые искренние поздравления с днём рождения!',
            'Принимай поздравления с днём рождения!',
            'Поздравляю!',
            'Хочу пожелать тебе в этот день всего самого хорошего!',
        })

    def get_enumerations(self) -> set:
        return self._congrats_data.get_enumerations()

    def get_prose(self) -> set:
        return self._congrats_data.get_prose()

    def get_endings(self) -> set:
        return self._congrats_data.get_endings()


class Factory:
    @abstractmethod
    def create(self):
        pass


class CongratsDataFactory(Factory):
    def create(self):


# todo add implementation
class TextGeneratorConfig:
    pass
