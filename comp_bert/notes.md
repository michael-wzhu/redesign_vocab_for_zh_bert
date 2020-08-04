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

# vocab=21128
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_21128_1_55.sh > logs/create_pretrain_data_21128_1_55.log &

nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_21128_131_218.sh > logs/create_pretrain_data_21128_131_180.log &
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_21128_131_218.sh > logs/create_pretrain_data_21128_181_218.log &

# vocab=5282


# vocab=1321




```


## pretrain albert

```bash

# vocab=21128
#   params = 128 * 21128 + 512 * 128 + 128 ^ 2 * 12 = 2, 966, 528




# vocab=5282
#   params = 128 * 5282 + 512 * 128 + 128 ^ 2 * 12 = 938, 240

# vocab=1321
#   params = 128 * 1321 + 512 * 128 + 128 ^ 2 * 12 = 431, 232




```
