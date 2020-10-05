import re


def delete_slash(s):
    if s[0:1] == "|":
        return s[1:]
    if s[-1:] == "|":
        return s[0:-1]
    return s


def is_punct(s):
    s = re.sub(',+', '', s)
    s = re.sub('\.+', '', s)
    if s == "":
        return True
    else:
        return False


def remove_duplicate_punctuation(s):
    res = list()
    for word in s.split():
        if res:
            if res[-1] != ',' and res[-1] != '.' or not is_punct(word):
                word = re.sub(',+', ',', word)
                word = re.sub('\.+', '.', word)
                res.append(word)
        elif not is_punct(word):
            res.append(word)
    return " ".join(res)
