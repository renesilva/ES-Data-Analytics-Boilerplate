import re


# No funciona con tildes
# https://www.pythontutorial.net/python-string-methods/python-titlecase/
def titlecase(s):
    return re.sub(
        r"[A-Za-z]+('[A-Za-z]+)?",
        lambda word: word.group(0).capitalize(),
        s)
