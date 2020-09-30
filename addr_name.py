from common_variables import *

##############
#
#   ADDR PERSON CPY
#
############


ABBR = and_(
	length_eq(1),
	is_title()
)

PART = and_(
	TITLE,
	or_(
		gram('Name'),
		gram('Surn')
	)
)

MAYBE_FIO = or_(
	rule(TITLE, PART),
	rule(PART, TITLE),
	rule(ABBR, '.', TITLE),
	rule(ABBR, '.', ABBR, '.', TITLE),
	rule(TITLE, ABBR, '.', ABBR, '.')
)

POSITION_WORDS_ = or_(
	rule(
		dictionary({
			'мичман',
			'геолог',
			'подводник',
			'краевед',
			'снайпер',
			'штурман',
			'бригадир',
			'учитель',
			'политрук',
			'военком',
			'ветеран',
			'историк',
			'пулемётчик',
			'авиаконструктор',
			'адмирал',
			'академик',
			'актер',
			'актриса',
			'архитектор',
			'атаман',
			'врач',
			'воевода',
			'генерал',
			'губернатор',
			'хирург',
			'декабрист',
			'разведчик',
			'граф',
			'десантник',
			'конструктор',
			'скульптор',
			'писатель',
			'поэт',
			'капитан',
			'князь',
			'комиссар',
			'композитор',
			'космонавт',
			'купец',
			'лейтенант',
			'лётчик',
			'майор',
			'маршал',
			'матрос',
			'подполковник',
			'полковник',
			'профессор',
			'сержант',
			'старшина',
			'танкист',
			'художник',
			'герой',
			'княгиня',
			'строитель',
			'дружинник',
			'диктор',
			'прапорщик',
			'артиллерист',
			'графиня',
			'большевик',
			'патриарх',
			'сварщик',
			'офицер',
			'рыбак',
			'брат',
		})
	),
	rule(normalized('генерал'), normalized('армия')),
	rule(('вице'), '-', normalized('адмирал')),
	rule(normalized('герой'), normalized('россия')),
	rule(
		normalized('герой'),
		normalized('российский'), normalized('федерация')),
	rule(
		normalized('герой'),
		normalized('советский'), normalized('союз')
	),
)

ABBR_POSITION_WORDS = rule(
	in_caseless({
		'адм',
		'ак',
		'акад',
		'ген'
	}),
	DOT.optional()
)

POSITION_WORDS = or_(
	POSITION_WORDS_,
	ABBR_POSITION_WORDS
)

MAYBE_PERSON = or_(
	MAYBE_FIO,
	rule(POSITION_WORDS, MAYBE_FIO),
	rule(POSITION_WORDS, TITLE)
)

###########
#
#   IMENI CPY
#
##########


IMENI_WORDS = or_(
	rule(
		caseless('им'),
		DOT.optional()
	),
	rule(caseless('имени'))
)

IMENI = or_(
	rule(
		IMENI_WORDS.optional(),
		MAYBE_PERSON
	),
	rule(
		IMENI_WORDS,
		TITLE
	)
)

##########
#
#   LET CPY
#
##########


LET_WORDS = or_(
	rule(caseless('лет')),
	rule(
		DASH.optional(),
		caseless('летия')
	)
)

LET_NAME = in_caseless({
	'влксм',
	'ссср',
	'алтая',
	'башкирии',
	'бурятии',
	'дагестана',
	'калмыкии',
	'колхоза',
	'комсомола',
	'космонавтики',
	'москвы',
	'октября',
	'пионерии',
	'победы',
	'приморья',
	'района',
	'совхоза',
	'совхозу',
	'татарстана',
	'тувы',
	'удмуртии',
	'улуса',
	'хакасии',
	'целины',
	'чувашии',
	'якутии',
})

LET = rule(
	INT,
	LET_WORDS,
	LET_NAME
)

#########
#
#   MODIFIER CPY
#
############


MODIFIER_WORDS_ = rule(
	dictionary({
		'большой',
		'малый',
		'средний',

		'верхний',
		'центральный',
		'нижний',
		'северный',
		'дальний',

		'первый',
		'второй',

		'старый',
		'новый',

		'красный',
		'лесной',
		'тихий',
	}),
	DASH.optional()
)

ABBR_MODIFIER_WORDS = rule(
	in_caseless({
		'б', 'м', 'н'
	}),
	DOT.optional()
)

SHORT_MODIFIER_WORDS = rule(
	in_caseless({
		'больше',
		'мало',
		'средне',

		'верх',
		'верхне',
		'центрально',
		'нижне',
		'северо',
		'дальне',
		'восточно',
		'западно',

		'перво',
		'второ',

		'старо',
		'ново',

		'красно',
		'тихо',
		'горно',
	}),
	DASH.optional()
)

MODIFIER_WORDS = or_(
	MODIFIER_WORDS_,
	ABBR_MODIFIER_WORDS,
	SHORT_MODIFIER_WORDS,
)

##########
#
#    ADDR DATE CPY
#
#############


MONTH_WORDS = dictionary({
	'январь',
	'февраль',
	'март',
	'апрель',
	'май',
	'июнь',
	'июль',
	'август',
	'сентябрь',
	'октябрь',
	'ноябрь',
	'декабрь',
})

DAY = and_(
	INT,
	gte(1),
	lte(31)
)

YEAR = and_(
	INT,
	gte(1),
	lte(2100)
)

YEAR_WORDS = normalized('год')

DATE = or_(
	rule(DAY, MONTH_WORDS),
	rule(YEAR, YEAR_WORDS)
)

##########
#
#   ADDR NAME IMP
#
##########


ROD = gram('gent')

SIMPLE_NOUN = and_(NOUN, ROD)

COMPLEX = or_(
	rule(
		ADJF,
		NOUN
	),
	rule(
		TITLE,
		DASH.optional(),
		TITLE
	),
)

EXCEPTION = dictionary({
	'арбат',
	'варварка',
	'мельникайте',
	'каховка',
	'зорге',
	'сретенка',
	'макаренко'
})

MAYBE_NAME = or_(
	rule(SIMPLE_NOUN),
	COMPLEX,
	rule(EXCEPTION)
)

NAME = or_(
	MAYBE_NAME,
	LET,
	DATE,
	IMENI
)

NAME = or_(rule(
	MODIFIER_WORDS.optional(),
	NAME),
	rule(MODIFIER_WORDS, ADJF)
)

ADDR_CRF = tag('I').repeatable()

NAME = or_(
	NAME,
	ANUM,
	rule(NAME, ANUM),
	rule(ADJF, ANUM),
	rule(ANUM, NAME),
	rule(ANUM, ADJF),
	rule(INT, DASH.optional(), NAME),
	rule(NAME, DASH, INT),
	ADDR_CRF
)

ADDR_NAME = NAME