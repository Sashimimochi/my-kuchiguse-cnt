# -*- coding: utf-8 -*-

import re
import unicodedata
import collections
import pandas as pd

from sudachipy import tokenizer, dictionary


tokenizer_obj = dictionary.Dictionary(dict_type='full').create()
mode = tokenizer.Tokenizer.SplitMode.C


def clean_text(text):
    # 不要な改行などを除去
    text = re.sub(r'[\n \u3000]', '', text)
    # 不要な文字を除去
    stop_chars = "\n,.、。()（）「」　『 』[]【】“”!！ ?？—:・■●★▲▼"
    for stop_char in stop_chars:
        text = text.replace(stop_char, " ")
    # ユニコード正規化
    text = unicodedata.normalize("NFKC", text)
    # アルファベットを小文字に統一
    text = text.lower()
    return text


def wakati(text, pos=['名詞']):
    res = []
    for token in tokenizer_obj.tokenize(clean_text(text), mode):
        if token.part_of_speech()[0] in pos:
            res.append(token.surface())
    return res


def counter(words: list):
    c = collections.Counter(words)
    return pd.DataFrame({'Word': c.keys(), 'Count': c.values()}).sort_values(by=['Count'],ascending=[True]).reset_index()

