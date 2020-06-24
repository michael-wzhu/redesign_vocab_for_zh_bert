# -*- coding: UTF-8 -*-
import os

import sentencepiece as spm
import tensorflow.compat.v1 as tf

from tokenizers import (ByteLevelBPETokenizer,
                            CharBPETokenizer,
                            SentencePieceBPETokenizer,
                            BertWordPieceTokenizer)


import sys
sys.path.append("./")


if __name__ == "__name__":

    vocab_sizes = [21128, 10564, 5282]
    prefixes = [
        "char_no_space",
        "char_spaced",
        "char_segmented",
    ]

    STORAGE_BUCKET = "gs://sbt0"

    for prefix in prefixes:
        input_dir_gs = os.path.join(
            STORAGE_BUCKET,
            "data/corpus/%s_lower/zhwiki-latest-pages-articles_%s_lower.txt" % (prefix, prefix)
        )
        input_dir_local = "./zhwiki-latest-pages-articles_%s_lower.txt" % prefix
        tf.gfile.Copy(input_dir_gs, input_dir_local, overwrite=True)

    for vocab_size in vocab_sizes:
        for prefix in prefixes:
            try:
                tokenizer_name = prefix + "_" + str(vocab_sizes)
                tokenizer = BertWordPieceTokenizer(
                    handle_chinese_chars=False
                )

                tokenizer.train(
                    [
                        "./zhwiki-latest-pages-articles_%s_lower.txt" % prefix
                    ],
                    vocab_size=vocab_size,

                )
                tokenizer.save("data_proc/tokenizers", tokenizer_name)

            except Exception as e:
                print(e)