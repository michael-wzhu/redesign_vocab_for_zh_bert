# coding=utf-8

import json

from tqdm import tqdm

from src.text_utils import sent_segmented2joined

label_name2id = {
    "0": "0",
    "1": "1",
}


def txt2jsonl(from_dir, to_dir):

    f_in = open(from_dir, "r", encoding="utf-8")
    f_out = open(to_dir, "w", encoding="utf-8")

    for i, line in tqdm(enumerate(f_in)):
        if i == 0:
            continue

        line = line.strip()
        if not line:
            continue

        line = line.split("	")
        sentence1 = line[1].strip()
        sentence2 = line[2].strip()
        label = line[3].strip()

        json_ = {
            "label": label_name2id[label],
            "sentence1": sentence1,
            "sentence2": sentence2,
        }
        f_out.write(json.dumps(json_, ensure_ascii=False) + "\n")

    f_out.close()





if __name__ == "__main__":

    from_dir = "datasets/nlpcc-dbqa/train.tsv"
    to_dir = "datasets/nlpcc-dbqa/train.json"
    txt2jsonl(from_dir, to_dir)

    from_dir = "datasets/nlpcc-dbqa/train.tsv"
    to_dir = "datasets/nlpcc-dbqa/dev.json"
    txt2jsonl(from_dir, to_dir)

    from_dir = "datasets/nlpcc-dbqa/test.tsv"
    to_dir = "datasets/nlpcc-dbqa/test.json"
    txt2jsonl(from_dir, to_dir)
