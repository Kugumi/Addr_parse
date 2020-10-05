from work_place import *
from streets import *
from settlements import *
from regions import *
from building_values import *
from common_variables import *
from natasha.grammars.addr import GOROD, INDEX, FED_OKRUG, RESPUBLIKA, KRAI, AUTO_OKRUG


# def value(key):
# 	@property
# 	def field(self):
# 		return getattr(self, key)
#
# 	return field


AddrPart = fact(
	'AddrPart',
	['value']
)

work_place_part = fact(
	'AddrPart',
	['value']
)


class work_place_part(AddrPart):
	@property
	def obj(self):
		from natasha import obj

		part = self.value
		return obj.AddrPart(part.value, part.type)


#########
#
#  work_place_part (final rule)
#
##########

WORK_PLACE_PART = or_(
	INDEX,

	GOROD,
	FED_OKRUG,
	RESPUBLIKA,
	KRAI,
	OBLAST,
	AUTO_OKRUG,

	DEREVNYA,
	SELO,
	POSELOK,

	STREET,
	PROSPEKT,
	PROEZD,
	PEREULOK,
	PLOSHAD,
	SHOSSE,
	NABEREG,
	BULVAR,

	DOM,
	KORPUS,
	STROENIE,
	OFIS,
	KVARTIRA,

	ISLAND,
	BC,
	ONLY_NAME_BC,
	FLOOR,
	PLACE,
	ONLY_NUMBER_PLACE,
	SECTOR,
	ROOM,
	CABINET,
	WINDOW,
	RAION,
	ISU,
	ONLY_NUMBER_ISU
).interpretation(
	AddrPart.value
).interpretation(
	AddrPart
)