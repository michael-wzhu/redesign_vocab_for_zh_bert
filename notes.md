

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

3. 合并文件
    - data_proc/merge_file_utils.py



### 建立词汇表

'''bash

- nohup python3 data_proc/build_vocab_spm.py > build_vocab_0624.log &

'''
    


|  | #vocab=21128 | #vocab=10564 |  #vocab=5282   |
| :----: | :----: | :----: | 
| char_no_space	     |      char_no_space_21128     |   char_no_space_10564      |   
|  char_spaced       |     char_spaced_21128      |   char_spaced_10564    |   
|  char_segmented       |       char_segmented_21128    |     char_segmented_10564       |

```bash
# /home/michaelwzhu91_gmail_com/redesign_vocab_for_zh_bert/data_proc/tokenizers/sentencepiece/char_segmented-21128-clean.model
# /home/michaelwzhu91_gmail_com/redesign_vocab_for_zh_bert/data_proc/tokenizers/sentencepiece/char_segmented-21128-clean.vocab

```


### 准备预训练 tfrecords

    - max sentence length = 128
    - dupe_factor = 1
    
```bash

# debug
python3 src/char_spaced/create_pretraining_data.py --input_file=datasets/zh_sample/wiki.valid.raw --output_file=experiments/zh_sample/wiki.valid.%s.tfrecord --do_lower_case=True --do_whole_word_mask=True --max_seq_length=128 --max_predictions_per_seq=13 --masked_lm_prob=0.1 --dupe_factor=2 --bert_tokenizer_name data_proc/tokenizers/char_spaced_21128-vocab.txt


# 启动VMs

$ export PROJECT_NAME=subchar-transformers
$ gcloud config set project ${PROJECT_NAME}
$ ctpu up --tpu-size=v3-8 --machine-type=n1-standard-16 --zone=europe-west4-a --tf-version=1.15 --name=h-bert-0


# char_spaced, vocab=21128

./src/char_spaced/scripts/create_pretrain_data_21128_1_75.sh
./src/char_spaced/scripts/create_pretrain_data_21128_76_150.sh
./src/char_spaced/scripts/create_pretrain_data_21128_151_218.sh

# char_segmented, vocab=31692

./src/char_segmented/scripts/create_pretrain_data_31692_1_75.sh
./src/char_segmented/scripts/create_pretrain_data_31692_76_150.sh
./src/char_segmented/scripts/create_pretrain_data_31692_151_218.sh

# char_segmented, vocab=21128

./src/char_segmented/scripts/create_pretrain_data_21128_1_75.sh
./src/char_segmented/scripts/create_pretrain_data_21128_76_150.sh
./src/char_segmented/scripts/create_pretrain_data_21128_151_218.sh

# char_segmented, vocab=10564

./src/char_segmented/scripts/create_pretrain_data_10564_1_75.sh
./src/char_segmented/scripts/create_pretrain_data_10564_76_150.sh
./src/char_segmented/scripts/create_pretrain_data_10564_151_218.sh

# char_no_space, vocab=21128

./src/char_no_space/scripts/create_pretrain_data_21128_1_75.sh
./src/char_no_space/scripts/create_pretrain_data_21128_76_150.sh
./src/char_no_space/scripts/create_pretrain_data_21128_151_218.sh

```

### 预训练

    - max sentence length = 128
    - dupe_factor = 1
    
```bash

# debug
### run pretrain

STORAGE_BUCKET=gs://sbt0
TPU_IP=10.236.58.210
TPU_NAME=grpc://${TPU_IP}:8470

PREFIX=char_segmented
VOCAB_SIZE=21128

python3 src/char_spaced/create_pretraining_data.py --input_file=datasets/zh_sample/wiki.valid.raw --output_file=experiments/zh_sample/wiki.valid.%s.tfrecord --do_lower_case=True --do_whole_word_mask=True --max_seq_length=128 --max_predictions_per_seq=13 --masked_lm_prob=0.1 --dupe_factor=2 --vocab_file data_proc/tokenizers/sentencepiece/char_segmented-21128-clean.vocab --spm_model_file data_proc/tokenizers/sentencepiece/char_segmented-21128-clean.model


python3 src/run_pretraining.py --input_file=experiments/zh_sample/wiki.valid.0.tfrecord --output_dir=experiments/zh_sample/run_debug/ --albert_config_file=./resources/albert_base_v2/config.json --do_train --do_eval --dev_input_file=experiments/zh_sample/wiki.valid.1.tfrecord --use_tpu --num_tpu_cores=8 --tpu_name=grpc://10.77.62.58:8470 --train_batch_size=16 --eval_batch_size=64 --max_seq_length=128 --max_predictions_per_seq=13 --optimizer="lamb" --learning_rate=4e-4 --num_train_steps=100 --num_warmup_steps=5 --save_checkpoints_steps=5


python3 src/run_pretraining.py --input_file=${STORAGE_BUCKET}/data/h_bert/data_records/zhwiki_train_examples_*_*.tfrecord --output_dir=${STORAGE_BUCKET}/experiments/h_bert/pretraining/length_512_sememe_16_steps_125k_time_0507_0/ --albert_config_file=./resources/albert_base_v2/config.json --do_train --do_eval --dev_input_file=${STORAGE_BUCKET}/data/h_bert/data_records/zhwiki_train_examples_110_*.tfrecord --use_tpu --num_tpu_cores=8 --tpu_name=${TPU_NAME} --train_batch_size=1024 --eval_batch_size=64 --max_seq_length=512 --max_sememe_length=16 --max_predictions_per_seq=51 --optimizer="lamb" --learning_rate=4e-4 --num_train_steps=125000 --num_warmup_steps=3125 --save_checkpoints_steps=5000

