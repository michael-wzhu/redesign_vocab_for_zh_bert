import json
import random
import re

import tqdm

from src.tokenization_bert import BertTokenizer


def read_dict_char2comps(dict_dir):
    dict_char2comps = {}

    with open(dict_dir, "r", encoding="utf-8") as f:
        for line in tqdm.tqdm(f):
            line = line.strip()
            if len(line) < 2:
                continue

            # if re.search(r"[a-zA-Z]", line):
            #     continue

            char = line.split(":")[0]

            comps = line.split(":")[1].split(" ")
            assert isinstance(comps, list)
            comps = [w.strip() for w in comps if len(w.strip()) > 0]

            # comps_clean = []
            # for comp in comps:
            #     if re.search("[a-zA-Z]", comp):
            #         assert "&CDP-" in comp
            #         assert ";" in comp
            #
            #         comp = comp.replace("&", "").replace("-", "").replace(";", "")
            #
            #     comps_clean.append(comp)

            dict_char2comps[char] = comps

        return dict_char2comps


def contain_chinese_char(text, tokenizer):
    is_chinese_char = False
    for char in text:
        if tokenizer.basic_tokenizer._is_chinese_char(ord(char)):
            is_chinese_char = True
            break

    return is_chinese_char


def check_bert_vocab(bert_vocab_file, dict_char2comps, bpe_tokenizer=None):

    with open(bert_vocab_file, "r", encoding="utf-8") as f:
        for line in tqdm.tqdm(f):
            line = line.strip()
            if not line:
                continue

            if not contain_chinese_char(line, bpe_tokenizer):
                continue

            if line.startswith("##"):
                line = line[2:]

            if line not in dict_char2comps:
                print(line)

            assert line in dict_char2comps


def remap_comps(dict_char2comps):

    # special comps like &CDP-8CBB;

    comp_set = set()
    char_set = set()

    for char, comps in dict_char2comps.items():
        char_set.add(char)
        for comp in comps:
            comp_set.add(comp)

    print("len of comp_set: ", len(comp_set))
    print("len of char_set: ", len(char_set))
    print("len of their intersection: ", len(char_set.intersection(comp_set)))

    independent_chars = char_set.difference(comp_set)
    independent_chars = list(independent_chars)

    random.shuffle(independent_chars)

    dict_comp2comp_new = {}

    for comp_orig, comp_new in zip(list(comp_set) + ["[token-sep]"], independent_chars):
        if "&" in comp_orig or "[" in comp_orig:
            dict_comp2comp_new[comp_orig] = comp_new
        else:
            dict_comp2comp_new[comp_orig] = comp_orig

    return dict_comp2comp_new


def get_char2comps_remapped(dict_char2comps, dict_comp2comp_remap):
    dict_char2comps_remap = {}

    for char, comps in dict_char2comps.items():
        comps_new = []
        for comp_ in comps:
            comp_new_ = dict_comp2comp_remap[comp_]
            comps_new.append(comp_new_)

        dict_char2comps_remap[char] = comps_new

    dict_char2comps_remap_joined = {}
    for char_, comps_ in dict_char2comps_remap.items():
        comps_joined_ = "".join(comps_)
        dict_char2comps_remap_joined[char_] = comps_joined_

    return dict_char2comps_remap, dict_char2comps_remap_joined



if __name__ == "__main__":
    #################
    # 使用 RAN 的映射表，并保留田字格
    #################
    # dict_dir_ = "data_proc/proc_comps/vocab/IDS_dictionary.txt"
    # ids_dict_char2comps = read_dict_char2comps(dict_dir_)
    #
    # # check whether chars in chinese bert vocab are in ids_dict_char2comps
    # bpe_tokenizer = BertTokenizer.from_pretrained("bert-base-chinese")
    #
    # bert_vocab_file = "data_proc/proc_comps/vocab/bert-chinese-vocab.txt"
    # check_bert_vocab(bert_vocab_file, ids_dict_char2comps, bpe_tokenizer=bpe_tokenizer)
    #
    # dict_comp2comp_remapped = remap_comps(ids_dict_char2comps)
    # with open("data_proc/proc_comps/vocab/dict_comp2comp_remapped.json", "w", encoding="utf-8") as f:
    #     json.dump(
    #         dict_comp2comp_remapped,
    #         f,
    #         ensure_ascii=False
    #     )

    dict_comp2comp_remapped = json.load(
        open("data_proc/proc_comps/vocab/dict_comp2comp_remapped.json", "r", encoding="utf-8")
    )
    dict_comp2comp_remapped_reversed = {v: k for k, v in dict_comp2comp_remapped.items()}
    with open("data_proc/proc_comps/vocab/dict_comp2comp_remapped_reversed.json", "w", encoding="utf-8") as f:
        json.dump(
            dict_comp2comp_remapped_reversed,
            f,
            ensure_ascii=False
        )

    # dict_char2comps_remap, dict_char2comps_remap_joined = \
    #     get_char2comps_remapped(ids_dict_char2comps, dict_comp2comp_remapped)
    # with open("data_proc/proc_comps/vocab/dict_char2comps_remapped.json", "w", encoding="utf-8") as f:
    #     json.dump(
    #         dict_char2comps_remap,
    #         f,
    #         ensure_ascii=False
    #     )
    # with open("data_proc/proc_comps/vocab/dict_char2comps_remapped_joined.json", "w", encoding="utf-8") as f:
    #     json.dump(
    #         dict_char2comps_remap_joined,
    #         f,
    #         ensure_ascii=False
    #     )
