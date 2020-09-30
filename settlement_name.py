from common_variables import *

##########
#
#  SETTLEMENT NAME IMP
#
##########

ADJS = gram('ADJS')
SIMPLE = or_(
	NOUN,  # Александровка, Заречье, Горки
	ADJS,  # Кузнецово
	ADJF,  # Никольское, Новая, Марьино
)

COMPLEX = rule(
	SIMPLE,
	DASH.optional(),
	SIMPLE
)

NAME = or_(
	rule(SIMPLE),
	COMPLEX
)

SETTLEMENT_NAME = or_(
	NAME,
	rule(NAME, '-', INT),
	rule(NAME, ANUM)
)