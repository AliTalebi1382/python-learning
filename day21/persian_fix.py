import arabic_reshaper
from bidi.algorithm import get_display

def fix_persian(text):
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)