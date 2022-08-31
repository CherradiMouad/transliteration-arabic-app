import sys, os, glob, json, codecs, platform
import ArabicTransliterator
from ArabicTransliterator import ALA_LC_Transliterator
import mishkal.tashkeel.tashkeel as tashkeel
import pandas as pd
from IPython.display import display, HTML




transliterator = ALA_LC_Transliterator()


def transliterate(text, vocalize=True):
    voc = text
    if vocalize:
        vocalizer=tashkeel.TashkeelClass()
        voc = vocalizer.tashkeel(text)
    return transliterator.do(voc.strip())

x=input("Enter:")

out=transliterate(x,vocalize=True)
print(out)