#!/bin/bash

### multi-processing version

pip3 install jieba_fast
pip3 install tokenizers
pip3 install boto3
pip3 install tensorflow_hub

export STORAGE_BUCKET=gs://sbt0

PREFIX=char_segmented

VOCAB_SIZE=21128

# NUM_PROC=218
NUM_PROC=218


for i in `seq 111 $((NUM_PROC))`; do
  python3 comp_bert/char_segmented/create_pretraining_data.py \
    --input_file=$STORAGE_BUCKET/data/corpus/${PREFIX}_lower/zhwiki-latest-pages-articles_${i}_${PREFIX}_lower.txt \
    --output_file=${STORAGE_BUCKET}/experiments/ehr_diagnose/experiments/tf_records/${PREFIX}_${VOCAB_SIZE}/zhwiki_train_examples_${i}_%s.tfrecord \
    --do_lower_case=True \
    --do_whole_word_mask=True \
    --max_seq_length=512 \
    --max_predictions_per_seq=51 \
    --masked_lm_prob=0.1 \
    --dupe_factor=10 \
    --vocab_file data_proc/tokenizers/sentencepiece/${PREFIX}_medical_lower-${VOCAB_SIZE}-clean.vocab \
    --spm_model_file data_proc/tokenizers/sentencepiece/${PREFIX}_medical_lower-${VOCAB_SIZE}-clean.model \
  $@ &
done
