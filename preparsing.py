from global_variables import *
from preparsing_functions import *

settlements, complex_settlements = extract_complex_names(settlements)
settlements, settlements_adjf = extract_adjf_names(settlements)

for elem in list(SETTLEMENTS_TO_REMOVE):
    if elem in settlements:
        settlements.remove(elem)

for elem in list(COMPLEX_SETTLEMENTS_TO_REMOVE):
    if elem in complex_settlements:
        complex_settlements.remove(elem)


towns_dict = locality_dict(towns)
complex_settlements_dict = locality_dict(complex_settlements)
complex_settlements_dict.update({"автономный округ": "автономный_округ",
                                 "автономная область": "автономная_область",
                                 "северная осетия": "северная_осетия",
                                 "н . новгород": "нижний_новгород",
                                 "в . новгород": "великий_новгород",
                                 "н новгород": "нижний_новгород",
                                 "в новгород": "великий_новгород"})
complex_list = list(complex_settlements_dict.values())
settlements = tuple(settlements)
complex_list = tuple(complex_list)
settlements_list = settlements + complex_list

towns_list = list(towns_dict.values())
