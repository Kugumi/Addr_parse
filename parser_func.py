from yargy import Parser
from general import WORK_PLACE_PART


def yargy_parser(text, parser=Parser(WORK_PLACE_PART)):
	region = ''
	district = ''
	settlement = ''
	street = ''
	building = ''
	index = ''
	place = ''
	isnone = ''
	deleted_addr_parts = text
	i = 0

	tmp_one_place_list = []
	building_list = []
	work_place_list = ['БЦ', 'АЛЦ', 'окно', 'ряд', 'бокс', 'место', 'кабинет', 'этаж', 'Отделение', 'ВСП/ДО', 'сектор',
					   'Блок', 'комната']
	street_list = ['улица', 'проспект', 'проезд', 'переулок', 'площадь', 'шоссе', 'набережная', 'бульвар']

	for match in parser.findall(text):
		if not match.fact.value.type is None:
			deleted_addr_parts = deleted_addr_parts[0: match.span.start - i] + deleted_addr_parts[match.span.stop - i:]
			i += match.span.stop - match.span.start
		if match.fact.value.type in work_place_list:
			tmp_one_place_list.append(match.fact.value.type)
			tmp_one_place_list.append(match.fact.value.value)
			place = ' '.join(tmp_one_place_list)
		elif match.fact.value.type in ('федеральный округ', 'республика', 'край', 'область', 'автономный округ'):
			region = match.fact.value.type + ' ' + match.fact.value.name
		elif match.fact.value.type == 'район':
			district = match.fact.value.name + ' ' + match.fact.value.type
		elif match.fact.value.type in ('остров', 'село', 'деревня', 'посёлок'):
			settlement = match.fact.value.type + ' ' + match.fact.value.name
		elif match.fact.value.type in street_list:
			street = match.fact.value.type + ' ' + match.fact.value.name
		elif match.fact.value.type in ('дом', 'корпус', 'строение', 'офис', 'квартира'):
			building_list.append(match.fact.value.type)
			building_list.append(match.fact.value.number)
			building = " ".join(building_list)
		elif match.fact.value.type == 'индекс':
			index = match.fact.value.value
		elif match.fact.value.type is None:
			isnone = match.fact.value.value

	return region, district, settlement, street, building, index, place, isnone, deleted_addr_parts

print(yargy_parser("привет"))