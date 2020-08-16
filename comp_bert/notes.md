# comp bert


## prepare dict for mapping zh chars into components (comps)

```bash

step1. 
# since the comp dicts has special comps like &CDP-8CBB;, we need to map it to a char which is not a comp
python data_proc/proc_comps/proc_and_remap.py

```

## preproc corpus

```bash

# comp segmented
nohup ./data_proc/char2comp_segmented_mp.sh > logs/preproc_corpus_char2comp_segmented_mp.log &

# comp spaced
nohup ./data_proc/char2comp_spaced_mp.sh > logs/preproc_corpus_char2comp_spaced_mp.log &


# merge files
nohup python3 data_proc/merge_file_utils.py > logs/merge_files.log &

```

## build vocab

```bash
nohup python3 data_proc/build_spm.py > logs/build_vocab.log &

```


## create pretraining data 

```bash

# subchar_segmented, vocab=21128
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_21128_1_15.sh > logs/create_pretrain_data_21128_1_15.log &
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_21128_16_55.sh > logs/create_pretrain_data_21128_16_55.log &
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_21128_56_130.sh > logs/create_pretrain_data_21128_56_130.log &
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_21128_56_130_tmp.sh > logs/create_pretrain_data_21128_56_130_tmp.log &

nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_21128_131_180.sh > logs/create_pretrain_data_21128_131_180.log &
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_21128_181_218.sh > logs/create_pretrain_data_21128_181_218.log &

# subchar_segmented, vocab=5282
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_5282_1_10.sh > logs/create_pretrain_data_5282_1_10.log &
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_5282_11_55.sh > logs/create_pretrain_data_5282_11_55.log &
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_5282_56_130.sh > logs/create_pretrain_data_5282_56_130.log &
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_5282_131_180.sh > logs/create_pretrain_data_5282_131_180.log &
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_5282_181_218.sh > logs/create_pretrain_data_5282_181_218.log &

# subchar_segmented, vocab=1321
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_1321_1_20.sh > logs/create_pretrain_data_1321_1_20.log &
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_1321_21_55.sh > logs/create_pretrain_data_1321_21_55.log &
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_1321_56_130.sh > logs/create_pretrain_data_1321_56_130.log &
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_1321_131_180.sh > logs/create_pretrain_data_1321_131_180.log &
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_1321_181_218.sh > logs/create_pretrain_data_1321_181_218.log &

# subchar_spaced, vocab=21128
nohup ./comp_bert/comp_spaced/scripts/create_pretrain_data_21128_1_20.sh > logs/comp_spaced_create_pretrain_data_21128_1_20.log &
nohup ./comp_bert/comp_spaced/scripts/create_pretrain_data_21128_21_60.sh > logs/comp_spaced_create_pretrain_data_21128_21_60.log &
nohup ./comp_bert/comp_spaced/scripts/create_pretrain_data_21128_61_110.sh > logs/comp_spaced_create_pretrain_data_21128_61_110.log &
nohup ./comp_bert/comp_spaced/scripts/create_pretrain_data_21128_111_160.sh > logs/comp_spaced_create_pretrain_data_21128_111_160.log &
nohup ./comp_bert/comp_spaced/scripts/create_pretrain_data_21128_161_218.sh > logs/comp_spaced_create_pretrain_data_21128_161_218.log &

# subchar_spaced, vocab=5282
nohup ./comp_bert/comp_spaced/scripts/create_pretrain_data_5282_1_25.sh > logs/comp_spaced_create_pretrain_data_5282_1_25.log &
nohup ./comp_bert/comp_spaced/scripts/create_pretrain_data_5282_26_40.sh > logs/comp_spaced_create_pretrain_data_5282_26_40.log &
nohup ./comp_bert/comp_spaced/scripts/create_pretrain_data_5282_41_60.sh > logs/comp_spaced_create_pretrain_data_5282_41_60.log &
nohup ./comp_bert/comp_spaced/scripts/create_pretrain_data_5282_61_110.sh > logs/comp_spaced_create_pretrain_data_5282_61_110.log &
nohup ./comp_bert/comp_spaced/scripts/create_pretrain_data_5282_111_165.sh > logs/comp_spaced_create_pretrain_data_5282_111_165.log &
nohup ./comp_bert/comp_spaced/scripts/create_pretrain_data_5282_166_218.sh > logs/comp_spaced_create_pretrain_data_5282_166_218.log &

```


## pretrain albert

```bash

# subchar_segmented, vocab=21128
#   params = 128 * 21128 + 512 * 128 + 256 ^ 2 * 12 = 3556352

nohup ./comp_bert/comp_segmented/scripts/run_pretrain_21128.sh > logs/subchar_segmented_pretrain_21128.log &

# subchar_segmented, vocab=5282
#   params = 128 * 5282 + 512 * 128 + 256 ^ 2 * 12 = 1528064
nohup ./comp_bert/comp_segmented/scripts/run_pretrain_5282.sh > logs/subchar_segmented_pretrain_5282.log &

# subchar_segmented, vocab=1321
#   params = 128 * 1321 + 512 * 128 + 128 ^ 2 * 12 = 1021056
nohup ./comp_bert/comp_segmented/scripts/run_pretrain_1321.sh > logs/subchar_segmented_pretrain_1321.log &



```


## finetune


### on chn

```bash

# subchar_segmented, vocab=21128

nohup ./comp_bert/comp_segmented/scripts/run_classifier_chn_21128.sh > logs/subchar_segmented_run_classifier_chn_21128.log_to_commit &




```



### on lcqmc

```bash

# subchar_segmented, vocab=21128

nohup ./comp_bert/comp_segmented/scripts/run_classifier_lcqmc_21128.sh > logs/subchar_segmented_run_classifier_lcqmc_21128.log_to_commit &




```



### on xnli

```bash

# subchar_segmented, vocab=21128

nohup ./comp_bert/comp_segmented/scripts/run_classifier_xnli_21128.sh > logs/subchar_segmented_run_classifier_xnli_21128.log_to_commit &




```