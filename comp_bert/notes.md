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


```

## build vocab

```bash
nohup python3 data_proc/build_spm.py > logs/build_vocab.log &

```


## create pretraining data 

```bash

# vocab=21128
nohup ./comp_bert/comp_segmented/scripts/create_pretrain_data_21128_1_55.sh > logs/create_pretrain_data_21128_1_55.log &



```