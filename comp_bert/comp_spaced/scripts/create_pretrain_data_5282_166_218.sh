#!/bin/bash

### multi-processing version

pip3 install jieba_fast
pip3 install tokenizers
pip3 install boto3
pip3 install tensorflow_hub

export STORAGE_BUCKET=gs://sbt0

PREFIX=subchar_spaced

VOCAB_SIZE=5282

# NUM_PROC=218
NUM_PROC=218


for i in `seq 166 $((NUM_PROC))`; do
  python3 comp_bert/comp_spaced/create_pretraining_data.py \
    --input_file=$STORAGE_BUCKET/data/corpus/${PREFIX}_lower/zhwiki-latest-pages-articles_${i}_${PREFIX}_lower.txt \
    --output_file=${STORAGE_BUCKET}/experiments/comp_bert/pretrain_tfrecords/${PREFIX}_${VOCAB_SIZE}/zhwiki_train_examples_${i}_%s.tfrecord \
    --do_lower_case=True \
    --do_whole_word_mask=True \
    --max_seq_length=512 \
    --max_predictions_per_seq=51 \
    --masked_lm_prob=0.1 \
    --dupe_factor=10 \
    --vocab_file data_proc/tokenizers/sentencepiece/${PREFIX}_lower-${VOCAB_SIZE}-clean.vocab \
    --spm_model_file data_proc/tokenizers/sentencepiece/${PREFIX}_lower-${VOCAB_SIZE}-clean.model \
  $@ &
done

# python comp_bert/comp_segmented/create_pretraining_data.py --input_file=datasets/zh_sample/wiki.valid.raw --output_file=experiments/zh_sample/tf_records/zhwiki_examples_%s.tfrecord --do_lower_case=True --do_whole_word_mask=True --max_seq_length=128 --max_predictions_per_seq=13 --masked_lm_prob=0.1 --dupe_factor=10 --vocab_file data_proc/tokenizers/sentencepiece/subchar_segmented_lower-21128-clean.vocab --spm_model_file data_proc/tokenizers/sentencepiece/subchar_segmented_lower-21128-clean.model
