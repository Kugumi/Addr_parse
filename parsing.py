from parsing_functions import *
from postparsing_functions import *
from preparsing import *
from parser_func import *


def address_parsing(address):
    address = change_punctuation(address)
    address = drop_spaces(address)
    # print(address)
    address = simple_changer(address, dictionary={'ё': 'е', ' р . п . ': ' рп ', 'р . п ': 'рп ', ' р п ': ' рп '})
    # print(address)
    address = complex_changer(address, change_dict=towns_dict)
    address = complex_changer(address, change_dict=complex_settlements_dict)
    # print(address)
    country, ost = addr_part_extractor(s=address, order_list=(1,), names=COUNTRY_KEY_WORDS)
    # print("ost1: " + ost)
    # print(towns_list)
    town, ost = addr_part_extractor(s=ost, names=towns_list, types=TOWNS_KEY_WORDS, special_names=SPECIAL_TOWNS)
    # print("ost2: " + ost)
    region, ost = addr_part_extractor(s=ost, names=regions, types=REGIONS_KEY_WORDS, special_names=SPECIAL_REGIONS)
    # print("ost3: " + ost)
    settlement, ost = settlement_extractor(town, s=ost, names=settlements_list,
                                               types=SETTLEMENT_KEY_WORDS, special_names=settlements_adjf)
    # print("ost3ю5: " + ost)
    ost, town = levenshtein_towns(ost, town, settlement, towns=towns)

    region_yargy, district, settlement_yargy, street, building, index, place, isnone, ost = yargy_parser(ost)
    # print("ost4: " + ost)
    region = adder(region, region_yargy)
    settlement = adder(settlement, settlement_yargy)
    ost = remove_duplicate_punctuation(ost)
    street, ost = needs(street, ost, func=yargy_only_street)
    # print("ost5: " + ost)
    street, ost = needs(street, ost, func=fill_street)
    # print("ost6: " + ost)
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
    district = capitalizer(district)
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
