# -*- coding: utf-8 -*-
import json
import os
import re
import sys

import tqdm

import tensorflow.compat.v1 as tf

sys.path.append("./")

from generic_utils.io_utils import load_from_json, dump_to_json
from generic_utils.tokenization_bert import BasicTokenizer
from hierachical_bert.text_utils import zh_char2comp




def contain_chinese_char(text, tokenizer):
    is_chinese_char = False
    for char in text:
        if tokenizer._is_chinese_char(ord(char)):
            is_chinese_char = True
            break

    return is_chinese_char


def collect_vocab(corpus_dir, 
                vocab_dir, 
                comp_freq_stat_dir,
                dict_char2comp=None, 
                basic_tokenizer=None):
    dict_vocab2freq = {}
    dict_comp_length2freq = {}

    with tf.gfile.GFile(corpus_dir, "r") as in_f:
        for i, line in tqdm.tqdm(enumerate(in_f)):

            if i % 10000 == 0:
                print(json.dumps(dict_vocab2freq, ensure_ascii=False))
                print("len of dict_vocab2freq: ", len(dict_vocab2freq))

            line = line.strip()
            if not line:
                continue

            if "[" in line and "]" in line:
                line_seg = [line]
            elif "<" in line and ">" in line:
                line_seg = [line]
            else:
                line_seg = basic_tokenizer.tokenize(line)

            for seg in line_seg:
                if contain_chinese_char(seg, basic_tokenizer):
                    assert len(seg) == 1

                    seg_comp = zh_char2comp(seg, dict_char2comp)
                    assert isinstance(seg_comp, list)
                    assert len(seg_comp) > 0

                else:
                    if "[" in seg and "]" in seg:
                        if "unused" in seg:
                            continue
                        # if seg == "[CLS]":
                        #     continue
                        # if seg == "[SEP]":
                        #     continue

                        seg_comp = [seg]

                    elif "<" in seg and ">" in seg:
                        if seg == "<S>":
                            continue
                        if seg == "<T>":
                            continue

                        seg_comp = [seg]
                    else:
                        seg_comp = list(seg)

                for c in seg_comp:
                    if c not in dict_vocab2freq:
                        dict_vocab2freq[c] = 0

                    dict_vocab2freq[c] += 1

                comp_length_ = len(seg_comp)
                if comp_length_ not in dict_comp_length2freq:
                    dict_comp_length2freq[comp_length_] = 0
                dict_comp_length2freq[comp_length_] += 1

    dump_to_json(
        dict_vocab2freq,
        vocab_dir
    )

    # list_vocab2freq = list(dict_vocab2freq.items())
    # list_vocab2freq = sorted(
    #     list_vocab2freq,
    #     key=lambda x: x[1],
    #     reverse=True
    # )
    #
    # list_vocab = [w[0] for w in list_vocab2freq]
    #
    # with open(vocab_dir, "w", encoding="utf-8") as f:
    #     for i, w in enumerate(list_vocab):
    #         f.write(w + " " + str(i) + "\n")

    list_comp_length2freq = list(dict_comp_length2freq.items())
    list_comp_length2freq = sorted(
        list_comp_length2freq,
        key=lambda x: x[1],
        reverse=True
    )

    dump_to_json(
        list_comp_length2freq,
        comp_freq_stat_dir
    )


if __name__ == "__main__":
    STORAGE_BUCKET = "gs://sbt0"
    corpus_dir = "./hierachical_bert/data_proc/vocabs/bert-chinese-vocab.txt"
    vocab_dir = "./hierachical_bert/data_proc/vocabs/dict_comp2freq.json"
    comp_freq_stat_dir = "./hierachical_bert/data_proc/vocabs/list_comp_length2freq.json"
    
    basic_tokenizer = BasicTokenizer(
        do_lower_case=True,
        never_split=None,
        tokenize_chinese_chars=True
    )
    
    dict_char2comp = load_from_json("hierachical_bert/data_proc/vocabs/ids_dict_char2comps.json")
    collect_vocab(
        corpus_dir, 
        vocab_dir, 
        comp_freq_stat_dir,
        dict_char2comp=dict_char2comp, 
        basic_tokenizer=basic_tokenizer
    )

    dict_comp2freq = load_from_json(
        "hierachical_bert/data_proc/vocabs/dict_comp2freq.json"
    )
    list_comp2freq = sorted(
        list(dict_comp2freq.items()),
        key=lambda x: (x[1], len(x[0])),
        reverse=False
    )

    dict_comp2id = {seme: idx for idx, (seme, _) in enumerate(list_comp2freq)}
    # dict_comp2id["<pad>"] = 0
    json.dump(
        dict_comp2id,
        open("hierachical_bert/data_proc/vocabs/dict_comp2id.json", "w", encoding="utf-8"),
        ensure_ascii=False
    )


