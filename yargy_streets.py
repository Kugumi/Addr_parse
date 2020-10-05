from natasha.grammars.addr import LET, DATE, IMENI, MODIFIER_WORDS
from yargy.interpretation import fact
from yargy import Parser
from yargy import (
    rule,
    or_, and_
)

from yargy.predicates import (
    eq, lte, gte, gram, type, tag,
    length_eq,
    in_, in_caseless, dictionary,
    normalized, caseless,
    is_title
)
from yargy.tokenizer import QUOTES

INT = type('INT')
DOT = eq('.')
ADJF = gram('ADJF')
NOUN = gram('NOUN')
TITLE = is_title()
DASH = eq('-')
SLASH = eq('/')
QUOTE = in_(QUOTES)

ANUM = rule(
    INT,
    DASH.optional(),
    in_caseless({
        'я', 'й', 'е',
        'ое', 'ая', 'ий', 'ой'
    })
)

def value(key):
    @property
    def field(self):
        return getattr(self, key)
    return field

OnlyNameStreet = fact(
    'OnlyNameStreet',
    ['name']
)

class OnlyNameStreet(OnlyNameStreet):
    type = 'улица'
    value = value('name')

##########
#
#   ADDR NAME IMP
#
##########


ROD = gram('gent')

SIMPLE = and_(
    or_(
        ADJF,  # Школьная
        and_(NOUN, ROD),  # Ленина, Победы
    )
)

COMPLEX = or_(
    rule(
        and_(ADJF),
        NOUN
    ),
    rule(
        TITLE,
        DASH.optional(),
        TITLE
    ),
)

EXCEPTION = dictionary({
    'арбат',
    'варварка',
    'мельникайте',
    'каховка',
    'зорге'
})

MAYBE_NAME = or_(
    rule(SIMPLE),
    COMPLEX,
    rule(EXCEPTION)
)

NAME = or_(
    MAYBE_NAME,
    LET,
    DATE,
    IMENI
)

NAME = rule(
    MODIFIER_WORDS.optional(),
    NAME
)

ADDR_CRF = tag('I').repeatable()

NAME = or_(
    NAME,
    ANUM,
    rule(NAME, ANUM),
    rule(ANUM, NAME),
    rule(INT, DASH.optional(), NAME),
    rule(NAME, DASH, INT),
    ADDR_CRF
)

ADDR_NAME = NAME

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

parser=Parser(ONLY_NAME_STREET)
