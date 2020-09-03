# -*- coding: utf-8 -*-
"""
@File: file_utils.py
@Copyright: 2019 Michael Zhu
@License：the Apache License, Version 2.0
@Author：Michael Zhu
@version：
@Date：
@Desc: 
"""
import os
import sys

import tqdm

import tensorflow.compat.v1 as tf

sys.path.append("./")


def txt_files2file(list_files, to_dir):
    # with open(to_dir, "w", encoding="utf-8") as out_f:
    with tf.gfile.GFile(to_dir, "w") as out_f:
        for file_ in tqdm.tqdm(list_files):
            # with open(file_, "r", encoding="utf-8") as in_f:
            with tf.gfile.GFile(file_, "r") as in_f:
                for line in tqdm.tqdm(in_f):
                    out_f.write(line)


if __name__ == "__main__":

    STORAGE_BUCKET = "gs://sbt0"

    # list_files_ = []
    # num_files = 218
    # for i in range(num_files):
    #     file_ = os.path.join(
    #         STORAGE_BUCKET,
    #         "data/corpus/char_no_space_lower/zhwiki-latest-pages-articles_%d_char_no_space_lower_simplified.txt" % (i + 1)
    #     )
    #     list_files_.append(file_)
    #
    # to_dir_ = os.path.join(
    #     STORAGE_BUCKET,
    #     "data/corpus/char_no_space_lower/zhwiki-latest-pages-articles_char_no_space_lower_simplified.txt")
    # txt_files2file(list_files_, to_dir_)
    #
    # list_files_ = []
    # num_files = 218
    # for i in range(num_files):
    #     file_ = os.path.join(
    #         STORAGE_BUCKET,
    #         "data/corpus/char_segmented_lower/zhwiki-latest-pages-articles_%d_char_segmented_lower_simplified.txt" % (
    #                     i + 1)
    #     )
    #     list_files_.append(file_)
    #
    # to_dir_ = os.path.join(
    #     STORAGE_BUCKET,
    #     "data/corpus/char_segmented_lower/zhwiki-latest-pages-articles_char_segmented_lower_simplified.txt")
    # txt_files2file(list_files_, to_dir_)

    # list_files_ = []
    # num_files = 218
    # for i in range(num_files):
    #     file_ = os.path.join(
    #         STORAGE_BUCKET,
    #         "data/corpus/subchar_spaced_lower/zhwiki-latest-pages-articles_%d_subchar_spaced_lower.txt" % (
    #                 i + 1)
    #     )
    #     list_files_.append(file_)
    #
    # to_dir_ = os.path.join(
    #     STORAGE_BUCKET,
    #     "data/corpus/subchar_spaced_lower/zhwiki-latest-pages-articles_subchar_spaced_lower.txt")
    # txt_files2file(list_files_, to_dir_)

    list_files_ = []
    num_files = 626
    for i in range(num_files):
        file_ = os.path.join(
            STORAGE_BUCKET,
            "experiments/ehr_diagnose/datasets/char_segmented_lower/outpatient_%d_char_segmented_lower_simplified.txt" % (
                    i + 1)
        )
        list_files_.append(file_)
        print(i)

    num_files = 218
    for i in range(num_files):
        file_ = os.path.join(
            STORAGE_BUCKET,
            "data/corpus/char_segmented_lower/zhwiki-latest-pages-articles_%d_char_segmented_lower_simplified.txt" % (
                        i + 1)
        )
        list_files_.append(file_)
        print(i)

    to_dir_ = os.path.join(
        STORAGE_BUCKET,
        "experiments/ehr_diagnose/datasets/char_segmented_lower/char_segmented_lower_simplified.txt")
    txt_files2file(list_files_, to_dir_)
