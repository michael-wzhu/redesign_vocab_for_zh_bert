#!/usr/bin/env bash
# @Author: Michael Zhu
# @Date:   2020-03-04
# @Last Modified by:   michael
# @Last Modified time: 2020-03-04 21:28:30


STORAGE_BUCKET=gs://sbt0
TPU_IP=10.165.184.58
TPU_NAME=grpc://${TPU_IP}:8470

PREFIX=char_segmented
VOCAB_SIZE=5282

TASK_NAME=weibo
DATA_DIR=datasets/weibo

DATE=0813

pip3 install tensorflow_hub
pip3 install sentencepiece
pip3 install jieba
pip3 install tokenizers
pip3 install boto3
pip3 install jieba_fast
pip3 install sklearn

# run task

echo "Start running..."
RUN_TIMES=10
for run_idx in `seq 1 $((RUN_TIMES))`; do

    python3 comp_bert/char_segmented/run_classifier.py \
      --task_name=${TASK_NAME} \
      --data_dir=${DATA_DIR} \
      --output_dir=${STORAGE_BUCKET}/experiments/comp_bert/finetune/${TASK_NAME}/${PREFIX}_${VOCAB_SIZE}_length_128_512_time_${DATE}_run_${run_idx}/ \
      --init_checkpoint=${STORAGE_BUCKET}/experiments/comp_bert/pretraining/${PREFIX}_${VOCAB_SIZE}/model.ckpt-125000 \
      --albert_config_file=./comp_bert/albert_configs/config_${VOCAB_SIZE}.json \
      --do_train=true \
      --do_eval=true \
      --do_predict \
      --do_lower_case \
      --max_seq_length=512 \
      --max_num_chars=128 \
      --optimizer=adamw \
      --train_batch_size=256 \
      --eval_batch_size=32 \
      --learning_rate=2e-5 \
      --warmup_step=300 \
      --save_checkpoints_steps=400 \
      --train_step=8000 \
      --use_tpu=True \
      --tpu_name=${TPU_NAME} \
      --num_tpu_cores=8 \
      --vocab_file=data_proc/tokenizers/sentencepiece/${PREFIX}_lower-${VOCAB_SIZE}-clean.vocab \
      --spm_model_file=data_proc/tokenizers/sentencepiece/${PREFIX}_lower-${VOCAB_SIZE}-clean.model \
      --dict_char2comp_dir=data_proc/proc_comps/vocab/dict_char2comps_remapped_joined.json

done