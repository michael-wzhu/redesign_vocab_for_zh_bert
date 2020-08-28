
import sys
import tensorflow.compat.v1 as tf

import jieba
from tqdm import tqdm

sys.path.append("./")
from comp_bert.tokenization import BasicTokenizer


def char2char_spaced_single_sent(sent,
                                 basic_tokenizer=None):
    sent = basic_tokenizer.tokenize(sent)

    sent_new = " ".join(sent)

    return sent_new


def char2char_spaced_file(from_file, to_file, basic_tokenizer=None):
    with tf.gfile.GFile(from_file, 'r') as in_f:
        with tf.gfile.GFile(to_file, 'r') as out_f:
            for line in tqdm(in_f):
                line = line.strip()

                if not line:
                    out_f.write("\n")

                else:
                    sent = char2char_spaced_single_sent(line, basic_tokenizer=basic_tokenizer)
                    out_f.write(sent + "\n")


def char2char_segmented_single_sent(sent,):

    sent = list(jieba.cut(sent))
    sent = [w.strip() for w in sent if len(w.strip()) > 0]

    sent_new = " ".join(sent)

    return sent_new


def char2char_segmented_file(from_file, to_file):
    with tf.gfile.GFile(from_file, 'r') as in_f:
        with tf.gfile.GFile(to_file, 'r') as out_f:
            for line in tqdm(in_f):
                line = line.strip()

                if not line:
                    out_f.write("\n")

                else:
                    sent = char2char_segmented_single_sent(line)
                    out_f.write(sent + "\n")



if __name__ == "__main__":
    basic_tokenizer = BasicTokenizer(do_lower_case=True)

    from_dir = "sbt0/experiments/ehr_diagnose/datasets/corpus.txt"

    to_file_spaced = "sbt0/experiments/ehr_diagnose/datasets/corpus_char_spaced_lower.txt"
    char2char_spaced_file(from_dir, to_file_spaced, basic_tokenizer=None)

    to_file_segmented = "sbt0/experiments/ehr_diagnose/datasets/corpus_char_segmented_lower.txt"
    char2char_segmented_file(from_dir, to_file_segmented)

