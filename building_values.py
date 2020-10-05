from general import ADDR_VALUE
from value_func import value
from common_variables import *

Building = fact(
	'Building',
	['number', 'type']
)

Room = fact(
	'Room',
	['number', 'type']
)


class Building(Building):
	value = value('number')


class Room(Room):
	value = value('number')


############
#
#    DOM IMP
#
#############


DOM_WORDS = or_(
	rule(normalized('дом')),
	rule(
		caseless('д'),
		DOT.optional()
	)
).interpretation(
	Building.type.const('дом')
)

DOM_VALUE = ADDR_VALUE.interpretation(
	Building.number
)

DOM = rule(
	DOM_WORDS,
	DOM_VALUE
).interpretation(
	Building
)

###########
#
#  KORPUS IMP
#
##########


KORPUS_WORDS = or_(
	rule(
		in_caseless({'корп', 'кор'}),
		DOT.optional()
	),
	rule(normalized('корпус'))
).interpretation(
	Building.type.const('корпус')
)

KORPUS_VALUE = or_(rule(ADDR_VALUE).interpretation(
	Building.number),
	rule(LETTERS).interpretation(
		Building.number)
)

KORPUS = rule(
	KORPUS_WORDS,
	KORPUS_VALUE
).interpretation(
	Building
)

###########
#
#  STROENIE IMP
#
##########


STROENIE_WORDS = or_(
	rule(
		caseless('стр'),
		DOT.optional()
	),
	rule(normalized('строение'))
).interpretation(
	Building.type.const('строение')
)

STROENIE_VALUE = ADDR_VALUE.interpretation(
	Building.number
)

STROENIE = rule(
	STROENIE_WORDS,
	STROENIE_VALUE
).interpretation(
	Building
)

###########
#
#   OFIS CPY
#
#############


OFIS_WORDS = or_(
	rule(
		caseless('оф'),
		DOT.optional()
	),
	rule(normalized('офис'))
).interpretation(
	Room.type.const('офис')
)

OFIS_VALUE = ADDR_VALUE.interpretation(
	Room.number
)

OFIS = rule(
	OFIS_WORDS,
	OFIS_VALUE
).interpretation(
	Room
)

###########
#
#   KVARTIRA CPY
#
#############


KVARTIRA_WORDS = or_(
	rule(
		caseless('кв'),
		DOT.optional()
	),
	rule(normalized('квартира'))
).interpretation(
	Room.type.const('квартира')
)

KVARTIRA_VALUE = ADDR_VALUE.interpretation(
	Room.number
)

KVARTIRA = rule(
	KVARTIRA_WORDS,
	KVARTIRA_VALUE
).interpretation(
	Room
)