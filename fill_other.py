def last_parsing(aim, s, func):
    if aim != "" or s == "":
        return aim, s
    else:
        return func(s)


def fill_street(row):
    s = list()
    street = ""
    for r in row.split():
        if (len(r) > 2) and r[0].isalpha() and r[1].isalpha() and not street and not r.lower() in KEY_WORDS:
            street = r
        else:
            s.append(r)
    if street != "":
        street = "улица " + street
    return street, " ".join(s)


def fill_building_number(row):
    s = list()
    num = ""
    for r in row.split():
        if r[0].isnumeric() and not num and (len(r) <= 3):
            num = r
        else:
            s.append(r)
    return num, " ".join(s)


def building_parsing(building, s):
    if s == "" or "дом" in building.split():
        return building, s
    else:
        num, s = fill_building_number(s)
        if num != "":
            building = "дом " + num + " " + building
        return building, s


ABBR = ("рф", "ао", "осб", "госб", "всп", "до", "удо", "сдо", "дф", "бц")
setex = set()


def capitalizer(s, setex=setex):
    res = list()
    for word in s.lower().split():
        if word in ABBR:
            res.append(word.upper())
        elif word not in KEY_WORDS:
            if "-" in word :
                nword = word.split("-")
                nword = map(str.capitalize, nword)
                res.append("-".join(nword))
            elif "_" in word:
                nword = word.split("_")
                nword = map(str.capitalize, nword)
                res.append(" ".join(nword))
            else:
                res.append(word.capitalize())
        else:
            if not KEY_WORDS_DICT.get(word):
                setex.update(word.split())
                res.append(word)
            else:
                res.append(KEY_WORDS_DICT.get(word))
    return " ".join(res)


def drop_punct(s):
    return s.replace(".", "").replace(",", "")


def settlements(s):
    res = list()
    settlements_dict = {"с": "село", "п": "поселок"}
    for word in s.split():
        if settlements_dict.get(word):
            res.append(settlements_dict.get(word))
        else:
            res.append(word)
    return(" ".join(res))


def town_words_order(s):
    key_word = ""
    res = list()
    for word in s.split():
        if word in KEY_WORDS:
            key_word = word
        else:
            res.append(word)
    if not res:
        return ""
    # if not key_word:
    return "город" + " " + " ".join(res)
    # else:
    #     return key_word + " " + " ".join(res)


def settlement_words_order(s):
    key_word = ""
    res = list()
    for word in s.split():
        if word in KEY_WORDS:
            key_word = word
        else:
            res.append(word)
    if not res:
        return ""
    if not key_word:
        return " ".join(res)
    else:
        return key_word + " " + " ".join(res)


def alnum_stay(s):
    res = list()
    for word in s.split():
        if word.isalnum() and word != " " and word != "":
            res.append(word)
    return " ".join(res)


def kabinet(place, s):
    if s.isnumeric() and not ("комната" in place.split() or "кабинет" in place.split()):
        if place == "":
            return "кабинет " + s, ""
        return place + " кабинет " + s, ""
    return place, s
