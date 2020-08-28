
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
        with tf.gfile.GFile(to_file, 'w') as out_f:
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
        with tf.gfile.GFile(to_file, 'w') as out_f:
            for line in tqdm(in_f):
                line = line.strip()

                if not line:
                    out_f.write("\n")

                else:
                    sent = char2char_segmented_single_sent(line)
                    out_f.write(sent + "\n")



if __name__ == "__main__":
    basic_tokenizer = BasicTokenizer(do_lower_case=True)

    from_dir = "gs://sbt0/experiments/ehr_diagnose/datasets/corpus.txt"
    from_dir_local = "./corpus.txt"

    to_file_spaced = "gs://sbt0/experiments/ehr_diagnose/datasets/corpus_char_spaced_lower.txt"
    to_file_spaced_local = "./corpus_char_spaced_lower.txt"

    tf.gfile.Copy(from_dir, from_dir_local, overwrite=True)

    char2char_spaced_file(from_dir_local, to_file_spaced_local, basic_tokenizer=basic_tokenizer)
    tf.gfile.Copy(to_file_spaced_local, to_file_spaced, overwrite=True)

    to_file_segmented = "gs://sbt0/experiments/ehr_diagnose/datasets/corpus_char_segmented_lower.txt"
    to_file_segmented_local = "./corpus_char_segmented_lower.txt"

    char2char_segmented_file(from_dir_local, to_file_segmented_local)
    tf.gfile.Copy(to_file_segmented_local, to_file_segmented, overwrite=True)

