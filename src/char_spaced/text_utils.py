import re

import jieba
import six

from data_proc.char2char_spaced_mp import drop_extra_blank


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


def contain_chinese_char(text, tokenizer):
    is_chinese_char = False
    for char in text:
        if tokenizer._is_chinese_char(ord(char)):
            is_chinese_char = True
            break

    return is_chinese_char


def proc_single_sent(sent):
    # 字与字之间有空格
    sent_new_ = ""

    sent = list(jieba.cut(sent))
    sent = " ".join(sent)
    for char_ in sent:

        if re.search("[\u4e00-\u9fa5]", char_):
            sent_new_ += " " + char_ + " "
        else:
            sent_new_ += char_

    # drop redundent blank
    sent_new_ = drop_extra_blank(sent_new_)

    return sent_new_


def tokenize_single_sent(sent, tokenizer=None):
    sent = proc_single_sent(sent)

    line_seg = tokenizer.tokenize(sent)

    return line_seg