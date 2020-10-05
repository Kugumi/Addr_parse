from value_func import value
from settlement_name import SETTLEMENT_NAME
from common_variables import *

Settlement = fact(
	'Settlement',
	['name', 'type']
)


class Settlement(Settlement):
	value = value('name')


###########
#
#   SELO CPY
#
#############

SELO_WORDS = or_(
	rule(
		caseless('с'),
		DOT.optional()
	),
	rule(normalized('село'))
).interpretation(
	Settlement.type.const('село')
)

SELO_NAME = SETTLEMENT_NAME.interpretation(
	Settlement.name
)

SELO = rule(
	SELO_WORDS,
	SELO_NAME
).interpretation(
	Settlement
)

###########
#
#   DEREVNYA IMP
#
#############

DEREVNYA_WORDS = or_(
	rule(
		caseless('д'),
		DOT.optional()
	),
	rule(
		caseless('ст'),
		DOT.optional()
	),
	rule(caseless('ст'), '-', in_caseless({'ца', 'ица'})),
	rule(normalized('деревня')),
	rule(normalized('станица'))
).interpretation(
	Settlement.type.const('деревня')
)

DEREVNYA_NAME = SETTLEMENT_NAME.interpretation(
	Settlement.name
)

DEREVNYA = rule(
	DEREVNYA_WORDS,
	DEREVNYA_NAME
).interpretation(
	Settlement
)

###########
#
#   POSELOK IMP
#
#############

POSELOK_WORDS = or_(
	rule(
		in_caseless({'п', 'пос'}),
		DOT.optional()
	),
	rule(normalized('посёлок')),
	rule(
		caseless('р'),
		DOT.optional(),
		caseless('п'),
		DOT.optional()
	),
	rule(
		caseless('рп'),
		DOT.optional()
	),
	rule(
		normalized('рабочий'),
		normalized('посёлок')
	),
	rule(
		caseless('пгт'),
		DOT.optional()
	),
	rule(
		caseless('п'), DOT, caseless('г'), DOT, caseless('т'),
		DOT.optional()
	),
	rule(
		normalized('посёлок'),
		normalized('городского'),
		normalized('типа'),
	),
).interpretation(
	Settlement.type.const('посёлок')
)

POSELOK_NAME = SETTLEMENT_NAME.interpretation(
	Settlement.name
)

POSELOK = rule(
	POSELOK_WORDS,
	POSELOK_NAME
).interpretation(
	Settlement
)

###########
#
#   ISLAND
#
#############


ISLAND_WORDS = or_(
	rule(
		caseless('о'),
		DOT
	),
	rule(normalized('остров'))
).interpretation(
	Settlement.type.const('остров')
)

ISLAND_NAME = SETTLEMENT_NAME.interpretation(
	Settlement.name
)

ISLAND = rule(
	ISLAND_WORDS,
	ISLAND_NAME
).interpretation(
	Settlement
)