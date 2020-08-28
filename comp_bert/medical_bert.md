


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

./comp_bert/char_segmented/scripts_for_medical/char2char_segmented_1_200.sh
./comp_bert/char_segmented/scripts_for_medical/char2char_segmented_201_400.sh
./comp_bert/char_segmented/scripts_for_medical/char2char_segmented_401_600.sh
./comp_bert/char_segmented/scripts_for_medical/char2char_segmented_601_626.sh

```