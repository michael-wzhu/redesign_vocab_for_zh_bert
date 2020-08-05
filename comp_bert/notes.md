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
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_21128_1_5.sh > logs/create_pretrain_data_21128_1_5.log &
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_21128_6_55.sh > logs/create_pretrain_data_21128_6_55.log &
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_21128_56_130.sh > logs/create_pretrain_data_21128_56_130.log &
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_21128_131_180.sh > logs/create_pretrain_data_21128_131_180.log &
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_21128_181_218.sh > logs/create_pretrain_data_21128_181_218.log &

# subchar_segmented, vocab=5282
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_5282_1_10.sh > logs/create_pretrain_data_5282_1_10.log &
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_5282_11_55.sh > logs/create_pretrain_data_5282_11_55.log &
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_5282_56_130.sh > logs/create_pretrain_data_5282_56_130.log &
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_5282_131_180.sh > logs/create_pretrain_data_5282_131_180.log &
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_5282_181_218.sh > logs/create_pretrain_data_5282_181_218.log &

# subchar_segmented, vocab=1321
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_1321_1_55.sh > logs/create_pretrain_data_1321_1_55.log &
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_1321_56_130.sh > logs/create_pretrain_data_1321_56_130.log &
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_1321_131_180.sh > logs/create_pretrain_data_1321_131_180.log &
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_1321_181_218.sh > logs/create_pretrain_data_1321_181_218.log &



```


## pretrain albert

```bash

# subchar_segmented, vocab=21128
#   params = 128 * 21128 + 512 * 128 + 128 ^ 2 * 12 = 2, 966, 528

nohup ./comp_bert/comp_segmented/scripts/run_pretrain_21128.sh > subchar_segmented_pretrain_21128.log &

# vocab=5282
#   params = 128 * 5282 + 512 * 128 + 128 ^ 2 * 12 = 938, 240

# vocab=1321
#   params = 128 * 1321 + 512 * 128 + 128 ^ 2 * 12 = 431, 232



```
