import re
from fuzzywuzzy import fuzz
from preparsing_functions import generate_ngrams


def addr_part_extractor(s, names, order_list=(3, 2, 1), types=tuple(), special_names=tuple()):
    ret_grams = set()
    first_time = True
    for n in order_list:
        grams_list = generate_ngrams(s, n)
        for gram in grams_list:
            name = ""
            nam = False
            typ = False
            punct = False
            if n == 1:
                typ = True
            if n < 3:
                punct = True
            for word in gram.split():
                if word in special_names and n == 1:
                    return " ".join(ret_grams), s
                if word in names:
                    nam = True
                    name = word
                if word in types:
                    typ = True
                if word == ".":
                    punct = True
            if nam & typ & punct & (first_time or name in ret_grams):
                s = re.sub(gram, "", s, flags=re.IGNORECASE, count=1)
                ret_grams.update(gram.split())
                first_time = False
    # print("dyenhb aeyr")
    # print(type(s))
    return " ".join(ret_grams), s


def settlement_extractor(*checks, s, names, order_list=(2, 3, 1), types=tuple(), special_names=tuple()):
    for check in checks:
        if check != "":
            return "", s
    return addr_part_extractor(s, names, order_list, types, special_names)


def levenshtein_towns(s, x_town, x_settlement, towns):
    if not (x_town == "" and x_settlement == ""):
        return s, x_town
    end_list = ("ий", "ый", "ая", "яя", "ое", "ее", "ой", "ва", "на", "са", "ма")
    res = list()
    key = True
    res_town = ""
    for word in s.lower().split():
        if key and (word[-2:] not in end_list or word[-2:] == "ва" and fuzz.ratio(word, "москва") >= 90):
            for town in towns:
                if fuzz.ratio(word, town.lower()) >= 90:
                    print(s)
                    print(word + " ---> " + town)
                    key = False
                    res_town = town
            if key:
                res.append(word)
        else:
            res.append(word)
    return " ".join(res), res_town


def adder(s1, s2):
    if s1 and s2:
        return s1 + "|" + s2
    elif s2:
        return s2
    return s1
