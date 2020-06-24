

### 准备 zh_wiki

0. char_no_space (保持wiki数据的原有样貌)
    - data_proc/char2char_no_space_mp.sh
    - outputs: ${STORAGE_BUCKET}/data/corpus/char_spaced_lower/zhwiki-latest-pages-articles_${i}_char_spaced_lower.txt

1. char_spaced (中文字与字之间拆开):
    - data_proc/char2char_spaced_mp.sh
    - outputs: ${STORAGE_BUCKET}/data/corpus/char_spaced_lower/zhwiki-latest-pages-articles_${i}_char_spaced_lower.txt

2. char_segmented (中文字与字之间拆开)
    - data_proc/char2char_segmented_mp.sh
    - outputs: ${STORAGE_BUCKET}/data/corpus/char_segmented_lower/zhwiki-latest-pages-articles_${i}_char_segmented_lower.txt


### 建立词汇表

    - nohup python3 data_proc/build_wp_vocab_tokenizers.py > build_vocab_0624.log &


|  | #vocab=21128 | #vocab=10564 |  #vocab=5282   |
| :----: | :----: | :----: | 
| char_no_space	     |      char_no_space_21128     |   char_no_space_10564      |   
|  char_spaced       |     char_spaced_21128      |   char_spaced_10564    |   
|  char_segmented       |       char_segmented_21128    |     char_segmented_10564       |   


### 准备预训练 tfrecords

    - max sentence length = 128
    - dupe_factor = 2

