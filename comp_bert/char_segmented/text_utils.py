import json
import re

import jieba_fast as jieba
import sys

import six
import tqdm


# [CLS] 我我我 [SEP] 我我 [SEP]
from comp_bert import tokenization


def char2comp_single_char(zh_char, dict_char2comp):
    if zh_char in dict_char2comp:
        zh_char_comp = dict_char2comp[zh_char].strip()
        return zh_char_comp
    else:
        return None


def drop_extra_blank(sent):

    sent_new = ""
    sent = sent.strip()
    prev_is_blank = False

    for i, char_ in enumerate(sent):
        if char_ == " " and prev_is_blank:
            continue
        elif char_ == " " and not prev_is_blank:
            sent_new += char_
            prev_is_blank = True
            continue
        else:
            sent_new += char_
            prev_is_blank = False
            continue

    return sent_new


def contain_chinese_char(text, tokenizer):
    is_chinese_char = False
    for char in text:
        if tokenizer.basic_tokenizer._is_chinese_char(ord(char)):
            is_chinese_char = True
            break

    return is_chinese_char


def tokenize_single_sent(sent, tokenizer=None):
    sent = sent.strip()
    # print(sent)
    line_seg = tokenizer.tokenize(sent)
    # print(line_seg)

    return line_seg


def char2char_single_sent(sent,
                          dict_char2comp=None,
                          sep_token="",
                          tokenizer=None):

    sent = list(jieba.cut(sent))
    sent = [w.strip() for w in sent if len(w.strip()) > 0]

    sent_new = " ".join(sent)
    # drop redundent blank
    sent_new = drop_extra_blank(sent_new)

    line_seg = tokenize_single_sent(sent_new, tokenizer=tokenizer)

    return line_seg


def printable_text(text):
    """Returns text encoded in a way suitable for print or `tf.logging`."""

    # These functions want `str` for both Python2 and Python3, but in one case
    # it's a Unicode string and in the other it's a byte string.
    if six.PY3:
        if isinstance(text, str):
            return text
        elif isinstance(text, bytes):
            return six.ensure_text(text, "utf-8", "ignore")
        else:
            raise ValueError("Unsupported string type: %s" % (type(text)))
    elif six.PY2:
        if isinstance(text, str):
            return text
        elif isinstance(text, six.text_type):
            return six.ensure_binary(text, "utf-8")
        else:
            raise ValueError("Unsupported string type: %s" % (type(text)))
    else:
        raise ValueError("Not running on Python2 or Python 3?")


if __name__ == "__main__":
    text_ = "⿰⿱立朩斤⿱冖⿺⿱一兀寸 ⿸疒⿱一内⿱龶母 已 ⿸㡏土 ⿱人王世⿱田⿱人⿰丿丨 ⿱艹⿳日罒又⿺廴⿱丿䖻 ！"

    bpe_tokenizer = tokenization.FullTokenizer(
        vocab_file="data_proc/tokenizers/sentencepiece/subchar_segmented_lower-21128-clean.vocab",
        do_lower_case=True,
        spm_model_file="data_proc/tokenizers/sentencepiece/subchar_segmented_lower-21128-clean.model")
    text_seg = tokenize_single_sent(text_, tokenizer=bpe_tokenizer)
    print(text_seg)
