import re


def change_punctuation(s):
    return s.replace(".", " . ").replace(",", " , ").replace(")", "").replace("(", "")


def drop_spaces(s):
    return re.sub(' +', ' ', s)


def simple_changer(s, dictionary):
    for key, value in dictionary.items():
        s = re.sub(key, value, s, flags=re.IGNORECASE)
    return s


def complex_changer(s, change_dict):
    for i in range(3, 0, -1):
        grams_list = generate_ngrams(s, i)
        for gram in grams_list:
            # print(gram)
            if change_dict.get(gram):
                return re.sub(gram, change_dict.get(gram), s, flags=re.IGNORECASE)
    return s


def generate_ngrams(s, n):
    s = s.lower()
    s = re.sub(r'^[a-zA-Z0-9,.\s]', ' ', s)
    tokens = [token for token in s.split(" ") if token != ""]
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]


def locality_dict(locs):
    l_dict = {}
    for loc in locs:
        if len(re.split(r'[\s]\s*', loc)) > 1:
            name = re.sub(r'\([^()]*\)', "", loc, flags=re.IGNORECASE)
            name = re.split(r'[\s]\s*', name)
            if "" in name:
                name.remove("")
            if " " in name:
                name.remove(" ")
            l_dict.update({loc: "_".join(name)})
    return l_dict


def extract_complex_names(locations):
    result = list()
    extracted = list()
    for loc in locations:
        if len(loc.split()) > 1:
            extracted.append(loc)
        else:
            result.append(loc)
    return result, extracted


def extract_adjf_names(locations):
    result = list()
    extracted = list()
    end_list = ("ий", "ый", "ая", "яя", "ое", "ее", "ой", "ва")
    for loc in locations:
        if loc[-2:] in end_list:
            extracted.append(loc)
        else:
            result.append(loc)
    return result, extracted
