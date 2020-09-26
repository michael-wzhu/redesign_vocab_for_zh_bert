# coding=utf-8


from data_proc.wordpiece import text_encoder


if __name__ == "__main__":
    encoder = text_encoder.SubwordTextEncoder(
        filename="data_proc/tokenizers/wordpiece/char.txt.tmp"
    )

    sent = "我喜欢篮球"
    sent = encoder.encode(sent)
    print(sent)

