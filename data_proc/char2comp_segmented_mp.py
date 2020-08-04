# -*- coding: utf-8 -*-
import json
# import sys
# from pathlib import Path
#
# import tqdm
# from blingfire import text_to_sentences
import re

import sys

import jieba
import tqdm

import tensorflow.compat.v1 as tf

sys.path.append("./")
from src.tokenization_bert import BertTokenizer


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


def split_sent(text_, spliter="。？?"):
    list_sents = []
    tmp_sent = ""
    for char_ in text_:
        if char_ in spliter:
            if len(tmp_sent) == 0:
                continue
            else:
                tmp_sent += char_
                list_sents.append(tmp_sent)
                tmp_sent = ""

        else:
            tmp_sent += char_

    if len(tmp_sent) > 0:
        list_sents.append(tmp_sent)

    return list_sents


def contain_chinese_char(text, tokenizer):
    is_chinese_char = False
    for char in text:
        if tokenizer.basic_tokenizer._is_chinese_char(ord(char)):
            is_chinese_char = True
            break

    return is_chinese_char


def char2comp_single_sent(sent, dict_char2comp, sep_token="", tokenizer=None):

    sent = list(jieba.cut(sent))
    sent = [w.strip() for w in sent if len(w.strip()) > 0]

    sent_new = []
    for seg in sent:

        if re.search("[\u4e00-\u9fa5]", seg):

            seg_new = ""
            for char in seg:
                if contain_chinese_char(char, tokenizer):
                    tmp_ = char2comp_single_char(char, dict_char2comp)
                    if tmp_:
                        seg_new += tmp_ + sep_token
                    else:
                        seg_new += char + sep_token
                else:
                    seg_new += char

            sent_new.append(seg_new)

        else:
            sent_new.append(seg)

    sent_new = " ".join(sent_new)
    # drop redundent blank
    sent_new = drop_extra_blank(sent_new)

    return sent_new


def char2comp_file(txt_file,
                   to_file,
                   dict_char2comp=None,
                   do_lower_case=1,
                   tokenizer=None):
    # with open(to_file, "w", encoding="utf-8") as out_f:
    with tf.gfile.GFile(to_file, "w") as out_f:
        # with open(txt_file, "r", encoding="utf-8") as in_f:
        with tf.gfile.GFile(txt_file, "r") as in_f:
            for i, line in tqdm.tqdm(enumerate(in_f)):
                line = line.strip()
                if len(line) == 0:
                    out_f.write("\n")
                    continue

                sents_ = split_sent(line, spliter="。？?")
                for sent in sents_:
                    sent_new_ = char2comp_single_sent(
                        sent,
                        dict_char2comp,
                        tokenizer=tokenizer
                    )
                    if do_lower_case:
                        sent_new_ = sent_new_.lower()

                    if i < 10:
                        print(sent_new_)

                    out_f.write(sent_new_ + "\n")


def main():
    file_in = str(sys.argv[1])
    file_out = str(sys.argv[2])
    dict_char2comp_dir = str(sys.argv[3])
    do_lower_case = int(sys.argv[4])

    tokenizer = BertTokenizer.from_pretrained("bert-base-chinese")

    print('Pre-processing {} to {}...'.format(file_in, file_out))
    dict_char2comp = json.load(
        # open(dict_char2comp_dir, "r", encoding="utf-8")
        open(dict_char2comp_dir, "r", encoding="utf-8")
    )
    char2comp_file(
        file_in,
        file_out,
        dict_char2comp=dict_char2comp,
        do_lower_case=do_lower_case,
        tokenizer=tokenizer
    )

    print('Successfully pre-processed {} to {}...'.format(file_in, file_out))


if __name__ == '__main__':
    main()
    # #
    # tokenizer = BertTokenizer.from_pretrained("bert-base-chinese")
    #
    # dict_char2comps_dir = "data_proc/proc_comps/vocab/dict_char2comps_remapped_joined.json"
    # dict_char2comps = json.load(
    #     open(dict_char2comps_dir, "r", encoding="utf-8")
    # )
    # print(char2comp_single_sent("新冠病毒已在全世界蔓延！", dict_char2comps, tokenizer=tokenizer))