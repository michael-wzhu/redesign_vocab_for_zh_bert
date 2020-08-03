import json
import re

import jieba_fast as jieba
import sys

import six
import tqdm


# [CLS] 我我我 [SEP] 我我 [SEP]


def zh_char2comp(zh_char, dict_char2comp):
    if zh_char in dict_char2comp:
        zh_char_comp = dict_char2comp[zh_char]
        return zh_char_comp
    else:
        return [zh_char]


def contain_chinese_char(text, tokenizer):
    is_chinese_char = False
    for char in text:
        if tokenizer.basic_tokenizer._is_chinese_char(ord(char)):
            is_chinese_char = True
            break

    return is_chinese_char


def zh_char2comp_sent(sent,
                      dict_char2comp,
                      max_comp_length=None,
                      tokenizer=None):
    line_seg = tokenizer.tokenize(sent)

    sent_seg_comps = []
    for seg in line_seg:
        if contain_chinese_char(seg, tokenizer):
            assert len(seg) == 1

            seg_comp = zh_char2comp(seg, dict_char2comp)
            assert isinstance(seg_comp, list)
            assert len(seg_comp) > 0

        else:
            if ("[" in seg and "]" in seg) or ("<" in seg and ">" in seg):
                seg_comp = zh_char2comp(seg, dict_char2comp)
            else:
                seg_comp = list(seg)

        sent_seg_comps.append(seg_comp[: max_comp_length])

    return line_seg, sent_seg_comps


def zh_char2comp_sent_seg(sent_seg,
                      dict_char2comp,
                      max_comp_length=None,
                      tokenizer=None):

    sent_seg_comps = []
    for seg in sent_seg:
        # print("seg: ", seg)
        if contain_chinese_char(seg, tokenizer):
            assert len(seg) == 1

            seg_comp = zh_char2comp(seg, dict_char2comp)
            assert isinstance(seg_comp, list)
            assert len(seg_comp) > 0

        else:
            if ("[" in seg and "]" in seg) or ("<" in seg and ">" in seg):
                seg_comp = zh_char2comp(seg, dict_char2comp)
            else:
                seg_comp = list(seg)

        sent_seg_comps.append(seg_comp[: max_comp_length])

    return sent_seg_comps


def get_comp_ids_word(comps, dict_comp2id):
    comp_ids = []
    for comp in comps:
        comp_ids.append(dict_comp2id.get(comp, dict_comp2id["[UNK]"]))

    return comp_ids


def get_comp_ids_sent(list_comps, dict_comp2id):
    list_comp_ids = []
    for comps in list_comps:
        comp_ids = get_comp_ids_word(
            comps, dict_comp2id
        )
        list_comp_ids.append(comp_ids)

    return list_comp_ids


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
    pass


