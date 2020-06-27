#!/usr/bin/env bash
# @Author: Michael Zhu
# @Date:   2020-03-04
# @Last Modified by:   michael
# @Last Modified time: 2020-03-04 21:28:30


STORAGE_BUCKET=gs://sbt0
TPU_IP=10.30.140.18
TPU_NAME=grpc://${TPU_IP}:8470

PREFIX=char_segmented
VOCAB_SIZE=10564

pip3 install tensorflow_hub
pip3 install sentencepiece
pip3 install jieba
pip3 install tokenizers
pip3 install boto3
pip3 install jieba_fast
pip3 install sklearn

# run task

echo "Start running..."
RUN_TIMES=11
for run_idx in `seq 1 $((RUN_TIMES))`; do

    python3 src/char_segmented/run_classifier.py \
      --task_name=chn \
      --data_dir=datasets/ChnSentiCorp \
      --output_dir=${STORAGE_BUCKET}/experiments/rethink_vocab/finetune/chn/${PREFIX}_${VOCAB_SIZE}_length_128_steps_4.5k_time_0625_run_${run_idx}/ \
      --init_checkpoint=${STORAGE_BUCKET}/experiments/rethink_vocab/pretraining/${PREFIX}_${VOCAB_SIZE}/model.ckpt-45000 \
      --albert_config_file=./src/config_${VOCAB_SIZE}.json \
      --do_train=true \
      --do_eval=true \
      --do_predict \
      --do_lower_case \
      --max_seq_length=128 \
      --max_num_chars=128 \
      --optimizer=adamw \
      --train_batch_size=32 \
      --eval_batch_size=32 \
      --learning_rate=2e-5 \
      --warmup_step=250 \
      --save_checkpoints_steps=300 \
      --train_step=6000 \
      --use_tpu=True \
      --tpu_name=${TPU_NAME} \
      --num_tpu_cores=1 \
      --vocab_file=./data_proc/tokenizers/sentencepiece/${PREFIX}-${VOCAB_SIZE}-clean.vocab \
      --spm_model_file=./data_proc/tokenizers/sentencepiece/${PREFIX}-${VOCAB_SIZE}-clean.model

done