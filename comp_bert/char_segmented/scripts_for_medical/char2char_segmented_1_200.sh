#!/bin/bash

export STORAGE_BUCKET=gs://sbt0

prefix=char_segmented

### multi-processing version
NUM_PROC=200
for i in `seq 1 $((NUM_PROC))`; do
  python3 data_proc/proc_medical_data/char2char_segmented_mp.py ${STORAGE_BUCKET}/experiments/ehr_diagnose/datasets/splited_corpus/outpatient_${i}.txt ${STORAGE_BUCKET}/experiments/ehr_diagnose/datasets/${prefix}_lower/outpatient_${i}_${prefix}_lower_simplified.txt 1 \
    $@ &
done