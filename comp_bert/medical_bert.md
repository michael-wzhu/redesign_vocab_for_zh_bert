


## pretraining

1) extract corpus from EMR

```bash

python3 data_proc/proc_medical_data/proc_emr_data.py

```

2) split corpus files for multi-processing

```bash

python3 data_proc/proc_medical_data/split_file_utils.py

```

3) preprocessing text in each file (multi-processing)

```bash

nohup ./comp_bert/char_segmented/scripts_for_medical/char2char_segmented_1_200.sh > logs/char2char_segmented_1_200.log &
nohup ./comp_bert/char_segmented/scripts_for_medical/char2char_segmented_201_400.sh > logs/char2char_segmented_201_400.log &
nohup ./comp_bert/char_segmented/scripts_for_medical/char2char_segmented_401_600.sh > logs/char2char_segmented_401_600.log &
nohup ./comp_bert/char_segmented/scripts_for_medical/char2char_segmented_601_626.sh > logs/char2char_segmented_601_626.log &

```

4) merge files

```bash
nohup python3 data_proc/proc_medical_data/merge_file_utils.py > logs/merge_files.log &
```

5) build vocab

```bash
nohup python3 data_proc/proc_medical_data/build_vocab_spm.py > logs/build_vocab_spm.log &
```

6) prepare tf records
```bash
nohup ./comp_bert/char_segmented/scripts_for_medical/create_pretrain_data_21128_emr_1_100.sh > logs/create_pretrain_data_21128_emr_1_100.log &
nohup ./comp_bert/char_segmented/scripts_for_medical/create_pretrain_data_21128_emr_101_200.sh > logs/create_pretrain_data_21128_emr_101_200.log &
nohup ./comp_bert/char_segmented/scripts_for_medical/create_pretrain_data_21128_emr_201_300.sh > logs/create_pretrain_data_21128_emr_201_300.log &
nohup ./comp_bert/char_segmented/scripts_for_medical/create_pretrain_data_21128_emr_301_400.sh > logs/create_pretrain_data_21128_emr_301_400.log &
nohup ./comp_bert/char_segmented/scripts_for_medical/create_pretrain_data_21128_emr_401_500.sh > logs/create_pretrain_data_21128_emr_401_500.log &
nohup ./comp_bert/char_segmented/scripts_for_medical/create_pretrain_data_21128_emr_501_600.sh > logs/create_pretrain_data_21128_emr_501_600.log &
nohup ./comp_bert/char_segmented/scripts_for_medical/create_pretrain_data_21128_emr_601_626.sh > logs/create_pretrain_data_21128_emr_601_626.log &

nohup ./comp_bert/char_segmented/scripts_for_medical/create_pretrain_data_21128_wiki_1_40.sh > logs/create_pretrain_data_21128_wiki_1_40.log & 
nohup ./comp_bert/char_segmented/scripts_for_medical/create_pretrain_data_21128_wiki_41_110.sh > logs/create_pretrain_data_21128_wiki_41_110.log & 
nohup ./comp_bert/char_segmented/scripts_for_medical/create_pretrain_data_21128_wiki_111_218.sh > logs/create_pretrain_data_21128_wiki_111_218.log & 

```

7) run pretrain

```bash

nohup ./comp_bert/char_segmented/scripts_for_medical/run_pretrain_21128.sh > medical_run_pretrain_21128.log &

```