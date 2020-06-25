#!/bin/bash

### run pretrain

### run pretrain

STORAGE_BUCKET=gs://sbt0
TPU_IP=10.240.1.2
TPU_NAME=grpc://${TPU_IP}:8470

PREFIX=char_segmented
VOCAB_SIZE=21128

python3 src/run_pretraining.py --input_file=${STORAGE_BUCKET}/experiments/rethink_vocab/pretrain_tfrecords/${PREFIX}_${VOCAB_SIZE}/zhwiki_train_examples_*_*.tfrecord --output_dir=${STORAGE_BUCKET}/experiments/rethink_vocab/pretraining/${PREFIX}_${VOCAB_SIZE}/ --albert_config_file=./src/config_${VOCAB_SIZE}.json --do_train --do_eval --dev_input_file=${STORAGE_BUCKET}/experiments/rethink_vocab/pretrain_tfrecords/${PREFIX}_${VOCAB_SIZE}/zhwiki_train_examples_150_*.tfrecord --use_tpu --num_tpu_cores=8 --tpu_name=${TPU_NAME} --train_batch_size=1024 --eval_batch_size=64 --max_seq_length=128 --max_predictions_per_seq=13 --optimizer="lamb" --learning_rate=4e-4 --num_train_steps=45000 --num_warmup_steps=3125 --save_checkpoints_steps=5000

