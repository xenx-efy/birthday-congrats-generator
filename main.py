import random

intros: list = [
    'С днем рождения!',
    'От всей души поздравляю с днем рождения!',
    'Поздравляю с днем рождения!',
    'В этот замечательный день позволь поздравить тебя с твоим праздником — днем рождения!',
    'С днем рождения поздравляю!',
    'От всей души прими мои самые искренние поздравления с днём рождения!',
    'Принимай поздравления с днём рождения!',
    'Поздравляю!',
    'Хочу пожелать тебе в этот день всего самого хорошего!',
]

# for future
introsWithContinuation: list = [
    'В этот прекрасный день желаю',
    'Хочу поздравить тебя с Днём рождения и пожелать',
]

wishesIntros: list = [
    'В этот прекрасный день хочется пожелать',
    'Пусть',
    'Пускай жизнь будет полна',
    'Желаю',
    'Я желаю тебе',
    'Желаю тебе',
]

onePhraseWishes: list = [
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
]

extraordinaryWishes: list = [
    'чтобы зубы не болели',
    'чтобы раковина не засорялась',
    'чтобы квартира не пылилась',
    'чтобы омывайка не замерзала',
    'чтобы всегда был 4g',
    'чтобы легко вставалось по утрам',
    'чтобы елось и не толстелось никогда',
    'чтобы всегда была горячая вода',
    'чтобы было побольше котиков в твоей жизни',
]

bydloCongrats: list = [
    'сдр',
    'с др!',
]

longWishes: list = [
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
]


def get_intro() -> str:
    return random.choice(intros)


def get_wishes() -> str:
    return '{0} {1}'.format(random.choice(wishesIntros),
                            generate_wishes_enumeration(random.choices(onePhraseWishes, k=4)))


def generate_wishes_enumeration(wishes_list):
    return '{0} и {1}.'.format(','.join(wishes_list[:-1]), wishes_list[-1])


def get_long_wish():
    return random.choice(longWishes)


def get_extraordinary_wish():
    return random.choice(extraordinaryWishes)


def get_long_wish_with_extraordinary():
    return '{0} и {1}'.format(get_extraordinary_wish(), get_long_wish())


congrats = get_intro() + get_wishes() + get_long_wish_with_extraordinary()
print(congrats)
# def get_single_wish
# def get_wishes(cnt)