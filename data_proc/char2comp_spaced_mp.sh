#!/bin/bash

export STORAGE_BUCKET=gs://sbt0

### multi-processing version
NUM_PROC=218
for i in `seq 1 $((NUM_PROC))`; do
  python3 data_proc/char2comp_spaced_mp.py \
    ${STORAGE_BUCKET}/data/corpus/splited/zhwiki-latest-pages-articles_${i}.txt \
    ${STORAGE_BUCKET}/data/corpus/subchar_spaced_lower/zhwiki-latest-pages-articles_${i}_subchar_spaced_lower.txt \
    data_proc/proc_comps/vocab/dict_char2comps_remapped_joined.json \
    1 \
    $@ &
done