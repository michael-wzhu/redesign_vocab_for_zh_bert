# coding=utf-8

import json

from src.text_utils import sent_segmented2joined

label_name2id = {
    "contradiction": "0",
    "contradictory": "0",
    "neutral": "1",
    "entailment": "2",
}



def xnli_txt2jsonl(from_dir, to_dir):

    f_in = open(from_dir, "r", encoding="utf-8")
    f_out = open(to_dir, "w", encoding="utf-8")

    for i, line in enumerate(f_in):
        if i == 0:
            continue

        line = line.strip()
        if not line:
            continue

        line = line.split("\t")
        sentence1 = line[0].strip()
        sentence2 = line[1].strip()
        label = line[2].strip()

        json_ = {
            "label": label_name2id[label],
            "sentence1": sentence1,
            "sentence2": sentence2,
        }
        f_out.write(json.dumps(json_, ensure_ascii=False) + "\n")

    f_out.close()


def xnli_jsonl2jsonl(from_dir, to_dir):
    f_in = open(from_dir, "r", encoding="utf-8")
    f_out = open(to_dir, "w", encoding="utf-8")

    for i, line in enumerate(f_in):
        if i == 0:
            continue

        line = line.strip()
        if not line:
            continue

        line = json.loads(line)

        lang = line["language"]
        if lang != "zh":
            continue

        label = line["gold_label"]
        sentence1 = line["sentence1"]
        sentence2 = line["sentence2"]


        json_ = {
            "label": label_name2id[label],
            "sentence1": sentence1,
            "sentence2": sentence2,
        }
        f_out.write(json.dumps(json_, ensure_ascii=False) + "\n")


def xnli_sent_join(from_dir, to_dir):
    f_in = open(from_dir, "r", encoding="utf-8")
    f_out = open(to_dir, "w", encoding="utf-8")

    for i, line in enumerate(f_in):

        line = line.strip()
        if not line:
            continue

        line = json.loads(line)

        sentence1 = line["sentence1"]
        sentence1 = sent_segmented2joined(sentence1)

        sentence2 = line["sentence2"]
        sentence2 = sent_segmented2joined(sentence2)

        json_ = {
            "label": line["label"],
            "sentence1": sentence1,
            "sentence2": sentence2,
        }
        f_out.write(json.dumps(json_, ensure_ascii=False) + "\n")






if __name__ == "__main__":
    # from_dir = "datasets/xnli/multinli.train.zh.tsv"
    # to_dir = "datasets/xnli/train.json"
    # xnli_txt2jsonl(from_dir, to_dir)
    #
    # from_dir = "datasets/xnli/xnli.dev.jsonl"
    # to_dir = "datasets/xnli/dev.json"
    # xnli_jsonl2jsonl(from_dir, to_dir)
    #
    # from_dir = "datasets/xnli/xnli.test.jsonl"
    # to_dir = "datasets/xnli/test.json"
    # xnli_jsonl2jsonl(from_dir, to_dir)

    from_dir = "datasets/xnli/test.json"
    to_dir = "datasets/xnli/test.jsonl"
    xnli_sent_join(from_dir, to_dir)

    from_dir = "datasets/xnli/dev.json"
    to_dir = "datasets/xnli/dev.jsonl"
    xnli_sent_join(from_dir, to_dir)

    from_dir = "datasets/xnli/train.json"
    to_dir = "datasets/xnli/train.jsonl"
    xnli_sent_join(from_dir, to_dir)
