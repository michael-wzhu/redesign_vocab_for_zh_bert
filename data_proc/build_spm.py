# -*- coding: UTF-8 -*-
import os

import sentencepiece as spm
import tensorflow.compat.v1 as tf

import sys
sys.path.append("./")


if __name__ == "__main__":
    # STORAGE_BUCKET = "gs://sbt0"
    # input_dir_gs = os.path.join(
    #     STORAGE_BUCKET,
    #     "data/corpus/char_lower/zhwiki-latest-pages-articles_char_lower.txt"
    # )
    # input_dir_local = "./zhwiki-latest-pages-articles_char_lower.txt"
    # tf.gfile.Copy(input_dir_gs, input_dir_local, overwrite=True)
    #
    #
    # for vocab_size in [15000]:
    #
    #     spm.SentencePieceTrainer.train('--input=zhwiki-latest-pages-articles_char_lower.txt --model_prefix=./resources/tokenizer/char-%d-clean --vocab_size=%d --pad_id=0 --unk_id=1 --eos_id=-1 --bos_id=-1 --control_symbols=[CLS],[SEP],[MASK] --user_defined_symbols=(,),”,-,.,–,£,€ --shuffle_input_sentence=true --input_sentence_size=30000000 --character_coverage=0.99995 --model_type=bpe --num_threads=32' % (vocab_size, vocab_size))

    # vocab_sizes = [5000, 10000, 15000, 20000, 25000, 30000]
    vocab_sizes = [21128, 5282, 1321]
    prefixes = [
        # "char_spaced_lower",
        # "char_no_space_lower",
        # "subchar_no_space_lower",
        "subchar_spaced_lower",
        "subchar_segmented_lower",
    ]

    STORAGE_BUCKET = "gs://sbt0"

    for prefix in prefixes:
        input_dir_gs = os.path.join(
            STORAGE_BUCKET,
            "data/corpus/%s/zhwiki-latest-pages-articles_%s.txt" % (prefix, prefix)
        )
        input_dir_local = "./zhwiki-latest-pages-articles_%s.txt" % prefix
        tf.gfile.Copy(input_dir_gs, input_dir_local, overwrite=True)


    for vocab_size in vocab_sizes:
        for prefix in prefixes:
            try:
                spm.SentencePieceTrainer.train(
                    '--input=./zhwiki-latest-pages-articles_%s.txt --model_prefix=./data_proc/tokenizers/sentencepiece/%s-%d-clean --vocab_size=%d --pad_id=0 --unk_id=1 --eos_id=-1 --bos_id=-1 --control_symbols=[CLS],[SEP],[MASK] --user_defined_symbols=(,),”,-,.,–,£,€ --shuffle_input_sentence=true --input_sentence_size=15000000 --model_type=bpe --num_threads=16' % (
                    prefix, prefix, vocab_size, vocab_size)
                )

            except Exception as e:
                print(e)


