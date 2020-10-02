from general import value
from yargy import Parser
from common_variables import *
from addr_name import ADDR_NAME

OnlyNameStreet = fact(
    'OnlyNameStreet',
    ['name']
)


class OnlyNameStreet(OnlyNameStreet):
    type = 'улица'
    value = value('name')

########
#
#    STREET IMP W/O STREET_WORDS
#
#########


ONLY_NAME_STREET = ADDR_NAME.interpretation(
    OnlyNameStreet.name
).interpretation(
    OnlyNameStreet
)


def yargy_only_street(row, parser=Parser(ONLY_NAME_STREET)):
    street = ""
    for match in parser.findall(row):
        row = row[0: match.span.start] + row[match.span.stop:]
        street = "улица " + match.fact.value
        try:
            value, span, typ, forms = [x for x in match.tokens[0]]
            name, grams = forms[0]
            gen = grams.gender
            male, female, neutral, bi, general = [x for x in gen]
            if male:
                street = "проспект " + match.fact.value
            elif neutral:
                street = "шоссе " + match.fact.value
        except:
            pass
        break
    return street, row