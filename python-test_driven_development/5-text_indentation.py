#!/usr/bin/python3
"""
Bu modul 'text_indentation' funksiyasını təqdim edir.
"""


def text_indentation(text):
    """
    Mətni  sətir əlavə edərək çap edir.
    Hər sətrin əvvəlində və sonunda boşluqlar silinir.

    Arqumentlər:
        text (str): Emal ediləcək mətn.

    Xətalar:
        TypeError: text string deyilsə.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    # 1. İşarələri tapıb yanına 2 dənə newline (\n) əlavə edirik
    # pycodestyle (E501) xətası almamaq üçün alt-alta yazırıq:
    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')

    # 2. Mətni sətirlərə (lines) bölürük
    lines = text.split('\n')

    # 3. Hər bir sətri təmizləyib (strip) çap edirik
    for i in range(len(lines)):
        # Əgər sonuncu sətirdirsə, sonuna '\n' əlavə etmirik (şərtə görə)
        if i == len(lines) - 1:
            print(lines[i].strip(), end="")
        else:
            print(lines[i].strip() + "\n", end="")
