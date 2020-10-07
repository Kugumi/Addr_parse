from parsing_functions import *
from postparsing_functions import *
from preparsing import *
from parser_func import *


def address_parsing(address):
    address = change_punctuation(address)
    address = drop_spaces(address)
    address = simple_changer(address, dictionary={'ё': 'е', 'р . п .': 'рп', ' р п ': 'рп'})
    address = complex_changer(address, change_dict=towns_dict)
    address = complex_changer(address, change_dict=complex_settlements_dict)
    country, ost = addr_part_extractor(s=address, order_list=(1,), names=COUNTRY_KEY_WORDS)
    town, ost = addr_part_extractor(s=ost, names=towns, types=TOWNS_KEY_WORDS, special_names=SPECIAL_TOWNS)
    region, ost = addr_part_extractor(s=ost, names=regions, types=REGIONS_KEY_WORDS, special_names=SPECIAL_REGIONS)
    settlement, ost = settlement_extractor(town, s=ost, names=settlements_list,
                                               types=SETTLEMENT_KEY_WORDS, special_names=settlements_adjf)
    ost, town = levenshtein_towns(ost, town, settlement, towns=towns)

    region_yargy, district, settlement_yargy, street, building, index, place, isnone, ost = yargy_parser(ost)
    region = adder(region, region_yargy)
    settlement = adder(settlement, settlement_yargy)
    ost = remove_duplicate_punctuation(ost)
    street, ost = needs(street, ost, func=yargy_only_street)
    street, ost = needs(street, ost, func=fill_street)
    building, ost = building_parsing(building, ost)

    country = capitalizer(country)
    region = capitalizer(region)
    region = drop_punct(region)
    town = capitalizer(town)
    town = drop_punct(town)
    town = town_words_order(town)
    settlement = capitalizer(settlement)
    settlement = drop_punct(settlement)
    settlement = settlements_changer(settlement)
    settlement = settlement_words_order(settlement)
    street = capitalizer(street)
    building = capitalizer(building)
    place = capitalizer(place)
    ost = alnum_stay(ost)
    country = alnum_stay(country)
    place, ost = kabinet(place, ost)
    place = space_dot(place)
    result_string = union(country, region, town, settlement, district, street,
                          building, place, index)
    return country, region, town, settlement, district, street, building, place, index, result_string
