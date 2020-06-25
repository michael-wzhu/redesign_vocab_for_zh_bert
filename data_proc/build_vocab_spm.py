# -*- coding: UTF-8 -*-
import os

import sentencepiece as spm
import tensorflow.compat.v1 as tf

import sys
sys.path.append("./")


if __name__ == "__main__":

    # vocab_sizes = [10564]
    # vocab_sizes = [21128]
    vocab_sizes = [31692]
    prefixes = [

        # "char_segmented",
        # "char_spaced",
        "char_no_space",
    ]

    STORAGE_BUCKET = "gs://sbt0"



    for prefix in prefixes:
        for vocab_size in vocab_sizes:
            input_dir_gs = os.path.join(
                STORAGE_BUCKET,
                "data/corpus/%s_lower/zhwiki-latest-pages-articles_%s_lower_simplified.txt" % (prefix, prefix)
            )
            input_dir_local = "./tmp/zhwiki-latest-pages-articles_%s_lower_simplified.txt" % prefix
            tf.gfile.Copy(input_dir_gs, input_dir_local, overwrite=True)

            try:
                spm.SentencePieceTrainer.train(
                    '--input=./tmp/zhwiki-latest-pages-articles_%s_lower_simplified.txt --model_prefix=./data_proc/tokenizers/sentencepiece/%s-%d-clean --vocab_size=%d --pad_id=0 --unk_id=1 --eos_id=-1 --bos_id=-1 --control_symbols=[CLS],[SEP],[MASK] --user_defined_symbols=(,),”,-,.,–,£,€ --shuffle_input_sentence=true --input_sentence_size=5000000 --shuffle_input_sentence=true --model_type=bpe --num_threads=12' % (
                    prefix, prefix, vocab_size, vocab_size)
                )

            except Exception as e:
                print(e)


