from settlements import Settlement
from gender_relation import gender
from common_variables import *
from general import value
from addr_name import ADDR_NAME

Street = fact(
	'Street',
	['name', 'type']
)


class Street(Settlement):
	value = value('name')


########
#
#    STREET IMP
#
#########

STREET_WORDS = or_(
	rule(normalized('улица')),
	rule(
		caseless('ул'),
		DOT.optional()
	)
).interpretation(
	Street.type.const('улица')
).match(gender)

STREET_NAME = or_(rule(ADJF).interpretation(
	Street.name).match(gender),
				  rule(ADDR_NAME).interpretation(
					  Street.name)
				  )

STREET = or_(
	rule(STREET_WORDS, STREET_NAME),
	rule(STREET_NAME, STREET_WORDS)
).interpretation(
	Street
)

##########
#
#    PROSPEKT IMP
#
##########

PROSPEKT_WORDS = or_(
	rule(
		in_caseless({'пр', 'просп'}),
		DOT.optional()
	),
	rule(
		caseless('пр'),
		'-',
		in_caseless({'кт', 'т'}),
		DOT.optional()
	),
	rule(normalized('проспект'))
).interpretation(
	Street.type.const('проспект')
).match(gender)

PROSPEKT_NAME = or_(rule(ADJF).interpretation(
	Street.name).match(gender),
					rule(ADDR_NAME).interpretation(
						Street.name)
					)

PROSPEKT = or_(
	rule(PROSPEKT_WORDS, PROSPEKT_NAME),
	rule(PROSPEKT_NAME, PROSPEKT_WORDS)
).interpretation(
	Street
)

############
#
#    PROEZD IMP
#
#############


PROEZD_WORDS = or_(
	rule(caseless('пр'), DOT.optional()),
	rule(
		caseless('пр'),
		'-',
		in_caseless({'зд', 'д'}),
		DOT.optional()
	),
	rule(normalized('проезд'))
).interpretation(
	Street.type.const('проезд')
).match(gender)

PROEZD_NAME = or_(rule(ADJF).interpretation(
	Street.name).match(gender),
				  rule(ADDR_NAME).interpretation(
					  Street.name)
				  )

PROEZD = or_(
	rule(PROEZD_WORDS, PROEZD_NAME),
	rule(PROEZD_NAME, PROEZD_WORDS)
).interpretation(
	Street
)

###########
#
#   PEREULOK IMP
#
##############


PEREULOK_WORDS = or_(
	rule(
		caseless('п'),
		DOT
	),
	rule(
		caseless('пер'),
		DOT.optional()
	),
	rule(normalized('переулок'))
).interpretation(
	Street.type.const('переулок')
).match(gender)

PEREULOK_NAME = or_(rule(ADJF).interpretation(
	Street.name).match(gender),
					rule(ADDR_NAME).interpretation(
						Street.name)
					)

PEREULOK = or_(
	rule(PEREULOK_WORDS, PEREULOK_NAME),
	rule(PEREULOK_NAME, PEREULOK_WORDS)
).interpretation(
	Street
)

########
#
#  PLOSHAD IMP
#
##########


PLOSHAD_WORDS = or_(
	rule(
		caseless('пл'),
		DOT.optional()
	),
	rule(normalized('площадь'))
).interpretation(
	Street.type.const('площадь')
).match(gender)

PLOSHAD_NAME = or_(rule(ADJF).interpretation(
	Street.name).match(gender),
				   rule(ADDR_NAME).interpretation(
					   Street.name)
				   )

PLOSHAD = or_(
	rule(PLOSHAD_WORDS, PLOSHAD_NAME),
	rule(PLOSHAD_NAME, PLOSHAD_WORDS)
).interpretation(
	Street
)

########
#
#  ADDR VALUE IMP
#
##########

LETTER = or_(
	rule(LETTER),
	rule(QUOTE, LETTER, QUOTE)
)

VALUE = rule(
	INT,
	LETTER.optional()
)

SEP = in_(r'/\-')

VALUE = or_(
	rule(VALUE),
	rule(VALUE, SEP, VALUE),
	rule(VALUE, SEP, LETTER),
)

ADDR_VALUE = rule(
	eq('№').optional(),
	VALUE
)

############
#
#   SHOSSE IMP
#
###########

SHOSSE_WORDS = or_(
	rule(
		caseless('ш'),
		DOT.optional()
	),
	rule(normalized('шоссе'))
).interpretation(
	Street.type.const('шоссе')
).match(gender)

SHOSSE_NAME = or_(rule(ADJF).interpretation(
	Street.name).match(gender),
				  rule(ADDR_NAME).interpretation(
					  Street.name)
				  )

SHOSSE = or_(
	rule(SHOSSE_NAME, SHOSSE_WORDS),
	rule(SHOSSE_WORDS, SHOSSE_NAME)
).interpretation(
	Street
)

########
#
#  NABEREG IMP
#
##########


NABEREG_WORDS = or_(
	rule(
		caseless('наб'),
		DOT.optional()
	),
	rule(normalized('набережная'))
).interpretation(
	Street.type.const('набережная')
).match(gender)

NABEREG_NAME = or_(rule(ADJF).interpretation(
	Street.name).match(gender),
				   rule(ADDR_NAME).interpretation(
					   Street.name)
				   )

NABEREG = or_(
	rule(NABEREG_WORDS, NABEREG_NAME),
	rule(NABEREG_NAME, NABEREG_WORDS)
).interpretation(
	Street
)

########
#
#  BULVAR IMP
#
##########


BULVAR_WORDS = or_(
	rule(
		caseless('б'),
		'-',
		caseless('р'),
		DOT.optional()
	),
	rule(
		caseless('б'),
		DOT
	),
	rule(
		caseless('бул'),
		DOT.optional()
	),
	rule(normalized('бульвар'))
).interpretation(
	Street.type.const('бульвар')
).match(gender)

BULVAR_NAME = or_(rule(ADJF).interpretation(
	Street.name).match(gender),
				  rule(ADDR_NAME).interpretation(
					  Street.name)
				  )

BULVAR = or_(
	rule(BULVAR_WORDS, BULVAR_NAME),
	rule(BULVAR_NAME, BULVAR_WORDS)
).interpretation(
	Street
)