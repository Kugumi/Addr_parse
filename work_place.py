from settlements import Settlement
#from general import value
from value_func import value
from common_variables import *
from yargy.pipelines import morph_pipeline

OnlyNameBC = fact(
    'OnlyNameBC',
    ['name']
)

OnlyNumberIsu = fact(
    'OnlyNumberIsu',
    ['number']
)

OnlyNumberPlace = fact(
    'OnlyNumberPlace',
    ['number']
)

work_place = fact(
    'work_place',
    ['number', 'type']
)


class OnlyNameBC(OnlyNameBC):
    type = 'БЦ'
    value = value('name')


class OnlyNumberIsu(OnlyNumberIsu):
	type = 'ВСП/ДО'
	value = value('number')


class OnlyNumberPlace(OnlyNumberPlace):
	type = 'место'
	value = value('number')


class work_place(work_place):
	value = value('number')


#########
#
#  BC
#
##########

SIMPLE_BC = or_(
	NOUN,
	ADJF
)

COMPLEX_BC = morph_pipeline([
    'poklonka place',
    'президент плаза',
    'поклонка плейс',
    'северное сияние',
    'даниловская мануфактура',
    'даниловский форт',
    'корпус кнопа',
    'чайка плаза',
    'романов двор-2',
    'золотая долина',
    'Фаберже 8'
])

COMPLEX_BC_WORDS = morph_pipeline([
    'бизнес-центр',
    'бизнес центр',
    'бизнес-парк'
])

COMPLEX_ALC_WORDS = morph_pipeline([
    'архивно-логистический центр'
])

SIMPLE_BC_KNOWN = dictionary({
    'кнопа',
    'ртс',
    'Чайка',
    'сенатор'
})

BC_ABBR = in_caseless({
    'ДМ'
})

ONLY_NAME_BC = or_(
    COMPLEX_BC,
    rule(SIMPLE_BC_KNOWN)
).interpretation(
    OnlyNameBC.name
).interpretation(
    OnlyNameBC
)

BC_NAME = or_(
    rule(SIMPLE_BC_KNOWN),
    rule(BC_ABBR),
    rule(QUOTE, SIMPLE_BC_KNOWN, QUOTE),
    rule(QUOTE, COMPLEX_BC, QUOTE),
    rule(QUOTE, BC_ABBR, QUOTE),
    rule(QUOTE, SIMPLE_BC, QUOTE),
    rule(SIMPLE_BC),
    rule(COMPLEX_BC)
).interpretation(
    Settlement.name
)

BC_WORDS = or_(
    rule(caseless('бц'),
         DOT.optional()),
    COMPLEX_BC_WORDS
).interpretation(
    Settlement.type.const('БЦ')
)

ALC_WORDS = or_(
    rule(caseless('алц'),
         DOT.optional()),
    COMPLEX_ALC_WORDS
).interpretation(
    Settlement.type.const('АЛЦ')
)

BC = or_(
    rule(BC_WORDS, BC_NAME),
    rule(
        COMPLEX_BC_WORDS,
        BC_NAME
    ),
    rule(ALC_WORDS, BC_NAME),
    rule(
        COMPLEX_ALC_WORDS,
        BC_NAME
    )
).interpretation(
    Settlement
)

#########
#
#  Floor
#
##########

FLOORNAME = rule(caseless('этаж')
                 ).interpretation(
    work_place.type.const('этаж'))

FLOOR_NUMBER = NUMBER.interpretation(
    work_place.number
)

FLOOR = rule(
    FLOORNAME,
    FLOOR_NUMBER
).interpretation(
    work_place
)

#########
#
#  Cabinet
#
##########


CABNAME = or_(
    rule(caseless('кабинет')),
    rule(
        caseless('каб'),
        DOT.optional()
    ),
    rule(
        caseless('к'),
        DOT
    )
).interpretation(
    work_place.type.const('кабинет')
)

CAB_NUMBER = NUMBER.interpretation(
    work_place.number
)

CABINET = rule(
    CABNAME,
    CAB_NUMBER
).interpretation(
    work_place
)

#########
#
#  Sector
#
##########

DOT_INT = rule(DOT, INT)

BLOCKNAME = or_(
    rule(caseless('блок')),
    rule(caseless('башня'))
).interpretation(
    work_place.type.const('Блок'))

SECTORNAME = or_(
    rule(caseless('сектор')),
    rule(caseless('секция')),
    rule(caseless('помещение')),
    rule(caseless('пом'), DOT.optional()),
).interpretation(
    work_place.type.const('сектор'))

COMPLEX_SECTORNAME = morph_pipeline([
    'доп.помещение',
    'дополнительное помещение',
    'служебное помещение'
])

LETTERS_OPT_INT = or_(
    rule(LETTER, INT.optional()),
    rule(LETTER_LATIN, INT.optional())
)

LETTERS_INT = or_(
    rule(LETTER, INT),
    rule(LETTER_LATIN, INT)
)

LETTERS_INTS = rule(LETTERS_OPT_INT, DOT_INT)

QUOTE_LETTER_INT = rule(
    QUOTE, LETTERS_OPT_INT, QUOTE
)

SECTOR_NUMBER = or_(
    rule(QUOTE_LETTER_INT),
    rule(LETTERS_INT, DOT_INT.optional()),
    rule(LETTERS_OPT_INT),
    rule(LETTERS, DOT_INT),
    rule(INT, DOT_INT, DOT_INT.optional()),
    rule(SIMPLE_NUMBER),
    rule(SIMPLE_NUMBER, SEP, SIMPLE_NUMBER),
    rule(SIMPLE_NUMBER, SEP, LETTERS)
).interpretation(
    work_place.number
)

