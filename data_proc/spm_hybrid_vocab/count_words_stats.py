import json
import os

import tqdm


def get_words_freq(corpus_file, to_folder):

    # 中文词不动，非中文根据给定 tokenizer处理
    dict_word2freq = {}

    with open(corpus_file, "r", encoding="utf-8") as f:
        for line in tqdm.tqdm(f):
            line = line.strip()

            if not line:
                continue

            line = line.split(" ")
            line = [w.strip() for w in line if len(w.strip()) > 0]

            for w in line:
                if w not in dict_word2freq:
                    dict_word2freq[w] = 0

                dict_word2freq[w] += 1

    list_word2freq = list(dict_word2freq.items())
    list_word2freq = sorted(
        list_word2freq,
        key=lambda x: x[1],
        reverse=True
    )


    json.dump(
        dict_word2freq,
        open(os.path.join(to_folder, "dict_word2freq.json"), "w", encoding="utf-8")
    )


if __name__ == "__main__":
    corpus_file_ = "./tmp/zhwiki-latest-pages-articles_char_segmented_lower_simplified.txt"
    to_folder_ = "./data_proc/spm_hybrid_vocab/"
    get_words_freq(corpus_file_, to_folder_)



