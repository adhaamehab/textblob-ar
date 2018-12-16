import re


'''
Code snippet from https://github.com/bakrianoo/aravec

'''


def clean_str(text):
    search = ["أ", "إ", "آ", "ة", "_", "-", "/", ".", "،", " و ", " يا ",
              '"', "ـ", "'", "ى", "\\", '\n', '\t', '&quot;', '?', '؟', '!']
    replace = ["ا", "ا", "ا", "ه", " ", " ", "", "", "", " و",
               " يا", "", "", "", "ي", "", ' ', ' ', ' ', ' ? ', ' ؟ ', ' ! ']

    p_tashkeel = re.compile(r'[\u0617-\u061A\u064B-\u0652]')
    text = re.sub(p_tashkeel, "", text)
    p_longation = re.compile(r'(.)\1+')
    subst = r"\1\1"
    text = re.sub(p_longation, subst, text)
    text = text.replace('وو', 'و')
    text = text.replace('يي', 'ي')
    text = text.replace('اا', 'ا')

    for i in range(0, len(search)):
        text = text.replace(search[i], replace[i])
    text = text.strip()

    return text