SECTOR = or_(
    rule(SECTORNAME,
         eq('№').optional(), SECTOR_NUMBER),
    rule(BLOCKNAME,
         eq('№').optional(), SECTOR_NUMBER),
    rule(COMPLEX_SECTORNAME,
         eq('№').optional(), SECTOR_NUMBER),
).interpretation(
    work_place
)

#########
#
#  Room
#
##########

ROOMNAME = or_(
    rule(caseless('комната')),
    rule(caseless('ком'),
         DOT.optional()),
    rule(caseless('комн'),
         DOT.optional())
).interpretation(
    work_place.type.const('комната'))

ROOM_NUMBER = or_(
    rule(LETTERS_INT),
    rule(INT, DOT_INT, DOT_INT.optional()),
    rule(SIMPLE_NUMBER)
).interpretation(
    work_place.number
)

ROOM = rule(
    ROOMNAME,
    eq('№').optional(), ROOM_NUMBER
).interpretation(
    work_place
)

#########
#
#  Window
#
##########

ROWNAME = rule(caseless('ряд')
               ).interpretation(
    work_place.type.const('ряд'))

WINDOWNAME = rule(normalized('окно')
                  ).interpretation(
    work_place.type.const('окно'))

BOXNAME = rule(('бокс')
               ).interpretation(
    work_place.type.const('бокс'))

WINDOW_NUMBER = NUMBER.interpretation(
    work_place.number
)

WINDOW = or_(
    rule(WINDOWNAME,
         WINDOW_NUMBER),
    rule(ROWNAME, WINDOW_NUMBER),
    rule(BOXNAME,
         WINDOW_NUMBER),
).interpretation(
    work_place
)

#########
#
#  ВСП
#
##########

INT_FOUR = and_(INT,
                length_eq(4))

ONLY_NUMBER_ISU = rule(
    INT_FOUR,
    SLASH,
    INT
).interpretation(
    OnlyNumberIsu.number
).interpretation(
    OnlyNumberIsu
)

BRANCHNAME = or_(rule(ADJF.optional(), caseless('отделение')),
                 rule(caseless('ОСБ')),
                 rule(caseless('ВОСБ')),
                 rule(caseless('ГОСБ'))
                 ).interpretation(
    work_place.type.const('Отделение'))

COMPLEX_ISUNAME = morph_pipeline([
    'дополнительный офис',
    'доп.офис',
    'Д/О'
])

ISUNAME = or_(
    rule(caseless('ВСП')),
    rule(caseless('ДО')),
    rule(
        caseless('д'),
        DOT.optional(),
        caseless('о'),
        DOT.optional()
    ),
    rule(caseless('УДО')),
    rule(caseless('СДО')),
    rule(caseless('ДФ')),
    COMPLEX_ISUNAME
).interpretation(
    work_place.type.const('ВСП/ДО'))

ISU_NUMBER = or_(
    rule(SIMPLE_NUMBER),
    rule(SIMPLE_NUMBER, SEP, SIMPLE_NUMBER),
    rule(SIMPLE_NUMBER, SEP, LETTERS),
).interpretation(
    work_place.number
)

COMPLEX_ISU = rule(COMPLEX_ISUNAME,
                   eq('№').optional(),
                   ISU_NUMBER)

ISU = or_(
    rule(ISUNAME,
         eq('№').optional(),
         ISU_NUMBER),
    rule(BRANCHNAME,
         eq('№').optional(),
         ISU_NUMBER),
    rule(COMPLEX_ISU)
).interpretation(
    work_place
)

#########
#
#  Place
#
##########

COMPLEX_PLACENAME = morph_pipeline([
    'рабочее место',
    'раб.место',
    'р/м'
])

PLACENAME = or_(
    rule(normalized('место')),
    rule(
        caseless('мес'),
        DOT.optional()
    ),
    rule(caseless('м'), DOT),
    rule(caseless('рм'), DOT.optional()),
    rule(
        caseless('р'),
        DOT.optional(),
        caseless('м'),
        DOT.optional()
    ),
    COMPLEX_PLACENAME
).interpretation(
    work_place.type.const('место'))

PLACE_NUMBER = or_(
    rule(LETTERS, DOT_INT, DOT_INT),
    rule(INT, DOT_INT, DOT_INT.optional()),
    rule(LETTERS_INT, DOT_INT.optional()),
    rule(SIMPLE_NUMBER),
    rule(SIMPLE_NUMBER, SEP, SIMPLE_NUMBER),
    rule(SIMPLE_NUMBER, SEP, LETTERS)
).interpretation(
    work_place.number
)

COMPLEX_PLACE = rule(COMPLEX_PLACENAME,
                     eq('№').optional(),
                     PLACE_NUMBER)

PLACE = or_(
    rule(PLACENAME,
         eq('№').optional(),
         PLACE_NUMBER),
    COMPLEX_PLACE
).interpretation(
    work_place
)

ONLY_NUMBER_PLACE = or_(
    rule(INT, DOT_INT, DOT_INT.optional()),  # 10.10.10
    rule(LETTERS_INTS, DOT_INT.optional()),  # B2.10.10 , B.10.10, B2.10
    rule(INT, DOT, LETTERS_INTS),  # 10.B10.10, 10.B.10
    rule(LETTERS_INTS, DOT_INT, DOT_INT.optional()),  # B2.10.10, B.10.10, B2.10.10.10, B.10.10.10
    rule(INT, DOT, LETTERS, DOT_INT, DOT_INT.optional()),  # 10.B.10, 10.B.10.10
).interpretation(
    OnlyNumberPlace.number
).interpretation(
    OnlyNumberPlace
)