#!/bin/bash

export STORAGE_BUCKET=gs://sbt0

### multi-processing version
NUM_PROC=218
for i in `seq 1 $((NUM_PROC))`; do
  python3 data_proc/char2char_no_space_mp.py ${STORAGE_BUCKET}/data/corpus/splited/zhwiki-latest-pages-articles_${i}.txt ${STORAGE_BUCKET}/data/corpus/char_no_space_lower/zhwiki-latest-pages-articles_${i}_char_no_space_lower_simplified.txt 1 \
    $@ &
done