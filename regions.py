from value_func import value
from common_variables import *
from gender_relation import gender

Region = fact(
	'Region',
	['name', 'type']
)


class Region(Region):
	value = value('name')


############
#
#    OBLAST IMP
#
############


OBLAST_WORDS = or_(
	rule(normalized('область')),
	rule(
		caseless('обл'),
		DOT.optional()
	)
).interpretation(
	Region.type.const('область')
)

OBLAST_NAME = dictionary({
	'амурский',
	'архангельский',
	'астраханский',
	'белгородский',
	'брянский',
	'владимирский',
	'волгоградский',
	'вологодский',
	'воронежский',
	'горьковский',
	'ивановский',
	'ивановский',
	'иркутский',
	'калининградский',
	'калужский',
	'камчатский',
	'кемеровский',
	'кировский',
	'костромской',
	'курганский',
	'курский',
	'ленинградский',
	'липецкий',
	'магаданский',
	'московский',
	'мурманский',
	'нижегородский',
	'новгородский',
	'новосибирский',
	'омский',
	'оренбургский',
	'орловский',
	'пензенский',
	'пермский',
	'псковский',
	'ростовский',
	'рязанский',
	'самарский',
	'саратовский',
	'сахалинский',
	'свердловский',
	'смоленский',
	'тамбовский',
	'тверской',
	'томский',
	'тульский',
	'тюменский',
	'ульяновский',
	'челябинский',
	'читинский',
	'ярославский',
}).interpretation(
	Region.name
)

OBLAST = or_(
	rule(OBLAST_NAME, OBLAST_WORDS),
	rule(OBLAST_WORDS, OBLAST_NAME)
).interpretation(
	Region
)

##########
#
#  RAION IMP
#
###########


RAION_WORDS = or_(
	rule(caseless('р'), '-', in_caseless({'он', 'н'})),
	rule(caseless('мрн')),
	rule(caseless('мкр')),
	rule(normalized('район')),
	rule(normalized('микрорайон'))
).interpretation(
	Region.type.const('район')
)

RAION_SIMPLE_NAME = and_(
	ADJF
).match(gender)

RAION_MODIFIERS = rule(
	in_caseless({
		'усть',
		'северо',
		'александрово',
		'гаврилово',
	}),
	DASH.optional()
)

RAION_COMPLEX_NAME = rule(
	RAION_MODIFIERS,
	RAION_SIMPLE_NAME
)

RAION_NAME = or_(
	rule(RAION_SIMPLE_NAME),
	RAION_COMPLEX_NAME
).interpretation(
	Region.name
)

RAION = or_(
	rule(RAION_NAME, RAION_WORDS),
	rule(RAION_WORDS, RAION_NAME)
).interpretation(
	Region
)