#!/bin/bash

### multi-processing version

pip3 install jieba_fast
pip3 install tokenizers
pip3 install boto3

export STORAGE_BUCKET=gs://sbt0
PREFIX=char_no_space
# VOCAB_SIZE=21128
# VOCAB_SIZE=31692
VOCAB_SIZE=10564


# NUM_PROC=218
NUM_PROC=75


for i in `seq 1 $((NUM_PROC))`; do
  python3 src/char_no_space/create_pretraining_data.py --input_file=$STORAGE_BUCKET/data/corpus/${PREFIX}_lower/zhwiki-latest-pages-articles_${i}_${PREFIX}_lower_simplified.txt --output_file=${STORAGE_BUCKET}/experiments/rethink_vocab/pretrain_tfrecords/${PREFIX}_${VOCAB_SIZE}/zhwiki_train_examples_${i}_%s.tfrecord --do_lower_case=True --do_whole_word_mask=True --max_seq_length=128 --max_predictions_per_seq=13 --masked_lm_prob=0.1 --dupe_factor=1 --vocab_file data_proc/tokenizers/sentencepiece/${PREFIX}-${VOCAB_SIZE}-clean.vocab --spm_model_file data_proc/tokenizers/sentencepiece/${PREFIX}-${VOCAB_SIZE}-clean.model \
  $@ &
done

# python3 src/char_no_space/create_pretraining_data.py --input_file=gs://sbt0/data/corpus/char_no_space_lower/zhwiki-latest-pages-articles_100_char_no_space_lower_simplified.txt --output_file=gs://sbt0/experiments/rethink_vocab/pretrain_tfrecords/char_no_space_21128/zhwiki_train_examples_100_%s.tfrecord --do_lower_case=True --do_whole_word_mask=True --max_seq_length=128 --max_predictions_per_seq=13 --masked_lm_prob=0.1 --dupe_factor=1 --vocab_file data_proc/tokenizers/sentencepiece/char_no_space-21128-clean.vocab --spm_model_file data_proc/tokenizers/sentencepiece/char_no_space-21128-clean.model