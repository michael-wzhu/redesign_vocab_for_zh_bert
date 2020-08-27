# comp bert


## prepare dict for mapping zh chars into components (comps)

```bash

step1. 
# since the comp dicts has special comps like &CDP-8CBB;, we need to map it to a char which is not a comp
python data_proc/proc_comps/proc_and_remap.py

```

## operation on google cloud

```bash
export PROJECT_ID=comp-bert-286705
gcloud config set project ${PROJECT_ID}
gsutil mb -p ${PROJECT_ID} -c standard -l europe-west4 -b on gs://sbt1
ctpu up --tpu-size=v3-8 --machine-type=n1-standard-16 --zone=europe-west4-a --tf-version=1.15 --name=comp-bert-1

# enter your vm 
ssh-keygen -t rsa -C "michael_wzhu91@163.com"

```


## get and clean corpus

```bash

# download corpus
wget https://dumps.wikimedia.org/zhwiki/20200420/zhwiki-20200420-pages-articles.xml.bz2
# extract corpus
nohup ./data_proc/wiki_preprocess/extract_and_clean.sh > extract_zhwiki.log &
# split data 

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

# comp build vocab
nohup python3 data_proc/build_spm.py > logs/build_vocab.log &

# char build vocab
nohup python3 data_proc/build_vocab_spm.py > logs/build_vocab_spm.log &

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

# subchar_spaced, vocab=1321
nohup ./comp_bert/comp_spaced/scripts/create_pretrain_data_1321_1_2.sh > logs/comp_spaced_create_pretrain_data_1321_1_2.log &
nohup ./comp_bert/comp_spaced/scripts/create_pretrain_data_1321_3_25.sh > logs/comp_spaced_create_pretrain_data_1321_3_25.log &
nohup ./comp_bert/comp_spaced/scripts/create_pretrain_data_1321_26_60.sh > logs/comp_spaced_create_pretrain_data_1321_26_60.log &
nohup ./comp_bert/comp_spaced/scripts/create_pretrain_data_1321_61_105.sh > logs/comp_spaced_create_pretrain_data_1321_61_105.log &
nohup ./comp_bert/comp_spaced/scripts/create_pretrain_data_1321_106_150.sh > logs/comp_spaced_create_pretrain_data_1321_106_150.log &
nohup ./comp_bert/comp_spaced/scripts/create_pretrain_data_1321_151_185.sh > logs/comp_spaced_create_pretrain_data_1321_150_185.log &
nohup ./comp_bert/comp_spaced/scripts/create_pretrain_data_1321_186_218.sh > logs/comp_spaced_create_pretrain_data_1321_186_218.log &


# char_segmented, vocab=21128
nohup ./comp_bert/char_segmented/scripts/create_pretrain_data_21128_1_25.sh > char_segmented_create_pretrain_data_21128_1_25.log &
nohup ./comp_bert/char_segmented/scripts/create_pretrain_data_21128_26_65.sh > char_segmented_create_pretrain_data_21128_26_65.log &
nohup ./comp_bert/char_segmented/scripts/create_pretrain_data_21128_66_120.sh > char_segmented_create_pretrain_data_21128_66_120.log &
nohup ./comp_bert/char_segmented/scripts/create_pretrain_data_21128_121_170.sh > char_segmented_create_pretrain_data_21128_121_170.log &
nohup ./comp_bert/char_segmented/scripts/create_pretrain_data_21128_171_218.sh > char_segmented_create_pretrain_data_21128_171_218.log &

# char_segmented, vocab=5282
nohup ./comp_bert/char_segmented/scripts/create_pretrain_data_5282_1_25.sh > char_segmented_create_pretrain_data_5282_1_25.log &
nohup ./comp_bert/char_segmented/scripts/create_pretrain_data_5282_26_65.sh > char_segmented_create_pretrain_data_5282_26_65.log &
nohup ./comp_bert/char_segmented/scripts/create_pretrain_data_5282_66_120.sh > char_segmented_create_pretrain_data_5282_66_120.log &
nohup ./comp_bert/char_segmented/scripts/create_pretrain_data_5282_121_170.sh > char_segmented_create_pretrain_data_5282_121_170.log &
nohup ./comp_bert/char_segmented/scripts/create_pretrain_data_5282_171_218.sh > char_segmented_create_pretrain_data_5282_171_218.log &


# char_segmented, vocab=1321
nohup ./comp_bert/char_segmented/scripts/create_pretrain_data_1321_1_25.sh > char_segmented_create_pretrain_data_1321_1_25.log &
nohup ./comp_bert/char_segmented/scripts/create_pretrain_data_1321_26_65.sh > char_segmented_create_pretrain_data_1321_26_65.log &
nohup ./comp_bert/char_segmented/scripts/create_pretrain_data_1321_66_120.sh > char_segmented_create_pretrain_data_1321_66_120.log &
nohup ./comp_bert/char_segmented/scripts/create_pretrain_data_1321_121_170.sh > char_segmented_create_pretrain_data_1321_121_170.log &
nohup ./comp_bert/char_segmented/scripts/create_pretrain_data_1321_171_218.sh > char_segmented_create_pretrain_data_1321_171_218.log &


# char_spaced, vocab=21128
nohup ./comp_bert/char_spaced/scripts/create_pretrain_data_21128_1_25.sh > char_spaced_create_pretrain_data_21128_1_25.log &
nohup ./comp_bert/char_spaced/scripts/create_pretrain_data_21128_26_65.sh > char_spaced_create_pretrain_data_21128_26_65.log &
nohup ./comp_bert/char_spaced/scripts/create_pretrain_data_21128_66_115.sh > char_spaced_create_pretrain_data_21128_66_115.log &
nohup ./comp_bert/char_spaced/scripts/create_pretrain_data_21128_116_175.sh > char_spaced_create_pretrain_data_21128_116_175.log &
nohup ./comp_bert/char_spaced/scripts/create_pretrain_data_21128_176_218.sh > char_spaced_create_pretrain_data_21128_176_218.log &


# char_spaced, vocab=5282
nohup ./comp_bert/char_spaced/scripts/create_pretrain_data_5282_1_25.sh > char_spaced_create_pretrain_data_5282_1_25.log &
nohup ./comp_bert/char_spaced/scripts/create_pretrain_data_5282_26_65.sh > char_spaced_create_pretrain_data_5282_26_65.log &
nohup ./comp_bert/char_spaced/scripts/create_pretrain_data_5282_66_115.sh > char_spaced_create_pretrain_data_5282_66_115.log &
nohup ./comp_bert/char_spaced/scripts/create_pretrain_data_5282_116_175.sh > char_spaced_create_pretrain_data_5282_116_175.log &
nohup ./comp_bert/char_spaced/scripts/create_pretrain_data_5282_176_218.sh > char_spaced_create_pretrain_data_5282_176_218.log &

# char_spaced, vocab=1321
nohup ./comp_bert/char_spaced/scripts/create_pretrain_data_1321_1_25.sh > char_spaced_create_pretrain_data_1321_1_25.log &
nohup ./comp_bert/char_spaced/scripts/create_pretrain_data_1321_26_65.sh > char_spaced_create_pretrain_data_1321_26_65.log &
nohup ./comp_bert/char_spaced/scripts/create_pretrain_data_1321_66_115.sh > char_spaced_create_pretrain_data_1321_66_115.log &
nohup ./comp_bert/char_spaced/scripts/create_pretrain_data_1321_116_175.sh > char_spaced_create_pretrain_data_1321_116_175.log &
nohup ./comp_bert/char_spaced/scripts/create_pretrain_data_1321_176_218.sh > char_spaced_create_pretrain_data_1321_176_218.log &

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

# subchar_spaced, vocab=21128
nohup ./comp_bert/comp_spaced/scripts/run_pretrain_21128.sh > logs/subchar_spaced_pretrain_21128.log &

# subchar_spaced, vocab=5282
nohup ./comp_bert/comp_spaced/scripts/run_pretrain_5282.sh > logs/subchar_spaced_pretrain_5282.log &

# subchar_spaced, vocab=1321
nohup ./comp_bert/comp_spaced/scripts/run_pretrain_1321.sh > logs/subchar_spaced_pretrain_1321.log &


# char_segmented, vocab=21128
nohup ./comp_bert/char_segmented/scripts/run_pretrain_21128.sh > logs/char_segmented_pretrain_21128.log & (xxx)

# char_segmented, vocab=5282
nohup ./comp_bert/char_segmented/scripts/run_pretrain_5282.sh > logs/char_segmented_pretrain_5282.log &


# char_spaced, vocab=5282
nohup ./comp_bert/char_spaced/scripts/run_pretrain_5282.sh > logs/char_spaced_pretrain_5282.log & (xxx)



```


## finetune


### on chn

```bash

# subchar_segmented, vocab=21128

nohup ./comp_bert/comp_segmented/scripts/run_classifier_chn_21128.sh > logs/subchar_segmented_run_classifier_chn_21128.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_chn_21128.log_to_commit (done)

INFO:tensorflow:accuracy: 0.868333
I0816 00:54:27.931452 140557174580992 run_classifier.py:535] accuracy: 0.868333
INFO:tensorflow:accuracy: 0.860000
I0816 01:16:27.080199 140429697218304 run_classifier.py:535] accuracy: 0.860000
INFO:tensorflow:accuracy: 0.865833
I0816 01:52:24.093982 140656895477504 run_classifier.py:535] accuracy: 0.865833
INFO:tensorflow:accuracy: 0.838333
I0816 02:31:23.787106 140568041797376 run_classifier.py:535] accuracy: 0.838333
INFO:tensorflow:accuracy: 0.839167
I0816 03:10:23.741451 140332852242176 run_classifier.py:535] accuracy: 0.839167

def get_stat(a):
    score_list = [float(w.split(" ")[-1]) for w in a.split("\n")]
    return np.mean(score_list), np.std(score_list)
    
score_stats = get_stat(a)
print(get_stat(""""""))

(0.8543331999999999, 0.013010552984404622)

# subchar_segmented, vocab=5282
nohup ./comp_bert/comp_segmented/scripts/run_classifier_chn_5282.sh > logs/subchar_segmented_run_classifier_chn_5282.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_chn_5282.log_to_commit (done)

INFO:tensorflow:accuracy: 0.847500
I0816 00:57:41.212886 139674096645888 run_classifier.py:535] accuracy: 0.847500
INFO:tensorflow:accuracy: 0.837500
I0816 01:19:11.547511 139753967494912 run_classifier.py:535] accuracy: 0.837500
INFO:tensorflow:accuracy: 0.812500
I0816 01:55:45.764172 140012370401024 run_classifier.py:535] accuracy: 0.812500
INFO:tensorflow:accuracy: 0.830000
I0816 02:34:45.525974 139710009972480 run_classifier.py:535] accuracy: 0.830000
INFO:tensorflow:accuracy: 0.847500
I0816 03:13:45.693686 140676589967104 run_classifier.py:535] accuracy: 0.847500

(0.835, 0.013038404810405314)


# subchar_segmented, vocab=1321
nohup ./comp_bert/comp_segmented/scripts/run_classifier_chn_1321.sh > logs/subchar_segmented_run_classifier_chn_1321.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_chn_1321.log_to_commit (done)

INFO:tensorflow:accuracy: 0.818333
I0816 00:58:11.826314 140210183026432 run_classifier.py:535] accuracy: 0.818333
INFO:tensorflow:accuracy: 0.819167
I0816 01:19:43.956153 140659666052864 run_classifier.py:535] accuracy: 0.819167
INFO:tensorflow:accuracy: 0.835833
I0816 01:56:17.189684 140058013034240 run_classifier.py:535] accuracy: 0.835833
INFO:tensorflow:accuracy: 0.818333
I0816 02:35:16.322833 140063805449984 run_classifier.py:535] accuracy: 0.818333
INFO:tensorflow:accuracy: 0.815000
I0816 03:14:16.310876 140641165555456 run_classifier.py:535] accuracy: 0.815000

(0.8213332, 0.007389836869647427)

# subchar_spaced, vocab=21128
nohup ./comp_bert/comp_spaced/scripts/run_classifier_chn_21128.sh > logs/subchar_spaced_run_classifier_chn_21128.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_chn_21128.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.867500
I0818 01:54:01.697374 140417316640512 run_classifier.py:535] accuracy: 0.867500
INFO:tensorflow:accuracy: 0.851667
I0818 02:23:11.272128 140645897656064 run_classifier.py:535] accuracy: 0.851667
INFO:tensorflow:accuracy: 0.860000
I0818 03:02:11.088569 140113584707328 run_classifier.py:535] accuracy: 0.860000
INFO:tensorflow:accuracy: 0.851667
I0818 03:41:11.346127 140345565591296 run_classifier.py:535] accuracy: 0.851667
INFO:tensorflow:accuracy: 0.842500
I0818 04:20:11.198344 140162194126592 run_classifier.py:535] accuracy: 0.842500
INFO:tensorflow:accuracy: 0.861667
I0818 04:59:11.123415 140494273193728 run_classifier.py:535] accuracy: 0.861667
INFO:tensorflow:accuracy: 0.844167
I0818 05:38:11.067501 140293848680192 run_classifier.py:535] accuracy: 0.844167
INFO:tensorflow:accuracy: 0.865000
I0818 06:17:11.186089 140251235993344 run_classifier.py:535] accuracy: 0.865000
INFO:tensorflow:accuracy: 0.850000
I0818 06:56:11.828765 140518584231680 run_classifier.py:535] accuracy: 0.850000

(0.8549075555555555, 0.008475085330427344)

# subchar_spaced, vocab=5282
nohup ./comp_bert/comp_spaced/scripts/run_classifier_chn_5282.sh > logs/subchar_spaced_run_classifier_chn_5282.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_chn_5282.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.850000
I0818 02:02:22.900762 140681070556928 run_classifier.py:535] accuracy: 0.850000
INFO:tensorflow:accuracy: 0.860000
I0818 02:26:02.675067 139633414964992 run_classifier.py:535] accuracy: 0.860000
INFO:tensorflow:accuracy: 0.835833
I0818 03:05:02.598013 139728019121920 run_classifier.py:535] accuracy: 0.835833
INFO:tensorflow:accuracy: 0.860833
I0818 03:44:02.611442 140154795931392 run_classifier.py:535] accuracy: 0.860833
INFO:tensorflow:accuracy: 0.841667
I0818 04:23:02.852504 140151308867328 run_classifier.py:535] accuracy: 0.841667
INFO:tensorflow:accuracy: 0.860833
I0818 05:02:02.679408 140595560306432 run_classifier.py:535] accuracy: 0.860833
INFO:tensorflow:accuracy: 0.846667
I0818 05:41:02.703604 140476429760256 run_classifier.py:535] accuracy: 0.846667
INFO:tensorflow:accuracy: 0.833333
I0818 06:20:02.678305 139957598525184 run_classifier.py:535] accuracy: 0.833333
INFO:tensorflow:accuracy: 0.843333
I0818 06:59:02.812633 139909880432384 run_classifier.py:535] accuracy: 0.843333
INFO:tensorflow:accuracy: 0.847500
I0818 07:38:02.634936 139863310726912 run_classifier.py:535] accuracy: 0.847500

(0.8479998999999999, 0.009510221989522621)


# subchar_spaced, vocab=1321
nohup ./comp_bert/comp_spaced/scripts/run_classifier_chn_1321.sh > logs/subchar_spaced_run_classifier_chn_1321.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_chn_1321.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.817500
I0820 12:52:27.097616 139776148637440 run_classifier.py:535] accuracy: 0.817500
INFO:tensorflow:accuracy: 0.832500
I0820 13:27:55.167342 139880742872832 run_classifier.py:535] accuracy: 0.832500



```



### on lcqmc

```bash

# subchar_segmented, vocab=21128
nohup ./comp_bert/comp_segmented/scripts/run_classifier_lcqmc_21128.sh > logs/subchar_segmented_run_classifier_lcqmc_21128.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_lcqmc_21128.log_to_commit (done)

INFO:tensorflow:accuracy: 0.747520
I0817 02:06:01.998881 140252774156032 run_classifier.py:535] accuracy: 0.747520
INFO:tensorflow:accuracy: 0.747600
I0817 02:32:55.255206 140248646907648 run_classifier.py:535] accuracy: 0.747600
INFO:tensorflow:accuracy: 0.754960
I0817 02:59:57.580595 139758842013440 run_classifier.py:535] accuracy: 0.754960
INFO:tensorflow:accuracy: 0.760560
I0817 03:29:39.445030 139810710734592 run_classifier.py:535] accuracy: 0.760560
INFO:tensorflow:accuracy: 0.755280
I0817 04:17:24.535227 139938314598144 run_classifier.py:535] accuracy: 0.755280

(0.753184, 0.0050042925573950976)

# subchar_segmented, vocab=5282
nohup ./comp_bert/comp_segmented/scripts/run_classifier_lcqmc_5282.sh > logs/subchar_segmented_run_classifier_lcqmc_5282.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_lcqmc_5282.log_to_commit (done)

INFO:tensorflow:accuracy: 0.769760
I0816 05:13:20.132289 139764198987520 run_classifier.py:535] accuracy: 0.770160
INFO:tensorflow:accuracy: 0.769760
I0816 05:50:36.097698 140664251246336 run_classifier.py:535] accuracy: 0.769760
INFO:tensorflow:accuracy: 0.770160
I0816 06:16:48.525429 139632845608704 run_classifier.py:535] accuracy: 0.770160
INFO:tensorflow:accuracy: 0.755600
I0816 06:42:46.548686 140300511172352 run_classifier.py:535] accuracy: 0.755600

(0.76637, 0.0062204742584468274)

# subchar_segmented, vocab=1321
nohup ./comp_bert/comp_segmented/scripts/run_classifier_lcqmc_1321.sh > logs/subchar_segmented_run_classifier_lcqmc_1321.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_lcqmc_1321.log_to_commit (done)

INFO:tensorflow:accuracy: 0.740160
I0816 04:59:59.052143 139844458825472 run_classifier.py:535] accuracy: 0.740160
INFO:tensorflow:accuracy: 0.754000
I0816 05:39:10.810330 140268642195200 run_classifier.py:535] accuracy: 0.754000
INFO:tensorflow:accuracy: 0.748960
I0816 06:05:10.869757 140249215497984 run_classifier.py:535] accuracy: 0.748960
INFO:tensorflow:accuracy: 0.745440
I0816 06:30:57.283895 140280868562688 run_classifier.py:535] accuracy: 0.745440
INFO:tensorflow:accuracy: 0.745280
I0816 06:56:44.459246 140255385433856 run_classifier.py:535] accuracy: 0.745280

(0.746768, 0.004577118744363078)

# subchar_spaced, vocab=21128
nohup ./comp_bert/comp_spaced/scripts/run_classifier_lcqmc_21128.sh > logs/subchar_spaced_run_classifier_lcqmc_21128.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_lcqmc_21128.log_to_commit (done)

INFO:tensorflow:accuracy: 0.770480
I0817 15:27:56.081325 140222761281280 run_classifier.py:535] accuracy: 0.770480
INFO:tensorflow:accuracy: 0.764720
I0817 15:57:27.731256 139720781915904 run_classifier.py:535] accuracy: 0.764720
INFO:tensorflow:accuracy: 0.770960
I0817 16:29:13.251104 140426667714304 run_classifier.py:535] accuracy: 0.770960
INFO:tensorflow:accuracy: 0.757840
I0817 17:00:45.515532 140218523662080 run_classifier.py:535] accuracy: 0.757840
INFO:tensorflow:accuracy: 0.765280
I0817 17:30:24.109249 140695221286656 run_classifier.py:535] accuracy: 0.765280

(0.765856, 0.004760477286995519)

# subchar_spaced, vocab=5282
nohup ./comp_bert/comp_spaced/scripts/run_classifier_lcqmc_5282.sh > logs/subchar_spaced_run_classifier_lcqmc_5282.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_lcqmc_5282.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.752240
I0818 02:14:16.074770 140237978208000 run_classifier.py:535] accuracy: 0.752240
INFO:tensorflow:accuracy: 0.763600
I0818 02:44:41.297156 140673806321408 run_classifier.py:535] accuracy: 0.763600
INFO:tensorflow:accuracy: 0.766960
I0818 03:11:17.784155 140047069304576 run_classifier.py:535] accuracy: 0.766960
INFO:tensorflow:accuracy: 0.773040
I0818 03:38:39.745694 140029444650752 run_classifier.py:535] accuracy: 0.773040
INFO:tensorflow:accuracy: 0.765920
I0818 04:06:13.452164 139845657532160 run_classifier.py:535] accuracy: 0.765920

(0.764352, 0.006811867291719631)


# subchar_spaced, vocab=1321
nohup ./comp_bert/comp_spaced/scripts/run_classifier_lcqmc_1321.sh > logs/subchar_spaced_run_classifier_lcqmc_1321.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_lcqmc_1321.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.751200
I0820 13:02:51.680398 140344161847040 run_classifier.py:535] accuracy: 0.751200
INFO:tensorflow:accuracy: 0.763760
I0820 13:28:11.201745 140665486157568 run_classifier.py:535] accuracy: 0.763760
INFO:tensorflow:accuracy: 0.756000
I0820 13:54:01.959968 139947559216896 run_classifier.py:535] accuracy: 0.756000
INFO:tensorflow:accuracy: 0.752880
I0820 14:28:09.731598 140372300658432 run_classifier.py:535] accuracy: 0.752880
INFO:tensorflow:accuracy: 0.756480
I0820 14:53:18.328680 140181488297728 run_classifier.py:535] accuracy: 0.756480

```



### on xnli

```bash

# subchar_segmented, vocab=21128
nohup ./comp_bert/comp_segmented/scripts/run_classifier_xnli_21128.sh > logs/subchar_segmented_run_classifier_xnli_21128.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_xnli_21128.log_to_commit

INFO:tensorflow:accuracy: 0.554291
I0813 05:08:50.479553 140252936034048 run_classifier.py:535] accuracy: 0.554291
INFO:tensorflow:accuracy: 0.577246
I0813 06:04:54.744012 140718557275904 run_classifier.py:535] accuracy: 0.577246
INFO:tensorflow:accuracy: 0.566068
I0813 06:45:24.131435 139821034039040 run_classifier.py:535] accuracy: 0.566068
INFO:tensorflow:accuracy: 0.570060
I0813 07:25:45.793235 139746511324928 run_classifier.py:535] accuracy: 0.570060
INFO:tensorflow:accuracy: 0.546108
I0813 08:06:17.681382 140012420654848 run_classifier.py:535] accuracy: 0.546108

(0.5627546000000001, 0.011163243070004348)

# subchar_segmented, vocab=5282
nohup ./comp_bert/comp_segmented/scripts/run_classifier_xnli_5282.sh > logs/subchar_segmented_run_classifier_xnli_5282.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_xnli_5282.log_to_commit (done)

INFO:tensorflow:accuracy: 0.555489
I0817 14:28:06.702242 140355311015680 run_classifier.py:535] accuracy: 0.555489
INFO:tensorflow:accuracy: 0.548503
I0817 15:12:18.630607 139958656132864 run_classifier.py:535] accuracy: 0.548503
INFO:tensorflow:accuracy: 0.556287
I0817 15:57:10.870271 140448366397184 run_classifier.py:535] accuracy: 0.556287
INFO:tensorflow:accuracy: 0.566667
I0817 16:45:36.266384 140682197907200 run_classifier.py:535] accuracy: 0.566667
INFO:tensorflow:accuracy: 0.564271
I0817 17:31:51.893543 139713861822208 run_classifier.py:535] accuracy: 0.564271

(0.5582434, 0.006535726603829155)

# subchar_segmented, vocab=1321

nohup ./comp_bert/comp_segmented/scripts/run_classifier_xnli_1321.sh > logs/subchar_segmented_run_classifier_xnli_1321.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_xnli_1321.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.523752
I0817 14:32:40.793073 139827565266688 run_classifier.py:535] accuracy: 0.523752
INFO:tensorflow:accuracy: 0.535529
I0817 15:16:07.449097 139664568362752 run_classifier.py:535] accuracy: 0.535529
INFO:tensorflow:accuracy: 0.513373
I0817 16:02:42.353504 140649203902208 run_classifier.py:535] accuracy: 0.513373
INFO:tensorflow:accuracy: 0.519361
I0817 16:48:13.826911 139625524750080 run_classifier.py:535] accuracy: 0.519361
INFO:tensorflow:accuracy: 0.532735
I0817 17:35:31.457537 139817767814912 run_classifier.py:535] accuracy: 0.532735

(0.5249499999999999, 0.008236753243845553)

# subchar_spaced, vocab=21128
nohup ./comp_bert/comp_spaced/scripts/run_classifier_xnli_21128.sh > logs/subchar_spaced_run_classifier_xnli_21128.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_xnli_21128.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.561876
I0817 15:42:30.081303 140610626606848 run_classifier.py:535] accuracy: 0.561876
INFO:tensorflow:accuracy: 0.561477
I0817 16:24:50.796932 140345807431424 run_classifier.py:535] accuracy: 0.561477
INFO:tensorflow:accuracy: 0.571257
I0817 17:10:30.171856 140056315913984 run_classifier.py:535] accuracy: 0.571257
INFO:tensorflow:accuracy: 0.554691
I0817 17:52:13.622805 139968717219584 run_classifier.py:535] accuracy: 0.554691
INFO:tensorflow:accuracy: 0.567066
I0817 18:33:36.321908 140649326024448 run_classifier.py:535] accuracy: 0.567066

(0.5632733999999999, 0.0056028395158169405)

# subchar_spaced, vocab=5282
nohup ./comp_bert/comp_spaced/scripts/run_classifier_xnli_5282.sh > logs/subchar_spaced_run_classifier_xnli_5282.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_xnli_5282.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.572455
I0818 02:32:35.706082 139705360221952 run_classifier.py:535] accuracy: 0.572455
INFO:tensorflow:accuracy: 0.564271
I0818 03:14:39.891002 140447274555136 run_classifier.py:535] accuracy: 0.564271
INFO:tensorflow:accuracy: 0.559082
I0818 03:55:07.032151 139739424511744 run_classifier.py:535] accuracy: 0.559082
INFO:tensorflow:accuracy: 0.560679
I0818 04:35:04.866047 139912522012416 run_classifier.py:535] accuracy: 0.560679
INFO:tensorflow:accuracy: 0.573253
I0818 05:14:57.125636 140383648057088 run_classifier.py:535] accuracy: 0.573253

(0.565948, 0.005889324579270546)


# subchar_spaced, vocab=1321
nohup ./comp_bert/comp_spaced/scripts/run_classifier_xnli_1321.sh > logs/subchar_spaced_run_classifier_xnli_1321.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_xnli_1321.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.554691
I0821 02:51:44.661673 139870592382720 run_classifier.py:535] accuracy: 0.554691
INFO:tensorflow:accuracy: 0.556088
I0821 03:30:41.917270 139772805216000 run_classifier.py:535] accuracy: 0.556088

```


### on nlpcc_dbqa

```bash

# subchar_segmented, vocab=21128
nohup ./comp_bert/comp_segmented/scripts/run_classifier_nlpcc_dbqa_21128.sh > logs/subchar_segmented_run_classifier_nlpcc_dbqa_21128.log_to_commit &
grep "macro avg" logs/subchar_segmented_run_classifier_nlpcc_dbqa_21128.log_to_commit   (xxx)


[0.5653318632352904,

{'0': {'precision': 0.9560297321542996, 'support': 77456, 'f1-score': 0.9595590599796766, 'recall': 0.9631145424499
07}, 'accuracy': 0.9228806907378336, 'weighted avg': {'precision': 0.9174535516126049, 'support': 81536, 'f1-score'
: 0.920105396255258, 'recall': 0.9228806907378336}, 'macro avg': {'precision': 0.5705704850161116, 'support': 81536
, 'f1-score': 0.5653318632352904, 'recall': 0.5610915849504436}, '1': {'precision': 0.18511123787792355, 'support':
 4080, 'f1-score': 0.17110466649090428, 'recall': 0.15906862745098038}}
  "macro avg": {
  "macro avg": {
  

  
{'accuracy': 0.9250269819466248, 'macro avg': {'recall': 0.539118603958832, 'f1-score': 0.5445810064739607, 'suppor
t': 81536, 'precision': 0.5536225411426025}, 'weighted avg': {'recall': 0.9250269819466248, 'f1-score': 0.919171453
6685476, 'support': 81536, 'precision': 0.9137675424434607}, '1': {'recall': 0.11029411764705882, 'f1-score': 0.128
33309567945245, 'support': 4080, 'precision': 0.15342652574156154}, '0': {'recall': 0.9679430902706052, 'f1-score':
 0.960828917268469, 'support': 77456, 'precision': 0.9538185565436433}}
  "macro avg": {
  "macro avg": {
  
   
  
{'weighted avg': {'f1-score': 0.9102833822427759, 'recall': 0.9059433869701727, 'precision': 0.914831202088968, 'su
pport': 81536}, '0': {'f1-score': 0.950209381593897, 'recall': 0.9447686428423879, 'precision': 0.9557131476184879,
 'support': 77456}, 'accuracy': 0.9059433869701727, '1': {'f1-score': 0.15231568475737817, 'recall': 0.168872549019
60785, 'precision': 0.13871552244815785, 'support': 4080}, 'macro avg': {'f1-score': 0.5512625331756376, 'recall': 
0.5568205959309979, 'precision': 0.5472143350333228, 'support': 81536}}
  "macro avg": {
  "macro avg": {
  
   
  
{'0': {'precision': 0.9555312983249515, 'recall': 0.9493260689940095, 'support': 77456, 'f1-score': 0.9524185766373
722}, '1': {'precision': 0.143574078114772, 'recall': 0.16127450980392158, 'support': 4080, 'f1-score': 0.151910423
64077112}, 'accuracy': 0.9098925627943485, 'weighted avg': {'precision': 0.9149015708615301, 'recall': 0.9098925627
943485, 'support': 81536, 'f1-score': 0.9123617518700777}, 'macro avg': {'precision': 0.5495526882198618, 'recall':
 0.5553002893989656, 'support': 81536, 'f1-score': 0.5521645001390716}}
  "macro avg": {
  "macro avg": {
  
  
  
{'1': {'f1-score': 0.16763814408953134, 'recall': 0.17622549019607844, 'precision': 0.15984882169853268, 'support':
 4080}, '0': {'f1-score': 0.9537846129946795, 'recall': 0.9512110101218757, 'precision': 0.9563721799631351, 'suppo
rt': 77456}, 'weighted avg': {'f1-score': 0.9144464360773301, 'recall': 0.9124313186813187, 'precision': 0.91651475
13215585, 'support': 81536}, 'macro avg': {'f1-score': 0.5607113785421054, 'recall': 0.563718250158977, 'precision'
: 0.5581105008308339, 'support': 81536}, 'accuracy': 0.9124313186813187}
  "macro avg": {
  "macro avg": {
  
  
  
{'accuracy': 0.9172758045525903, '1': {'recall': 0.11372549019607843, 'precision': 0.12913999443362092, 'f1-score':
 0.12094356835657499, 'support': 4080}, 'macro avg': {'recall': 0.5366641807518298, 'precision': 0.5413735587938604
, 'f1-score': 0.538769585322439, 'support': 81536}, '0': {'recall': 0.959602871307581, 'precision': 0.9536071231540
998, 'f1-score': 0.956595602288303, 'support': 77456}, 'weighted avg': {'recall': 0.9172758045525903, 'precision': 
0.9123514092954416, 'f1-score': 0.91478020420106, 'support': 81536}}
  "macro avg": {
  "macro avg": {
  
  
  
{'1': {'f1-score': 0.17438364401683704, 'recall': 0.17769607843137256, 'support': 4080, 'precision': 0.171192443919
71664}, 'weighted avg': {'f1-score': 0.9165466466084283, 'recall': 0.9158040620094191, 'support': 81536, 'precision
': 0.9172971190307241}, '0': {'f1-score': 0.9556401325949716, 'recall': 0.9546839495971907, 'support': 77456, 'prec
ision': 0.9565982328818514}, 'macro avg': {'f1-score': 0.5650118883059043, 'recall': 0.5661900140142816, 'support':
 81536, 'precision': 0.563895338400784}, 'accuracy': 0.9158040620094191}
  "macro avg": {
  "macro avg": {
  
  
  
{'weighted avg': {'support': 81536, 'f1-score': 0.9194785707280703, 'precision': 0.9178969214603176, 'recall': 0.92
11023351648352}, '1': {'support': 4080, 'f1-score': 0.17747091164812684, 'precision': 0.1855118952151831, 'recall':
 0.17009803921568628}, 'macro avg': {'support': 81536, 'f1-score': 0.5680173928164177, 'precision': 0.5709936235507
755, 'recall': 0.5653797880441166}, '0': {'support': 77456, 'f1-score': 0.9585638739847085, 'precision': 0.95647535
1886368, 'recall': 0.960661536872547}, 'accuracy': 0.9211023351648352}
  "macro avg": {
  "macro avg": {
  
  
  
{'accuracy': 0.9231137166405023, 'weighted avg': {'support': 81536, 'f1-score': 0.9196308036658545, 'precision': 0.
9163308019408164, 'recall': 0.9231137166405023}, 'macro avg': {'support': 81536, 'f1-score': 0.5591763291556254, 'p
recision': 0.56534127513957, 'recall': 0.554480798206496}, '1': {'support': 4080, 'f1-score': 0.15863642464098782, 
'precision': 0.17531889646989024, 'recall': 0.1448529411764706}, '0': {'support': 77456, 'f1-score': 0.959716233670
263, 'precision': 0.9553636538092497, 'recall': 0.9641086552365213}}

[0.5653318632352904,0.5445810064739607,0.5512625331756376,0.5521645001390716, 0.5607113785421054, 0.538769585322439, 0.5650118883059043, 0.5680173928164177, 0.5591763291556254, ]

(0.5561140530184947, 0.009482)

# subchar_segmented, vocab=5282
nohup ./comp_bert/comp_segmented/scripts/run_classifier_nlpcc_dbqa_5282.sh > logs/subchar_segmented_run_classifier_nlpcc_dbqa_5282.log_to_commit &
grep "macro avg" logs/subchar_segmented_run_classifier_nlpcc_dbqa_5282.log_to_commit  (xxx)



{'1': {'support': 4080, 'precision': 0.2077028885832187, 'f1-score': 0.19572261827608556, 'recall': 0.18504901960784315}, '0': {'support': 77456, 'precision': 0.9573176210831696, 'f1-score': 0.9600597333882606, 'recall': 0.9628175996694898}, 'macro avg': {'support': 81536, 'precision': 0.5825102548331942, 'f1-score': 0.5778911758321731, 'recall': 0.5739333096386665}, 'accuracy': 0.9238986459968603, 'weighted avg': {'support': 81536, 'precision': 0.9198074647276973, 'f1-score': 0.9218128801006615, 'recall': 0.9238986459968603}}



  "macro avg": {
  "macro avg": {
{'accuracy': 0.9129586930926217, 'macro avg': {'recall': 0.5780431698603837, 'f1-score': 0.5727065298044567, 'precision': 0.5683357341765309, 'support': 81536}, 'weighted avg': {'recall': 0.9129586930926217, 'f1-score': 0.9158440486465572, 'precision': 0.9188535217819074, 'support': 81536}, '0': {'recall': 0.950203986779591, 'f1-score': 0.954003694222107, 'precision': 0.9578339124663257, 'support': 77456}, '1': {'recall': 0.20588235294117646, 'f1-score': 0.19140936538680645, 'precision': 0.17883755588673622, 'support': 4080}}
  "macro avg": {
  "macro avg": {
  
  
  
{'1': {'precision': 0.18651488616462347, 'f1-score': 0.19703977798334876, 'support': 4080, 'recall': 0.2088235294117647}, '0': {'precision': 0.9580604926722794, 'f1-score': 0.9550328964409678, 'support': 77456, 'recall': 0.9520243751291055}, 'macro avg': {'precision': 0.5722876894184514, 'f1-score': 0.5760363372121583, 'support': 81536, 'recall': 0.5804239522704351}, 'accuracy': 0.9148351648351648, 'weighted avg': {'precision': 0.9194529319070808, 'f1-score': 0.9171034919655571, 'support': 81536, 'recall': 0.9148351648351648}}
  "macro avg": {
  "macro avg": {
  

  
{'0': {'precision': 0.9577666520426333, 'support': 77456, 'recall': 0.9582859946292088, 'f1-score': 0.9580262529524891}, '1': {'precision': 0.199851411589896, 'support': 4080, 'recall': 0.19779411764705881, 'f1-score': 0.19881744271988172}, 'accuracy': 0.9202315541601256, 'weighted avg': {'precision': 0.9198411445239033, 'support': 81536, 'recall': 0.9202315541601256, 'f1-score': 0.9200360161767209}, 'macro avg': {'precision': 0.5788090318162646, 'support': 81536, 'recall': 0.5780400561381338, 'f1-score': 0.5784218478361854}}
  "macro avg": {
  "macro avg": {
  
    
  
{'accuracy': 0.9251128335949764, 'macro avg': {'recall': 0.5566939459113536, 'f1-score': 0.5626384782322722, 'precision': 0.5708781307048031, 'support': 81536}, '1': {'recall': 0.14730392156862746, 'f1-score': 0.16447728516694032, 'precision': 0.18618339529120198, 'support': 4080}, 'weighted avg': {'recall': 0.9251128335949764, 'f1-score': 0.9209522991501708, 'precision': 0.9170731967579377, 'support': 81536}, '0': {'recall': 0.9660839702540798, 'f1-score': 0.960799671297604, 'precision': 0.9555728661184042, 'support': 77456}}
  "macro avg": {
  "macro avg": {
  
  
  
{'0': {'support': 77456, 'f1-score': 0.9571608486453321, 'recall': 0.9566850857260897, 'precision': 0.9576370849972214}, 'accuracy': 0.9186494309262166, 'weighted avg': {'support': 81536, 'f1-score': 0.919009438108974, 'recall': 0.9186494309262166, 'precision': 0.9193715982015276}, 'macro avg': {'support': 81536, 'f1-score': 0.5759459700310551, 'recall': 0.5766268565885351, 'precision': 0.5752823385053464}, '1': {'support': 4080, 'f1-score': 0.19473109141677794, 'recall': 0.1965686274509804, 'precision': 0.19292759201347126}}
  "macro avg": {
  "macro avg": {
  
 
  
{'weighted avg': {'support': 81536, 'f1-score': 0.9164665041318528, 'recall': 0.9127869897959183, 'precision': 0.9203625449068326}, '0': {'support': 77456, 'f1-score': 0.9538573347435905, 'recall': 0.9489129312125594, 'precision': 0.9588535347605442}, '1': {'support': 4080, 'f1-score': 0.20662724534196142, 'recall': 0.2269607843137255, 'precision': 0.1896375179193119}, 'accuracy': 0.9127869897959183, 'macro avg': {'support': 81536, 'f1-score': 0.5802422900427759, 'recall': 0.5879368577631424, 'precision': 0.5742455263399281}}
  "macro avg": {
  "macro avg": {
  
   
  
{'1': {'precision': 0.22994512673112097, 'recall': 0.21568627450980393, 'support': 4080, 'f1-score': 0.22258758062476286}, 'macro avg': {'precision': 0.594382927673427, 'recall': 0.5888194334746912, 'support': 81536, 'f1-score': 0.5914858439327211}, 'accuracy': 0.9246099882260597, '0': {'precision': 0.9588207286157331, 'recall': 0.9619525924395786, 'support': 77456, 'f1-score': 0.9603841072406792}, 'weighted avg': {'precision': 0.9223483427286499, 'recall': 0.9246099882260597, 'support': 81536, 'f1-score': 0.9234653250022454}}
  "macro avg": {
  "macro avg": {
  
 
  
{'weighted avg': {'f1-score': 0.9204940292822316, 'support': 81536, 'recall': 0.9229910714285714, 'precision': 0.918100737968003}, 'accuracy': 0.9229910714285714, '0': {'f1-score': 0.9596031730713556, 'support': 77456, 'recall': 0.9628305102251601, 'precision': 0.9563973992331072}, 'macro avg': {'f1-score': 0.5688184735627756, 'support': 81536, 'recall': 0.5647485884459134, 'precision': 0.5737311525527716}, '1': {'f1-score': 0.17803377405419557, 'support': 4080, 'recall': 0.16666666666666666, 'precision': 0.19106490587243607}}

 [0.5778911758321731, 0.5727065298044567, 0.5760363372121583, 0.5784218478361854, 0.5626384782322722, 0.5759459700310551, 0.5802422900427759, 0.5914858439327211, 0.5688184735627756]
 
 (0.5760207718318415, 0.007514446592634158)

# subchar_segmented, vocab=1321
nohup ./comp_bert/comp_segmented/scripts/run_classifier_nlpcc_dbqa_1321.sh > logs/subchar_segmented_run_classifier_nlpcc_dbqa_1321.log_to_commit &
grep "macro avg" logs/subchar_segmented_run_classifier_nlpcc_dbqa_1321.log_to_commit   (xxx)



{'0': {'recall': 0.9702024375129106, 'f1-score': 0.9639858637299485, 'precision': 0.9578484481549933, 'support': 77
456}, 'macro avg': {'recall': 0.579831610913318, 'f1-score': 0.5899387494882112, 'precision': 0.6043705077516284, '
support': 81536}, '1': {'recall': 0.18946078431372548, 'f1-score': 0.21589163524647395, 'precision': 0.250892567348
26354, 'support': 4080}, 'accuracy': 0.9311347135007849, 'weighted avg': {'recall': 0.9311347135007849, 'f1-score':
 0.926551792249712, 'precision': 0.9224729085934321, 'support': 81536}}
  "macro avg": {
  "macro avg": {
  
  
  
{'0': {'f1-score': 0.9688473520249222, 'support': 77456, 'recall': 0.9837197892997315, 'precision': 0.9544179171781
446}, 'macro avg': {'f1-score': 0.560694862453139, 'support': 81536, 'recall': 0.5459040122969245, 'precision': 0.6
067624250990605}, 'weighted avg': {'f1-score': 0.9280000659806503, 'support': 81536, 'recall': 0.9399038461538461, 
'precision': 0.919625079470073}, '1': {'f1-score': 0.15254237288135594, 'support': 4080, 'recall': 0.10808823529411
765, 'precision': 0.2591069330199765}, 'accuracy': 0.9399038461538461}
  "macro avg": {
  "macro avg": {
  
  
  
{'accuracy': 0.940946330455259, '1': {'recall': 0.15416666666666667, 'f1-score': 0.2071463856413634, 'precision': 0
.3156046161565479, 'support': 4080}, '0': {'recall': 0.9823900020656889, 'f1-score': 0.9693310148472284, 'precision
': 0.9566146612524044, 'support': 77456}, 'macro avg': {'recall': 0.5682783343661778, 'f1-score': 0.588238700244295
9, 'precision': 0.6361096387044761, 'support': 81536}, 'weighted avg': {'recall': 0.940946330455259, 'f1-score': 0.
9311918703324138, 'precision': 0.9245390016175058, 'support': 81536}}
  "macro avg": {
  "macro avg": {
  
  
  
{'accuracy': 0.9370830062794349, '1': {'support': 4080, 'precision': 0.2765957446808511, 'f1-score': 0.202177293934
68117, 'recall': 0.15931372549019607}, 'macro avg': {'support': 81536, 'precision': 0.616640003525231, 'f1-score': 
0.5847137283631348, 'recall': 0.5686828904253294}, '0': {'support': 77456, 'precision': 0.9566842623696108, 'f1-sco
re': 0.9672501627915885, 'recall': 0.9780520553604627}, 'weighted avg': {'support': 81536, 'precision': 0.922653145
41305, 'f1-score': 0.9289664929410171, 'recall': 0.9370830062794349}}
  "macro avg": {
  "macro avg": {
  
  
  
{'weighted avg': {'support': 81536, 'f1-score': 0.9302408517129267, 'recall': 0.9422218406593407, 'precision': 0.92
26713118069126}, 'accuracy': 0.9422218406593407, '1': {'support': 4080, 'f1-score': 0.17423312883435582, 'recall': 
0.12181372549019608, 'precision': 0.3058461538461538}, 'macro avg': {'support': 81536, 'f1-score': 0.57214836905220
3, 'recall': 0.5536253093470398, 'precision': 0.6305043861295692}, '0': {'support': 77456, 'f1-score': 0.9700636092
700502, 'recall': 0.9854368932038835, 'precision': 0.9551626184129844}}
  "macro avg": {
  "macro avg": {
  
  
  
{'accuracy': 0.9353537087912088, '1': {'support': 4080, 'f1-score': 0.18468677494199537, 'recall': 0.14632352941176
47, 'precision': 0.25031446540880503}, 'weighted avg': {'support': 81536, 'f1-score': 0.9272290371425953, 'recall':
 0.9353537087912088, 'precision': 0.9206837549367639}, 'macro avg': {'support': 81536, 'f1-score': 0.57551463779825
01, 'recall': 0.5616197279366197, 'precision': 0.6031549838383111}, '0': {'support': 77456, 'f1-score': 0.966342500
6545047, 'recall': 0.9769159264614748, 'precision': 0.9559955022678173}}
  "macro avg": {
  "macro avg": {
  
  
  
{'macro avg': {'support': 81536, 'f1-score': 0.5868775373026048, 'recall': 0.5735446006537298, 'precision': 0.6093451485711963}, '1': {'support': 4080, 'f1-score': 0.20808736717827625, 'recall': 0.17279411764705882, 'precision': 0.26149851632047477}, '0': {'support': 77456, 'f1-score': 0.9656677074269334, 'recall': 0.9742950836604007, 'precision': 0.9571917808219178}, 'weighted avg': {'support': 81536, 'f1-score': 0.9277589580620574, 'recall': 0.934188579277865, 'precision': 0.9223798140935292}, 'accuracy': 0.934188579277865}
  "macro avg": {
  "macro avg": {
  
  
  
{'1': {'precision': 0.2582972582972583, 'f1-score': 0.17437895762299072, 'recall': 0.13161764705882353, 'support': 4080}, 'accuracy': 0.937634909733124, 'weighted avg': {'precision': 0.9205268558105852, 'f1-score': 0.9279016488804708, 'recall': 0.937634909733124, 'support': 81536}, '0': {'precision': 0.9554098443183106, 'f1-score': 0.967593507230121, 'recall': 0.9800919231563726, 'support': 77456}, 'macro avg': {'precision': 0.6068535513077844, 'f1-score': 0.5709862324265559, 'recall': 0.5558547851075981, 'support': 81536}}
  "macro avg": {
  "macro avg": {
  
 
  
{'accuracy': 0.9372056514913658, 'macro avg': {'f1-score': 0.5770636002878589, 'recall': 0.5615496312137745, 'support': 81536, 'precision': 0.6106593772699717}, '1': {'f1-score': 0.18678526048284622, 'recall': 0.14411764705882352, 'support': 4080, 'precision': 0.26534296028880866}, 'weighted avg': {'f1-score': 0.9282834720197638, 'recall': 0.9372056514913658, 'support': 81536, 'precision': 0.9214170476537263}, '0': {'f1-score': 0.9673419400928714, 'recall'

 [0.5899387494882112,  0.560694862453139, 0.588238700244295, 0.5847137283631348, 0.57214836905220, 0.57551463779825, 0.5868775373026048, 0.5709862324265559, 0.5770636002878589]
 
 (0.5784640463795834, 0.009184937326831255)
 


# subchar_spaced, vocab=21128
nohup ./comp_bert/comp_spaced/scripts/run_classifier_nlpcc_dbqa_21128.sh > logs/subchar_spaced_run_classifier_nlpcc_dbqa_21128.log_to_commit &
grep "macro avg" logs/subchar_spaced_run_classifier_nlpcc_dbqa_21128.log_to_commit   (xxx)

grep "macro avg" logs/subchar_spaced_run_classifier_nlpcc_dbqa_21128.log_to_commit



"macro avg": {
  "macro avg": {
{'macro avg': {'precision': 0.5719765930171501, 'support': 81536, 'recall': 0.5648835417248907, 'f1-score': 0.5681620704476648}, '0': {'precision': 0.9564190143557872, 'support': 77456, 'recall': 0.9616298285478208, 'f1-score': 0.9590173432732049}, '1': {'precision': 0.18753417167851286, 'support': 4080, 'recall': 0.1681372549019608, 'f1-score': 0.17730679762212456}, 'accuracy': 0.9219240580847724, 'weighted avg': {'precision': 0.9179445962076898, 'support': 81536, 'recall': 0.9219240580847724, 'f1-score': 0.919901136612878}}
  "macro avg": {
  "macro avg": {
  
  
  
{'macro avg': {'recall': 0.5621518453487572, 'f1-score': 0.560580568764036, 'support': 81536, 'precision': 0.5591269752930523}, 'weighted avg': {'recall': 0.9143077904238619, 'f1-score': 0.9153763942921803, 'support': 81536, 'precision': 0.9164602833666295}, 'accuracy': 0.9143077904238619, '1': {'recall': 0.17083333333333334, 'f1-score': 0.1663286004056795, 'support': 4080, 'precision': 0.16205533596837945}, '0': {'recall': 0.953470357364181, 'f1-score': 0.9548325371223925, 'support': 77456, 'precision': 0.9561986146177252}}
  "macro avg": {
  "macro avg": {
  
  
  
{'0': {'f1-score': 0.9580871503772479, 'recall': 0.9598869035323281, 'precision': 0.9562941335356991, 'support': 77456}, '1': {'f1-score': 0.17333841657135593, 'recall': 0.16715686274509803, 'precision': 0.17999472156241753, 'support': 4080}, 'weighted avg': {'f1-score': 0.9188189150710269, 'recall': 0.9202192896389325, 'precision': 0.917448695927146, 'support': 81536}, 'accuracy': 0.9202192896389325, 'macro avg': {'f1-score': 0.5657127834743019, 'recall': 0.5635218831387131, 'precision': 0.5681444275490584, 'support': 81536}}
  "macro avg": {
  "macro avg": {
  
  
  
{'0': {'support': 77456, 'precision': 0.954657410125193, 'recall': 0.9657870274736625, 'f1-score': 0.9601899688733434}, '1': {'support': 4080, 'precision': 0.16587976078061065, 'recall': 0.12916666666666668, 'f1-score': 0.14523907950943918}, 'accuracy': 0.9239231750392465, 'weighted avg': {'support': 81536, 'precision': 0.9151875709213335, 'recall': 0.9239231750392465, 'f1-score': 0.9194104404612955}, 'macro avg': {'support': 81536, 'precision': 0.5602685854529018, 'recall': 0.5474768470701646, 'f1-score': 0.5527145241913913}}
  "macro avg": {
  "macro avg": {
  
 
  
{'1': {'support': 4080, 'f1-score': 0.12639894667544435, 'recall': 0.11764705882352941, 'precision': 0.13655761024182078}, 'weighted avg': {'support': 81536, 'f1-score': 0.915745970178866, 'recall': 0.9186249018838305, 'precision': 0.9129614520462516}, 'macro avg': {'support': 81536, 'f1-score': 0.5418619121550392, 'recall': 0.5392317611820601, 'precision': 0.5452080933894534}, 'accuracy': 0.9186249018838305, '0': {'support': 77456, 'f1-score': 0.957324877634634, 'recall': 0.9608164635405908, 'precision': 0.9538585765370862}}
  "macro avg": {
  "macro avg": {
  
   
  
{'macro avg': {'precision': 0.5694780184348956, 'support': 81536, 'recall': 0.5642444692192101, 'f1-score': 0.5667102270112121}, 'weighted avg': {'precision': 0.9176446226356735, 'support': 81536, 'recall': 0.9207098704866562, 'f1-score': 0.9191583991662508}, 'accuracy': 0.9207098704866562, '0': {'precision': 0.9563635428586122, 'support': 77456, 'recall': 0.9603516835364594, 'f1-score': 0.958353464102812}, '1': {'precision': 0.18259249401117914, 'support': 4080, 'recall': 0.1681372549019608, 'f1-score': 0.17506698991961211}}
  "macro avg": {
  "macro avg": {
  
  
  
{'accuracy': 0.9256524725274725, 'weighted avg': {'f1-score': 0.9202857321204371, 'recall': 0.9256524725274725, 'precision': 0.9153443660881854, 'support': 81536}, 'macro avg': {'f1-score': 0.5529443663493183, 'recall': 0.5467617288601043, 'precision': 0.5625609621287, 'support': 81536}, '0': {'f1-score': 0.9611370396963792, 'recall': 0.9677881636025615, 'precision': 0.9545767114914425, 'support': 77456}, '1': {'f1-score': 0.14475169300225732, 'recall': 0.12573529411764706, 'precision': 0.17054521276595744, 'support': 4080}}
  "macro avg": {
  "macro avg": {
  
  
  
{'0': {'support': 77456, 'precision': 0.95618281668879, 'recall': 0.9486030778764718, 'f1-score': 0.9523778662069502}, 'weighted avg': {'support': 81536, 'precision': 0.9159369123138882, 'recall': 0.9098802982731554, 'f1-score': 0.9128542561841824}, 'accuracy': 0.9098802982731554, 'macro avg': {'support': 81536, 'precision': 0.554039427091732, 'recall': 0.5616789899186281, 'f1-score': 0.5574517550774892}, '1': {'support': 4080, 'precision': 0.15189603749467406, 'recall': 0.1747549019607843, 'f1-score': 0.16252564394802826}}
  "macro avg": {
  "macro avg": {
  
  [0.5719765930171501,  0.560580568764036, 0.5657127834743019, 0.5527145241913913, 0.5418619121550392, 0.566710227011212, 0.5529443663493183, 0.5574517550774892, 0.5818751226515607]
  
{'weighted avg': {'support': 81536, 'recall': 0.9225863422291993, 'precision': 0.9205144701053667, 'f1-score': 0.9215401650108556}, 'accuracy': 0.9225863422291993, '1': {'support': 4080, 'recall': 0.19877450980392156, 'precision': 0.2104307213284899, 'f1-score': 0.2044366019662213}, '0': {'support': 77456, 'recall': 0.9607131790952282, 'precision': 0.9579181792435828, 'f1-score': 0.9593136433369001}, 'macro avg': {'support': 81536, 'recall': 0.5797438444495749, 'precision': 0.5841744502860363, 'f1-score': 0.5818751226515607}}


(0.561314205854611, 0.011169201436428905)

# subchar_spaced, vocab=5282
nohup ./comp_bert/comp_spaced/scripts/run_classifier_nlpcc_dbqa_5282.sh > logs/subchar_spaced_run_classifier_nlpcc_dbqa_5282.log_to_commit &
grep "macro avg" logs/subchar_spaced_run_classifier_nlpcc_dbqa_5282.log_to_commit   (xxx)



"macro avg": {
  "macro avg": {
{'macro avg': {'recall': 0.5606643468170164, 'support': 81536, 'precision': 0.5958009865137326, 'f1-score': 0.5729590917274643}, 'weighted avg': {'recall': 0.9335385596546311, 'support': 81536, 'precision': 0.9198735923302171, 'f1-score': 0.926093363428061}, '0': {'recall': 0.9750051642222681, 'support': 77456, 'precision': 0.9559130665924079, 'f1-score': 0.9653647281396406}, '1': {'recall': 0.1463235294117647, 'support': 4080, 'precision': 0.23568890643505724, 'f1-score': 0.18055345531528808}, 'accuracy': 0.9335385596546311}
  "macro avg": {
  "macro avg": {
  
  
  
{'1': {'f1-score': 0.18738216098622187, 'support': 4080, 'recall': 0.15833333333333333, 'precision': 0.2294849023090586}, '0': {'f1-score': 0.9641240387509044, 'support': 77456, 'recall': 0.9719970047510845, 'precision': 0.956377586666836}, 'weighted avg': {'f1-score': 0.9252564604875617, 'support': 81536, 'recall': 0.931281887755102, 'precision': 0.9200044244786035}, 'macro avg': {'f1-score': 0.5757530998685632, 'support': 81536, 'recall': 0.5651651690422089, 'precision': 0.5929312444879473}, 'accuracy': 0.931281887755102}
  "macro avg": {
  "macro avg": {
  
  
  
{'weighted avg': {'support': 81536, 'recall': 0.925713795133438, 'f1-score': 0.9218297888235317, 'precision': 0.918209887194014}, '0': {'support': 77456, 'recall': 0.9661097913654204, 'f1-score': 0.961103012477604, 'precision': 0.9561478604193553}, 'macro avg': {'support': 81536, 'recall': 0.5624666603885926, 'f1-score': 0.5686788012204421, 'precision': 0.5770656808971204}, 'accuracy': 0.925713795133438, '1': {'support': 4080, 'recall': 0.1588235294117647, 'f1-score': 0.17625458996328033, 'precision': 0.19798350137488543}}
  "macro avg": {
  "macro avg": {
  
  
  
{'0': {'precision': 0.959318924645058, 'support': 77456, 'f1-score': 0.959015387794373, 'recall': 0.9587120429663293}, 'macro avg': {'precision': 0.5923986243472323, 'support': 81536, 'f1-score': 0.5929198025584119, 'recall': 0.5934491587380666}, 'weighted avg': {'precision': 0.9225980939637607, 'support': 81536, 'f1-score': 0.9223770933535683, 'recall': 0.9221570839874411}, '1': {'precision': 0.22547832404940663, 'support': 4080, 'f1-score': 0.22682421732245095, 'recall': 0.22818627450980392}, 'accuracy': 0.9221570839874411}
  "macro avg": {
  "macro avg": {
  
  
  
{'1': {'f1-score': 0.18318113670437508, 'precision': 0.20632483880871968, 'recall': 0.16470588235294117, 'support': 4080}, 'accuracy': 0.9264987244897959, '0': {'f1-score': 0.9615179632067294, 'precision': 0.9564634193078604, 'recall': 0.966626213592233, 'support': 77456}, 'macro avg': {'f1-score': 0.5723495499555522, 'precision': 0.58139412905829, 'recall': 0.5656660479725871, 'support': 81536}, 'weighted avg': {'f1-score': 0.922570574910399, 'precision': 0.9189270499932448, 'recall': 0.9264987244897959, 'support': 81536}}

[0.5729590917274643, 0.5757530998685632, 0.5686788012204421, 0.5929198025584119, 0.5723495499555522]

(0.5765320690660867, 0.008498212177321756)


# subchar_spaced, vocab=1321
nohup ./comp_bert/comp_spaced/scripts/run_classifier_nlpcc_dbqa_1321.sh > logs/subchar_spaced_run_classifier_nlpcc_dbqa_1321.log_to_commit &
grep "macro avg" logs/subchar_spaced_run_classifier_nlpcc_dbqa_1321.log_to_commit   (xxx)



  "macro avg": {
  "macro avg": {
{'0': {'f1-score': 0.9660240516142259, 'support': 77456, 'precision': 0.9588426073131956, 'recall': 0.9733138814294567}, '1': {'f1-score': 0.24145329709626662, 'support': 4080, 'precision': 0.2899347303332188, 'recall': 0.2068627450980392}, 'accuracy': 0.9349612441130298, 'weighted avg': {'f1-score': 0.9297670770455291, 'support': 81536, 'precision': 0.9253709611927299, 'recall': 0.9349612441130298}, 'macro avg': {'f1-score': 0.6037386743552462, 'support': 81536, 'precision': 0.6243886688232072, 'recall': 0.590088313263748}}
  "macro avg": {
  "macro avg": {
  
  
  
{'macro avg': {'precision': 0.6286314353307052, 'support': 81536, 'f1-score': 0.6056861479574724, 'recall': 0.5909401061602083}, 'weighted avg': {'precision': 0.9258637631901647, 'support': 81536, 'f1-score': 0.9304255951754148, 'recall': 0.9359178767660911}, '0': {'precision': 0.9589183831658132, 'support': 77456, 'f1-score': 0.9665392275524647, 'recall': 0.9742821731047304}, 'accuracy': 0.9359178767660911, '1': {'precision': 0.29834448749559705, 'support': 4080, 'f1-score': 0.24483306836248012, 'recall': 0.2075980392156863}}
  "macro avg": {
  "macro avg": {
  
  
  
{'0': {'precision': 0.959805427547363, 'recall': 0.9680334641602975, 'support': 77456, 'f1-score': 0.9639018871805419}, 'accuracy': 0.9311224489795918, 'weighted avg': {'precision': 0.9255470690706339, 'recall': 0.9311224489795918, 'support': 81536, 'f1-score': 0.9282188274527199}, '1': {'precision': 0.275175644028103, 'recall': 0.23039215686274508, 'support': 4080, 'f1-score': 0.2508004268943436}, 'macro avg': {'precision': 0.6174905357877329, 'recall': 0.5992128105115213, 'support': 81536, 'f1-score': 0.6073511570374428}}
  "macro avg": {
  "macro avg": {
  
  
  
{'weighted avg': {'precision': 0.9274359741237826, 'support': 81536, 'f1-score': 0.9330801533269938, 'recall': 0.9411302982731554}, '1': {'precision': 0.34140969162995594, 'support': 4080, 'f1-score': 0.2440944881889764, 'recall': 0.18995098039215685}, 'accuracy': 0.9411302982731554, 'macro avg': {'precision': 0.6498573197634552, 'support': 81536, 'f1-score': 0.6067335038410457, 'recall': 0.5853248498325172}, '0': {'precision': 0.9583049478969545, 'support': 77456, 'f1-score': 0.9693725194931152, 'recall': 0.9806987192728776}}
  "macro avg": {
  "macro avg": {
  
  
  
{'accuracy': 0.9339555533751962, '0': {'f1-score': 0.9654747937142967, 'support': 77456, 'precision': 0.958951564629316, 'recall': 0.9720873786407767}, '1': {'f1-score': 0.24144245668404, 'support': 4080, 'precision': 0.2838688307386552, 'recall': 0.21004901960784314}, 'macro avg': {'f1-score': 0.6034586251991684, 'support': 81536, 'precision': 0.6214101976839856, 'recall': 0.5910681991243099}, 'weighted avg': {'f1-score': 0.9292447611509695, 'support': 81536, 'precision': 0.925170933321993, 'recall': 0.9339555533751962}}
  "macro avg": {
  "macro avg": {
  
  
  
{'weighted avg': {'recall': 0.9403453689167975, 'support': 81536, 'f1-score': 0.9310662439452014, 'precision': 0.9245575149515288}, '1': {'recall': 0.15931372549019607, 'support': 4080, 'f1-score': 0.21090201168072678, 'precision': 0.31190019193857965}, 'macro avg': {'recall': 0.5703999943294814, 'support': 81536, 'f1-score': 0.5899514774543028, 'precision': 0.6343647362552487}, '0': {'recall': 0.9814862631687667, 'support': 77456, 'f1-score': 0.9690009432278788, 'precision': 0.9568292805719176}, 'accuracy': 0.9403453689167975}
  "macro avg": {
  "macro avg": {
  
  
  
{'0': {'precision': 0.9586051657700966, 'f1-score': 0.9658335949362223, 'support': 77456, 'recall': 0.9731718653170832}, 'macro avg': {'precision': 0.6213969680038909, 'f1-score': 0.6010608616239181, 'support': 81536, 'recall': 0.5876888738350122}, 'accuracy': 0.9345933084772371, '1': {'precision': 0.28418877023768513, 'f1-score': 0.23628812831161392, 'support': 4080, 'recall': 0.20220588235294118}, 'weighted avg': {'precision': 0.924857877532113, 'f1-score': 0.9293276895223144, 'support': 81536, 'recall': 0.9345933084772371}}
  "macro avg": {
  "macro avg": {
  
  
  
{'0': {'f1-score': 0.9681364413919883, 'support': 77456, 'precision': 0.9574054436196536, 'recall': 0.9791107209254286}, 'accuracy': 0.9387755102040817, 'weighted avg': {'f1-score': 0.9307246365054613, 'support': 81536, 'precision': 0.9246988479503191, 'recall': 0.9387755102040817}, 'macro avg': {'f1-score': 0.5943118184473996, 'support': 81536, 'precision': 0.6305960092452829, 'recall': 0.5760749683058516}, '1': {'f1-score': 0.22048719550281073, 'support': 4080, 'precision': 0.3037865748709122, 'recall': 0.1730392156862745}}
  "macro avg": {
  "macro avg": {
  
  [0.6037386743552462, 0.6056861479574724, 0.6073511570374428, 0.6067335038410457, 0.6034586251991684, 0.5899514774543028, 0.6010608616239181, 0.5943118184473996, 0.5699676394625722]
  
{'macro avg': {'precision': 0.5961289800601652, 'f1-score': 0.5699676394625722, 'recall': 0.5570724023961992, 'support': 81536}, '0': {'precision': 0.9555490993608368, 'f1-score': 0.9659817905530513, 'recall': 0.9766448047923982, 'support': 77456}, '1': {'precision': 0.23670886075949368, 'f1-score': 0.17395348837209304, 'recall': 0.1375, 'support': 4080}, 'accuracy': 0.9346546310832025, 'weighted avg': {'precision': 0.9195788754904791, 'f1-score': 0.926349291130731, 'recall': 0.9346546310832025, 'support': 81536}}
  "macro avg": {
  "macro avg": {
  
  [0.6037386743552462, 0.6056861479574724, 0.6073511570374428, 0.6067335038410457, 0.6034586251991684, 0.5899514774543028, 0.6010608616239181, 0.5943118184473996, 0.5699676394625722, 0.5783432950922367]
  
{'macro avg': {'precision': 0.6343227734320535, 'support': 81536, 'recall': 0.5588494264675504, 'f1-score': 0.5783432950922367}, 'accuracy': 0.942001079277865, 'weighted avg': {'precision': 0.9235165757242455, 'support': 81536, 'recall': 0.942001079277865, 'f1-score': 0.9307389788841129}, '1': {'precision': 0.31296829971181556, 'support': 4080, 'recall': 0.13308823529411765, 'f1-score': 0.18675838349097162}, '0': {'precision': 0.9556772471522913, 'support': 77456, 'recall': 0.9846106176409832, 'f1-score': 0.9699282066935018}}


(0.5960603200470805, 0.012279454565546266)


```


### on book_review

```bash

# subchar_segmented, vocab=21128
nohup ./comp_bert/comp_segmented/scripts/run_classifier_book_review_21128.sh > logs/subchar_segmented_run_classifier_book_review_21128.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_book_review_21128.log_to_commit  (xxx)

INFO:tensorflow:accuracy: 0.778700
I0819 08:36:25.765766 139795317909248 run_classifier.py:535] accuracy: 0.778700
INFO:tensorflow:accuracy: 0.774700
I0819 09:07:37.368498 140198866642688 run_classifier.py:535] accuracy: 0.774700
INFO:tensorflow:accuracy: 0.773900
I0819 09:46:38.628833 140583309432576 run_classifier.py:535] accuracy: 0.773900
INFO:tensorflow:accuracy: 0.776900
I0819 10:25:36.668711 140449618532096 run_classifier.py:535] accuracy: 0.776900
INFO:tensorflow:accuracy: 0.776100
I0819 11:04:35.416110 140345984382720 run_classifier.py:535] accuracy: 0.776100
INFO:tensorflow:accuracy: 0.776800
I0819 11:43:35.497005 140140729997056 run_classifier.py:535] accuracy: 0.776800
INFO:tensorflow:accuracy: 0.776600
I0819 12:22:35.543556 139816330237696 run_classifier.py:535] accuracy: 0.776600
INFO:tensorflow:accuracy: 0.777400
I0819 13:01:34.587368 139992739190528 run_classifier.py:535] accuracy: 0.777400

(0.7763875, 0.0014128318194321387)

# subchar_segmented, vocab=5282
nohup ./comp_bert/comp_segmented/scripts/run_classifier_book_review_5282.sh > logs/subchar_segmented_run_classifier_book_review_5282.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_book_review_5282.log_to_commit   (xxx)

INFO:tensorflow:accuracy: 0.753100
I0819 08:38:16.370702 140636674483968 run_classifier.py:535] accuracy: 0.753100
INFO:tensorflow:accuracy: 0.766600
I0819 09:08:54.722966 140667222243072 run_classifier.py:535] accuracy: 0.766600
INFO:tensorflow:accuracy: 0.768900
I0819 09:47:54.945497 140177811412736 run_classifier.py:535] accuracy: 0.768900
INFO:tensorflow:accuracy: 0.768700
I0819 10:26:53.704057 139964209186560 run_classifier.py:535] accuracy: 0.768700
INFO:tensorflow:accuracy: 0.771200
I0819 11:05:53.742986 139953644545792 run_classifier.py:535] accuracy: 0.771200
INFO:tensorflow:accuracy: 0.765500
I0819 11:44:53.641887 139771301263104 run_classifier.py:535] accuracy: 0.765500
INFO:tensorflow:accuracy: 0.774400
I0819 12:23:53.233848 139861045585664 run_classifier.py:535] accuracy: 0.774400
INFO:tensorflow:accuracy: 0.765200
I0819 13:02:53.913831 139664180242176 run_classifier.py:535] accuracy: 0.765200

# subchar_segmented, vocab=1321
nohup ./comp_bert/comp_segmented/scripts/run_classifier_book_review_1321.sh > logs/subchar_segmented_run_classifier_book_review_1321.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_book_review_1321.log_to_commit   (xxx)

INFO:tensorflow:accuracy: 0.756700
I0819 09:12:25.273187 140329132451584 run_classifier.py:535] accuracy: 0.756700
INFO:tensorflow:accuracy: 0.755200
I0819 10:08:41.018355 140369005037312 run_classifier.py:535] accuracy: 0.755200
INFO:tensorflow:accuracy: 0.759600
I0819 11:03:21.991717 140256343176960 run_classifier.py:535] accuracy: 0.759600
INFO:tensorflow:accuracy: 0.764800
I0819 11:55:25.119588 140569750353664 run_classifier.py:535] accuracy: 0.764800
INFO:tensorflow:accuracy: 0.760000
I0819 12:47:45.281965 139980965754624 run_classifier.py:535] accuracy: 0.760000


# subchar_spaced, vocab=21128
nohup ./comp_bert/comp_spaced/scripts/run_classifier_book_review_21128.sh > logs/subchar_spaced_run_classifier_book_review_21128.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_book_review_21128.log_to_commit  (xxx)

INFO:tensorflow:accuracy: 0.776800
I0824 04:26:07.696024 139783044851456 run_classifier.py:535] accuracy: 0.776800
INFO:tensorflow:accuracy: 0.777700
I0824 05:20:20.578330 140582267516672 run_classifier.py:535] accuracy: 0.777700
INFO:tensorflow:accuracy: 0.779000
I0824 06:12:45.667360 140707224225536 run_classifier.py:535] accuracy: 0.779000
INFO:tensorflow:accuracy: 0.776400
I0824 07:08:08.512165 140323467228928 run_classifier.py:535] accuracy: 0.776400
INFO:tensorflow:accuracy: 0.782200
I0824 08:03:03.548662 139788124034816 run_classifier.py:535] accuracy: 0.782200
INFO:tensorflow:accuracy: 0.780300
I0824 08:56:03.921288 139939171956480 run_classifier.py:535] accuracy: 0.780300
INFO:tensorflow:accuracy: 0.779100
I0824 09:49:47.177220 140583759783680 run_classifier.py:535] accuracy: 0.779100
INFO:tensorflow:accuracy: 0.770600
I0824 10:41:41.800814 140157610534656 run_classifier.py:535] accuracy: 0.770600
INFO:tensorflow:accuracy: 0.777100
I0824 11:33:02.769069 139702891783936 run_classifier.py:535] accuracy: 0.777100
INFO:tensorflow:accuracy: 0.770700
I0824 12:25:19.732561 140363246352128 run_classifier.py:535] accuracy: 0.770700

(0.7769900000000001, 0.003576157155383416)

# subchar_spaced, vocab=5282
nohup ./comp_bert/comp_spaced/scripts/run_classifier_book_review_5282.sh > logs/subchar_spaced_run_classifier_book_review_5282.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_book_review_5282.log_to_commit  (xxx)

INFO:tensorflow:accuracy: 0.773300
I0825 01:22:29.583366 140612151469824 run_classifier.py:535] accuracy: 0.773300
INFO:tensorflow:accuracy: 0.767100
I0825 01:41:10.461426 140508159026944 run_classifier.py:535] accuracy: 0.767100



# subchar_spaced, vocab=1321
nohup ./comp_bert/comp_spaced/scripts/run_classifier_book_review_1321.sh > logs/subchar_spaced_run_classifier_book_review_1321.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_book_review_1321.log_to_commit  (xxx)

INFO:tensorflow:accuracy: 0.756500
I0824 05:24:41.084658 140307435304704 run_classifier.py:535] accuracy: 0.756500
INFO:tensorflow:accuracy: 0.753900
I0824 06:17:32.548522 139792670217984 run_classifier.py:535] accuracy: 0.753900
INFO:tensorflow:accuracy: 0.753100
I0824 07:14:04.227120 140004215539456 run_classifier.py:535] accuracy: 0.753100
INFO:tensorflow:accuracy: 0.739500
I0824 08:06:17.996259 139829832328960 run_classifier.py:535] accuracy: 0.739500
INFO:tensorflow:accuracy: 0.761700
I0824 08:57:50.443545 140174145763072 run_classifier.py:535] accuracy: 0.761700
INFO:tensorflow:accuracy: 0.762700
I0824 09:50:11.701448 140473983362816 run_classifier.py:535] accuracy: 0.762700
INFO:tensorflow:accuracy: 0.757900
I0824 10:41:25.541016 139883746354944 run_classifier.py:535] accuracy: 0.757900
INFO:tensorflow:accuracy: 0.760900
I0824 11:32:26.891453 139693125285632 run_classifier.py:535] accuracy: 0.760900
INFO:tensorflow:accuracy: 0.750100
I0824 12:23:31.680656 140619180754688 run_classifier.py:535] accuracy: 0.750100
INFO:tensorflow:accuracy: 0.755100
I0824 13:14:25.385532 140562818131712 run_classifier.py:535] accuracy: 0.755100

(0.75514, 0.00646949)

```


### on shopping

```bash

# subchar_segmented, vocab=21128
nohup ./comp_bert/comp_segmented/scripts/run_classifier_shopping_21128.sh > logs/subchar_segmented_run_classifier_shopping_21128.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_shopping_21128.log_to_commit  (xxx)

INFO:tensorflow:accuracy: 0.912400
I0820 02:25:04.618901 139912098735872 run_classifier.py:535] accuracy: 0.912400
INFO:tensorflow:accuracy: 0.920200
I0820 02:55:39.715814 139944333858560 run_classifier.py:535] accuracy: 0.920200
INFO:tensorflow:accuracy: 0.916600
I0820 03:34:40.341461 139994722330368 run_classifier.py:535] accuracy: 0.916600
INFO:tensorflow:accuracy: 0.915000
I0820 04:13:39.466413 139753653319424 run_classifier.py:535] accuracy: 0.915000
INFO:tensorflow:accuracy: 0.919700
I0820 04:52:39.422994 140609540830976 run_classifier.py:535] accuracy: 0.919700
INFO:tensorflow:accuracy: 0.920900
I0820 05:31:39.778007 139788722042624 run_classifier.py:535] accuracy: 0.920900
INFO:tensorflow:accuracy: 0.923600
I0820 06:10:39.579704 139736687716096 run_classifier.py:535] accuracy: 0.923600
INFO:tensorflow:accuracy: 0.921700
I0820 06:49:40.086746 140669703493376 run_classifier.py:535] accuracy: 0.921700
INFO:tensorflow:accuracy: 0.919100
I0820 07:25:03.448951 140718598129408 run_classifier.py:535] accuracy: 0.919100
INFO:tensorflow:accuracy: 0.921600
I0820 07:43:21.772058 140045312673536 run_classifier.py:535] accuracy: 0.921600

(0.9190800000000001, 0.0032560098279949905)


# subchar_segmented, vocab=5282
nohup ./comp_bert/comp_segmented/scripts/run_classifier_shopping_5282.sh > logs/subchar_segmented_run_classifier_shopping_5282.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_shopping_5282.log_to_commit  (xxx)

INFO:tensorflow:accuracy: 0.917700
I0820 02:27:40.572716 139982704883456 run_classifier.py:535] accuracy: 0.917700
INFO:tensorflow:accuracy: 0.916400
I0820 02:58:25.310672 139915007043328 run_classifier.py:535] accuracy: 0.916400
INFO:tensorflow:accuracy: 0.918900
I0820 03:37:24.647228 140226429212416 run_classifier.py:535] accuracy: 0.918900
INFO:tensorflow:accuracy: 0.923900
I0820 04:16:25.529235 139857863997184 run_classifier.py:535] accuracy: 0.923900
INFO:tensorflow:accuracy: 0.921900
I0820 04:55:25.154970 139890384185088 run_classifier.py:535] accuracy: 0.921900
INFO:tensorflow:accuracy: 0.914200
I0820 05:34:25.014908 140564389734144 run_classifier.py:535] accuracy: 0.914200
INFO:tensorflow:accuracy: 0.913900
I0820 06:13:25.333926 139735674771200 run_classifier.py:535] accuracy: 0.913900
INFO:tensorflow:accuracy: 0.913400
I0820 06:41:50.097838 140133308872448 run_classifier.py:535] accuracy: 0.913400
INFO:tensorflow:accuracy: 0.913500
I0820 07:03:31.192242 140264988735232 run_classifier.py:535] accuracy: 0.913500
INFO:tensorflow:accuracy: 0.911800
I0820 07:42:31.132653 140202982975232 run_classifier.py:535] accuracy: 0.911800

# subchar_segmented, vocab=1321
nohup ./comp_bert/comp_segmented/scripts/run_classifier_shopping_1321.sh > logs/subchar_segmented_run_classifier_shopping_1321.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_shopping_1321.log_to_commit  (xxx)

INFO:tensorflow:accuracy: 0.905700
I0820 02:27:50.024807 140027375015680 run_classifier.py:535] accuracy: 0.905700
INFO:tensorflow:accuracy: 0.895800
I0820 02:59:15.238819 140376563144448 run_classifier.py:535] accuracy: 0.895800
INFO:tensorflow:accuracy: 0.909600
I0820 03:21:04.851376 139712233502464 run_classifier.py:535] accuracy: 0.909600
INFO:tensorflow:accuracy: 0.904600
I0820 03:49:14.066069 139816383538944 run_classifier.py:535] accuracy: 0.904600
INFO:tensorflow:accuracy: 0.906400
I0820 04:28:14.235481 140555484997376 run_classifier.py:535] accuracy: 0.906400
INFO:tensorflow:accuracy: 0.905000
I0820 05:07:14.614424 139900158891776 run_classifier.py:535] accuracy: 0.905000
INFO:tensorflow:accuracy: 0.903600
I0820 05:46:15.259264 140560931505920 run_classifier.py:535] accuracy: 0.903600
INFO:tensorflow:accuracy: 0.899400
I0820 06:25:14.639013 140257157019392 run_classifier.py:535] accuracy: 0.899400
INFO:tensorflow:accuracy: 0.897800
I0820 07:04:16.198919 140100947990272 run_classifier.py:535] accuracy: 0.897800
INFO:tensorflow:accuracy: 0.912000
I0820 07:43:14.841886 140377604491008 run_classifier.py:535] accuracy: 0.912000


# subchar_spaced, vocab=21128
nohup ./comp_bert/comp_spaced/scripts/run_classifier_shopping_21128.sh > logs/subchar_spaced_run_classifier_shopping_21128.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_shopping_21128.log_to_commit  (xxx)

INFO:tensorflow:accuracy: 0.915000
I0823 09:43:44.660551 140694917310208 run_classifier.py:535] accuracy: 0.915000
INFO:tensorflow:accuracy: 0.919400
I0823 10:03:36.379704 140636686247680 run_classifier.py:535] accuracy: 0.919400
INFO:tensorflow:accuracy: 0.919400
I0823 10:42:36.797063 139959764932352 run_classifier.py:535] accuracy: 0.919400
INFO:tensorflow:accuracy: 0.917700
I0823 11:21:40.050426 140610786297600 run_classifier.py:535] accuracy: 0.917700
INFO:tensorflow:accuracy: 0.914100
I0823 12:00:36.612797 140325430535936 run_classifier.py:535] accuracy: 0.914100
INFO:tensorflow:accuracy: 0.918600
I0823 12:39:36.387808 139905736660736 run_classifier.py:535] accuracy: 0.918600
INFO:tensorflow:accuracy: 0.918100
I0823 13:18:36.049896 140588659488512 run_classifier.py:535] accuracy: 0.918100
INFO:tensorflow:accuracy: 0.919900
I0823 13:57:36.494869 140446870406912 run_classifier.py:535] accuracy: 0.919900
INFO:tensorflow:accuracy: 0.922000
I0823 14:36:37.068696 139816544700160 run_classifier.py:535] accuracy: 0.922000
INFO:tensorflow:accuracy: 0.913500
I0823 15:15:36.084255 139826958026496 run_classifier.py:535] accuracy: 0.913500


# subchar_spaced, vocab=5282
nohup ./comp_bert/comp_spaced/scripts/run_classifier_shopping_5282.sh > logs/subchar_spaced_run_classifier_shopping_5282.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_shopping_5282.log_to_commit  (xxx)

INFO:tensorflow:accuracy: 0.912900
I0823 09:45:39.398215 139733299947264 run_classifier.py:535] accuracy: 0.912900
INFO:tensorflow:accuracy: 0.917800
I0823 10:05:27.464494 140037159024384 run_classifier.py:535] accuracy: 0.917800
INFO:tensorflow:accuracy: 0.904500
I0823 10:44:27.844861 139648924260096 run_classifier.py:535] accuracy: 0.904500
INFO:tensorflow:accuracy: 0.916200
I0823 11:23:27.769538 140534447130368 run_classifier.py:535] accuracy: 0.916200
INFO:tensorflow:accuracy: 0.913900
I0823 12:02:27.156876 140445216982784 run_classifier.py:535] accuracy: 0.913900
INFO:tensorflow:accuracy: 0.921400
I0823 12:41:27.992531 139665353484032 run_classifier.py:535] accuracy: 0.921400
INFO:tensorflow:accuracy: 0.914500
I0823 13:20:27.769847 139699376576256 run_classifier.py:535] accuracy: 0.914500
INFO:tensorflow:accuracy: 0.904300
I0823 13:59:27.807020 139768535672576 run_classifier.py:535] accuracy: 0.904300
INFO:tensorflow:accuracy: 0.911000
I0823 14:38:27.399888 139902566295296 run_classifier.py:535] accuracy: 0.911000
INFO:tensorflow:accuracy: 0.919000
I0823 15:17:28.103018 139830313056000 run_classifier.py:535] accuracy: 0.919000

# subchar_spaced, vocab=1321
nohup ./comp_bert/comp_spaced/scripts/run_classifier_shopping_1321.sh > logs/subchar_spaced_run_classifier_shopping_1321.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_shopping_1321.log_to_commit  (xxx)

INFO:tensorflow:accuracy: 0.910700
I0823 09:45:47.086561 140501823321856 run_classifier.py:535] accuracy: 0.910700
INFO:tensorflow:accuracy: 0.905700
I0823 10:05:34.235178 140251116013312 run_classifier.py:535] accuracy: 0.905700
INFO:tensorflow:accuracy: 0.911200
I0823 10:44:34.985703 140496126592768 run_classifier.py:535] accuracy: 0.911200
INFO:tensorflow:accuracy: 0.900300
I0823 11:23:34.369838 140062659729152 run_classifier.py:535] accuracy: 0.900300
INFO:tensorflow:accuracy: 0.912900
I0823 12:02:34.304106 139666662786816 run_classifier.py:535] accuracy: 0.912900
INFO:tensorflow:accuracy: 0.907300
I0823 12:41:34.429946 139882043459328 run_classifier.py:535] accuracy: 0.907300
INFO:tensorflow:accuracy: 0.908400
I0823 13:20:34.270812 140426243393280 run_classifier.py:535] accuracy: 0.908400
INFO:tensorflow:accuracy: 0.903800
I0823 13:59:34.864184 139973051197184 run_classifier.py:535] accuracy: 0.903800
INFO:tensorflow:accuracy: 0.911100
I0823 14:38:34.164508 140454790334208 run_classifier.py:535] accuracy: 0.911100
INFO:tensorflow:accuracy: 0.912000
I0823 15:17:34.177029 139736601782016 run_classifier.py:535] accuracy: 0.912000

```


### on weibo

```bash

# subchar_segmented, vocab=21128
nohup ./comp_bert/comp_segmented/scripts/run_classifier_weibo_21128.sh > logs/subchar_segmented_run_classifier_weibo_21128.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_weibo_21128.log_to_commit  (xxx)

INFO:tensorflow:accuracy: 0.971500
I0820 12:41:59.721886 140079076329216 run_classifier.py:535] accuracy: 0.971500
INFO:tensorflow:accuracy: 0.970400
I0820 13:12:09.834496 139744268957440 run_classifier.py:535] accuracy: 0.970400

# subchar_segmented, vocab=5282
nohup ./comp_bert/comp_segmented/scripts/run_classifier_weibo_5282.sh > logs/subchar_segmented_run_classifier_weibo_5282.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_weibo_5282.log_to_commit  (xxx)

INFO:tensorflow:accuracy: 0.970300
I0820 12:47:09.871517 140299135575808 run_classifier.py:535] accuracy: 0.970300
INFO:tensorflow:accuracy: 0.968300
I0820 13:15:32.926744 140225591154432 run_classifier.py:535] accuracy: 0.968300
INFO:tensorflow:accuracy: 0.967600
I0820 13:54:36.577291 140321270732544 run_classifier.py:535] accuracy: 0.967600
INFO:tensorflow:accuracy: 0.971200
I0820 14:33:36.064100 140715693545216 run_classifier.py:535] accuracy: 0.971200
INFO:tensorflow:accuracy: 0.967800
I0820 15:12:34.021783 140314328200960 run_classifier.py:535] accuracy: 0.967800
INFO:tensorflow:accuracy: 0.971300
I0820 15:51:33.202008 140247005366016 run_classifier.py:535] accuracy: 0.971300
INFO:tensorflow:accuracy: 0.969000
I0820 16:30:33.747640 140285520774912 run_classifier.py:535] accuracy: 0.969000
INFO:tensorflow:accuracy: 0.970500
I0820 17:09:32.701941 140446576252672 run_classifier.py:535] accuracy: 0.970500
INFO:tensorflow:accuracy: 0.971000
I0820 17:48:32.725283 139909746218752 run_classifier.py:535] accuracy: 0.971000
INFO:tensorflow:accuracy: 0.966300
I0820 18:27:32.995300 140350964094720 run_classifier.py:535] accuracy: 0.966300

# subchar_segmented, vocab=1321
nohup ./comp_bert/comp_segmented/scripts/run_classifier_weibo_1321.sh > logs/subchar_segmented_run_classifier_weibo_1321.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_weibo_1321.log_to_commit  (xxx)

INFO:tensorflow:accuracy: 0.968400
I0820 12:56:49.567634 139820280452864 run_classifier.py:535] accuracy: 0.968400
INFO:tensorflow:accuracy: 0.956500
I0820 13:22:27.376910 140415245268736 run_classifier.py:535] accuracy: 0.956500
INFO:tensorflow:accuracy: 0.953500
I0820 14:01:30.783882 140139550045952 run_classifier.py:535] accuracy: 0.953500
INFO:tensorflow:accuracy: 0.957000
I0820 14:40:28.312928 140572168353536 run_classifier.py:535] accuracy: 0.957000
INFO:tensorflow:accuracy: 0.966500
I0820 15:19:27.499963 140417739282176 run_classifier.py:535] accuracy: 0.966500
INFO:tensorflow:accuracy: 0.963900
I0820 15:58:27.072713 140493914638080 run_classifier.py:535] accuracy: 0.963900
INFO:tensorflow:accuracy: 0.953800
I0820 16:37:27.155388 139809801832192 run_classifier.py:535] accuracy: 0.953800
INFO:tensorflow:accuracy: 0.952200
I0820 17:16:27.730049 140501902939904 run_classifier.py:535] accuracy: 0.952200
INFO:tensorflow:accuracy: 0.967000
I0820 17:55:27.336361 139687667189504 run_classifier.py:535] accuracy: 0.967000
INFO:tensorflow:accuracy: 0.964100
I0820 18:34:27.687292 140652904675072 run_classifier.py:535] accuracy: 0.964100


# subchar_spaced, vocab=21128
nohup ./comp_bert/comp_spaced/scripts/run_classifier_weibo_21128.sh > logs/subchar_spaced_run_classifier_weibo_21128.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_weibo_21128.log_to_commit  (xxx)

INFO:tensorflow:accuracy: 0.962600
I0824 02:35:58.027402 140195388303104 run_classifier.py:535] accuracy: 0.962600
INFO:tensorflow:accuracy: 0.970800
I0824 03:03:42.340783 140224955021056 run_classifier.py:535] accuracy: 0.970800
INFO:tensorflow:accuracy: 0.970000
I0824 03:38:12.591933 139660975089408 run_classifier.py:535] accuracy: 0.970000
INFO:tensorflow:accuracy: 0.962500
I0824 04:17:12.561796 140535427401472 run_classifier.py:535] accuracy: 0.962500
INFO:tensorflow:accuracy: 0.966900
I0824 04:56:13.909105 140059635640064 run_classifier.py:535] accuracy: 0.966900
INFO:tensorflow:accuracy: 0.970400
I0824 05:35:17.175061 140339461580544 run_classifier.py:535] accuracy: 0.970400
INFO:tensorflow:accuracy: 0.970100
I0824 06:14:16.519480 139866322728704 run_classifier.py:535] accuracy: 0.970100
INFO:tensorflow:accuracy: 0.968900
I0824 06:53:16.999149 140089528047360 run_classifier.py:535] accuracy: 0.968900
INFO:tensorflow:accuracy: 0.970400
I0824 07:32:17.192048 140709748565760 run_classifier.py:535] accuracy: 0.970400
INFO:tensorflow:accuracy: 0.961900
I0824 08:11:16.980093 139667084683008 run_classifier.py:535] accuracy: 0.961900

(0.9674500000000001, 0.003512620104708165)

# subchar_spaced, vocab=5282
nohup ./comp_bert/comp_spaced/scripts/run_classifier_weibo_5282.sh > logs/subchar_spaced_run_classifier_weibo_5282.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_weibo_5282.log_to_commit  (xxx)

INFO:tensorflow:accuracy: 0.968800
I0824 02:36:16.326043 139799218439936 run_classifier.py:535] accuracy: 0.968800
INFO:tensorflow:accuracy: 0.967500
I0824 03:05:10.622779 139763603302144 run_classifier.py:535] accuracy: 0.967500
INFO:tensorflow:accuracy: 0.962300
I0824 03:44:11.271738 140519512569600 run_classifier.py:535] accuracy: 0.962300
INFO:tensorflow:accuracy: 0.966400
I0824 04:23:10.779309 140689639261952 run_classifier.py:535] accuracy: 0.966400
INFO:tensorflow:accuracy: 0.967200
I0824 05:02:10.974750 140462695368448 run_classifier.py:535] accuracy: 0.967200
INFO:tensorflow:accuracy: 0.969000
I0824 05:41:15.742356 139778956207872 run_classifier.py:535] accuracy: 0.969000
INFO:tensorflow:accuracy: 0.966300
I0824 06:20:32.622110 140536067188480 run_classifier.py:535] accuracy: 0.966300
INFO:tensorflow:accuracy: 0.965200
I0824 06:59:15.079433 139847014250240 run_classifier.py:535] accuracy: 0.965200
INFO:tensorflow:accuracy: 0.966400
I0824 07:38:16.605597 139804722988800 run_classifier.py:535] accuracy: 0.966400
INFO:tensorflow:accuracy: 0.964200
I0824 08:17:13.856602 140414374565632 run_classifier.py:535] accuracy: 0.964200

(0.9663299999999999, 0.0019344508264621202)

# subchar_spaced, vocab=1321
nohup ./comp_bert/comp_spaced/scripts/run_classifier_weibo_1321.sh > logs/subchar_spaced_run_classifier_weibo_1321.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_weibo_1321.log_to_commit  (xxx)

INFO:tensorflow:accuracy: 0.967900
I0824 02:36:18.588708 140463905359616 run_classifier.py:535] accuracy: 0.967900
INFO:tensorflow:accuracy: 0.967700
I0824 03:05:59.050737 139875778615040 run_classifier.py:535] accuracy: 0.967700
INFO:tensorflow:accuracy: 0.968000
I0824 03:44:59.409863 140148371994368 run_classifier.py:535] accuracy: 0.968000
INFO:tensorflow:accuracy: 0.968600
I0824 04:23:59.424409 139701967210240 run_classifier.py:535] accuracy: 0.968600
INFO:tensorflow:accuracy: 0.955100
I0824 05:02:59.346051 140252305463040 run_classifier.py:535] accuracy: 0.955100
INFO:tensorflow:accuracy: 0.968300
I0824 05:42:03.452257 140658393515776 run_classifier.py:535] accuracy: 0.968300
INFO:tensorflow:accuracy: 0.968200
I0824 06:21:04.574935 140292026418944 run_classifier.py:535] accuracy: 0.968200
INFO:tensorflow:accuracy: 0.967500
I0824 07:00:04.383669 140560709388032 run_classifier.py:535] accuracy: 0.967500
INFO:tensorflow:accuracy: 0.968600
I0824 07:39:03.613559 140391449863936 run_classifier.py:535] accuracy: 0.968600
INFO:tensorflow:accuracy: 0.970900
I0824 08:18:02.301079 140184146274048 run_classifier.py:535] accuracy: 0.970900



```

### law_qa

```bash

# subchar_segmented, vocab=21128
nohup ./comp_bert/comp_segmented/scripts/run_classifier_law_qa_21128.sh > logs/subchar_segmented_run_classifier_law_qa_21128.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_law_qa_21128.log_to_commit  (xxx)

INFO:tensorflow:accuracy: 0.851005
I0824 03:50:10.788068 140575282718464 run_classifier.py:535] accuracy: 0.851005
INFO:tensorflow:accuracy: 0.849628
I0824 04:25:28.181960 140479162156800 run_classifier.py:535] accuracy: 0.849628
INFO:tensorflow:accuracy: 0.848251
I0824 05:03:23.005941 139851123791616 run_classifier.py:535] accuracy: 0.848251
INFO:tensorflow:accuracy: 0.853484
I0824 05:41:27.387265 140490922399488 run_classifier.py:535] accuracy: 0.853484
INFO:tensorflow:accuracy: 0.844671
I0824 06:21:49.154493 140365538428672 run_classifier.py:535] accuracy: 0.844671
INFO:tensorflow:accuracy: 0.852933
I0824 07:00:57.317213 139911868991232 run_classifier.py:535] accuracy: 0.852933
INFO:tensorflow:accuracy: 0.853759
I0824 07:40:17.516252 140229300692736 run_classifier.py:535] accuracy: 0.853759
INFO:tensorflow:accuracy: 0.847425
I0824 08:18:12.005956 140232269498112 run_classifier.py:535] accuracy: 0.847425
INFO:tensorflow:accuracy: 0.852107
I0824 08:52:52.570018 140086904547072 run_classifier.py:535] accuracy: 0.852107
INFO:tensorflow:accuracy: 0.852107
I0824 09:28:50.568727 140045284685568 run_classifier.py:535] accuracy: 0.852107

(0.8505369999999999, 0.002830235149241156)

# subchar_segmented, vocab=5282
nohup ./comp_bert/comp_segmented/scripts/run_classifier_law_qa_5282.sh > logs/subchar_segmented_run_classifier_law_qa_5282.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_law_qa_5282.log_to_commit  (xxx)

INFO:tensorflow:accuracy: 0.852933
I0824 03:41:13.159695 140679532623616 run_classifier.py:535] accuracy: 0.852933
INFO:tensorflow:accuracy: 0.853759
I0824 04:14:37.659148 140278181656320 run_classifier.py:535] accuracy: 0.853759
INFO:tensorflow:accuracy: 0.854586
I0824 04:53:37.837896 140675283642112 run_classifier.py:535] accuracy: 0.854586
INFO:tensorflow:accuracy: 0.854310
I0824 05:32:38.145728 139832719177472 run_classifier.py:535] accuracy: 0.854310
INFO:tensorflow:accuracy: 0.855687
I0824 06:11:38.898446 139957930153728 run_classifier.py:535] accuracy: 0.855687
INFO:tensorflow:accuracy: 0.856238
I0824 06:50:38.470463 139885313967872 run_classifier.py:535] accuracy: 0.856238
INFO:tensorflow:accuracy: 0.855687
I0824 07:29:38.330944 139674427508480 run_classifier.py:535] accuracy: 0.855687
INFO:tensorflow:accuracy: 0.859818
I0824 08:08:37.583536 139823044036352 run_classifier.py:535] accuracy: 0.859818
INFO:tensorflow:accuracy: 0.851281
I0824 08:47:37.570137 140543207728896 run_classifier.py:535] accuracy: 0.851281
INFO:tensorflow:accuracy: 0.858717
I0824 09:26:39.191721 140125269776128 run_classifier.py:535] accuracy: 0.858717

(0.8553016, 0.002426668423992027)

# subchar_segmented, vocab=1321
nohup ./comp_bert/comp_segmented/scripts/run_classifier_law_qa_1321.sh > logs/subchar_segmented_run_classifier_law_qa_1321.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_law_qa_1321.log_to_commit  (xxx)

INFO:tensorflow:accuracy: 0.858717
I0824 03:41:49.181958 139818489734912 run_classifier.py:535] accuracy: 0.858717
INFO:tensorflow:accuracy: 0.858166
I0824 04:15:07.696575 140464617719552 run_classifier.py:535] accuracy: 0.858166
INFO:tensorflow:accuracy: 0.855963
I0824 04:54:08.252393 140556379911936 run_classifier.py:535] accuracy: 0.855963
INFO:tensorflow:accuracy: 0.858166
I0824 05:33:09.517764 140062513235712 run_classifier.py:535] accuracy: 0.858166
INFO:tensorflow:accuracy: 0.851281
I0824 06:12:09.699786 140193502607104 run_classifier.py:535] accuracy: 0.851281
INFO:tensorflow:accuracy: 0.853759
I0824 06:51:09.611519 140419933034240 run_classifier.py:535] accuracy: 0.853759
INFO:tensorflow:accuracy: 0.853759
I0824 07:30:09.063567 139896045573888 run_classifier.py:535] accuracy: 0.853759
INFO:tensorflow:accuracy: 0.857890
I0824 08:09:08.858231 140344516654848 run_classifier.py:535] accuracy: 0.857890
INFO:tensorflow:accuracy: 0.860369
I0824 08:48:08.988418 140448570468096 run_classifier.py:535] accuracy: 0.860369
INFO:tensorflow:accuracy: 0.855412
I0824 09:27:08.664713 140715401914112 run_classifier.py:535] accuracy: 0.855412


# subchar_spaced, vocab=21128
nohup ./comp_bert/comp_spaced/scripts/run_classifier_law_qa_21128.sh > logs/subchar_spaced_run_classifier_law_qa_21128.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_law_qa_21128.log_to_commit  (xxx)

INFO:tensorflow:accuracy: 0.856789
I0821 07:49:58.708060 140278428358400 run_classifier.py:535] accuracy: 0.856789
INFO:tensorflow:accuracy: 0.857064
I0821 08:18:21.502461 140525894346496 run_classifier.py:535] accuracy: 0.857064
INFO:tensorflow:accuracy: 0.856238
I0821 08:57:20.761123 139715227444992 run_classifier.py:535] accuracy: 0.856238
INFO:tensorflow:accuracy: 0.854586
I0821 09:36:21.562232 140251783100160 run_classifier.py:535] accuracy: 0.854586
INFO:tensorflow:accuracy: 0.857615
I0821 10:15:20.876875 140470324782848 run_classifier.py:535] accuracy: 0.857615

(0.8564584, 0.0010361688279426522)


# subchar_spaced, vocab=5282
nohup ./comp_bert/comp_spaced/scripts/run_classifier_law_qa_5282.sh > logs/subchar_spaced_run_classifier_law_qa_5282.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_law_qa_5282.log_to_commit  (xxx)

[0.855412, 0.866153, 0.863674, 0.849628, 0.858166, 0.861471, 0.856238, 0.852658, 0.857615, 0.856238 ]

(0.8577253, 0.004708174657975195)

# subchar_spaced, vocab=1321
nohup ./comp_bert/comp_spaced/scripts/run_classifier_law_qa_1321.sh > logs/subchar_spaced_run_classifier_law_qa_1321.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_law_qa_1321.log_to_commit  (xxx)

INFO:tensorflow:accuracy: 0.850454
I0821 08:06:54.954979 140203285927680 run_classifier.py:535] accuracy: 0.850454
INFO:tensorflow:accuracy: 0.853208
I0821 08:27:37.875100 139906013779712 run_classifier.py:535] accuracy: 0.853208
INFO:tensorflow:accuracy: 0.853208
I0821 09:05:43.644976 140564761753344 run_classifier.py:535] accuracy: 0.853208
INFO:tensorflow:accuracy: 0.854035
I0821 09:44:43.852674 139848559060736 run_classifier.py:535] accuracy: 0.854035
INFO:tensorflow:accuracy: 0.854310
I0821 10:23:44.080285 139912884926208 run_classifier.py:535] accuracy: 0.854310

(0.8530430000000001, 0.001367239847283553)

```

### char segmented

```bash

# char_segmented, vocab=5282
nohup ./comp_bert/char_segmented/scripts/run_classifier_chn_5282.sh > logs/char_segmented_run_classifier_chn_5282.log_to_commit &
grep "accuracy: " logs/char_segmented_run_classifier_chn_5282.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.871667
I0825 02:00:37.235349 139719687558912 run_classifier.py:535] accuracy: 0.871667
INFO:tensorflow:accuracy: 0.880833
I0825 02:19:21.298739 140109103163136 run_classifier.py:535] accuracy: 0.880833

(0.87625, 0.004583000000000004)

# char_segmented, vocab=5282
nohup ./comp_bert/char_segmented/scripts/run_classifier_law_qa_5282.sh > logs/char_segmented_run_classifier_law_qa_5282.log_to_commit &
grep "accuracy: " logs/char_segmented_run_classifier_law_qa_5282.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.858166
I0825 02:03:42.737190 139879124403968 run_classifier.py:535] accuracy: 0.858166
INFO:tensorflow:accuracy: 0.853484
I0825 02:23:31.543319 139740051719936 run_classifier.py:535] accuracy: 0.853484

# char_segmented, vocab=5282
nohup ./comp_bert/char_segmented/scripts/run_classifier_lcqmc_5282.sh > logs/char_segmented_run_classifier_lcqmc_5282.log_to_commit &
grep "accuracy: " logs/char_segmented_run_classifier_lcqmc_5282.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.793600
I0825 02:17:03.366427 139773689669376 run_classifier.py:535] accuracy: 0.793600
INFO:tensorflow:accuracy: 0.783680
I0825 02:42:06.030442 139805456787200 run_classifier.py:535] accuracy: 0.783680
INFO:tensorflow:accuracy: 0.786400
I0825 03:07:01.723360 140226122008320 run_classifier.py:535] accuracy: 0.786400

(0.7878933333333333, 0.004185222680920177)

# char_segmented, vocab=5282
nohup ./comp_bert/char_segmented/scripts/run_classifier_nlpcc_dbqa_5282.sh > logs/char_segmented_run_classifier_nlpcc_dbqa_5282.log_to_commit &
grep "macro avg" logs/char_segmented_run_classifier_nlpcc_dbqa_5282.log_to_commit (xxx)

"macro avg": {
  "macro avg": {
{'1': {'f1-score': 0.29288924134284955, 'recall': 0.27156862745098037, 'precision': 0.3178427997705106, 'support': 4080}, 'macro avg': {'f1-score': 0.6292427120633968, 'recall': 0.6204336630334844, 'precision': 0.6398823223708414, 'support': 81536}, '0': {'f1-score': 0.965596182783944, 'recall': 0.9692986986159884, 'precision': 0.9619218449711723, 'support': 77456}, 'weighted avg': {'f1-score': 0.9319344343405611, 'recall': 0.9343848116169545, 'precision': 0.9296926148836197, 'support': 81536}, 'accuracy': 0.9343848116169545}
  "macro avg": {
  "macro avg": {
  
  
  
{'macro avg': {'recall': 0.6239601433426087, 'support': 81536, 'precision': 0.6313333238321547, 'f1-score': 0.627510595399419}, '0': {'recall': 0.9653222474695311, 'support': 77456, 'precision': 0.9623280178127855, 'f1-score': 0.9638228071645407}, 'weighted avg': {'recall': 0.9311592425431711, 'support': 81536, 'precision': 0.9292025676695121, 'f1-score': 0.9301651878552369}, '1': {'recall': 0.28259803921568627, 'support': 4080, 'precision': 0.3003386298515238, 'f1-score': 0.2911983836342973}, 'accuracy': 0.9311592425431711}
  "macro avg": {
  "macro avg": {
  
  
  
{'macro avg': {'f1-score': 0.6039284089881783, 'precision': 0.6311919061878404, 'support': 81536, 'recall': 0.5876061703342771}, 'accuracy': 0.9370830062794349, 'weighted avg': {'f1-score': 0.9308280042120781, 'precision': 0.9258084314466984, 'support': 81536, 'recall': 0.9370830062794349}, '0': {'f1-score': 0.9671818623813301, 'precision': 0.9585721531828557, 'support': 77456, 'recall': 0.9759476347862012}, '1': {'f1-score': 0.24067495559502664, 'precision': 0.3038116591928251, 'support': 4080, 'recall': 0.19926470588235295}}

[0.6292427120633968, 0.627510595399419, 0.6039284089881783]
(0.620227238816998, 0.011546686317612926)


# char_segmented, vocab=5282
nohup ./comp_bert/char_segmented/scripts/run_classifier_book_review_5282.sh > logs/char_segmented_run_classifier_book_review_5282.log_to_commit &
grep "accuracy: " logs/char_segmented_run_classifier_book_review_5282.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.783300
I0825 02:04:18.245216 139776369071872 run_classifier.py:535] accuracy: 0.783300
INFO:tensorflow:accuracy: 0.787300
I0825 02:23:08.357668 139890098325248 run_classifier.py:535] accuracy: 0.787300

(0.7853, 0.002000)

# char_segmented, vocab=5282
nohup ./comp_bert/char_segmented/scripts/run_classifier_shopping_5282.sh > logs/char_segmented_run_classifier_shopping_5282.log_to_commit &
grep "accuracy: " logs/char_segmented_run_classifier_shopping_5282.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.917700
I0825 02:39:11.127845 139950979397376 run_classifier.py:535] accuracy: 0.917700
INFO:tensorflow:accuracy: 0.921600
I0825 03:31:05.272953 139809315649280 run_classifier.py:535] accuracy: 0.921600
INFO:tensorflow:accuracy: 0.924400
I0825 04:22:27.476329 139703760021248 run_classifier.py:535] accuracy: 0.924400
INFO:tensorflow:accuracy: 0.925300
I0825 05:13:50.748475 140102101989120 run_classifier.py:535] accuracy: 0.925300
INFO:tensorflow:accuracy: 0.920900
I0825 06:06:01.145343 139801581594368 run_classifier.py:535] accuracy: 0.920900
INFO:tensorflow:accuracy: 0.923600
I0825 06:57:15.075316 139636004890368 run_classifier.py:535] accuracy: 0.923600
INFO:tensorflow:accuracy: 0.923300
I0825 07:48:32.008706 139635989243648 run_classifier.py:535] accuracy: 0.923300
INFO:tensorflow:accuracy: 0.922900
I0825 08:39:38.939351 140450267887360 run_classifier.py:535] accuracy: 0.922900

(0.9224625, 0.002232116428414979)

# char_segmented, vocab=5282
nohup ./comp_bert/char_segmented/scripts/run_classifier_weibo_5282.sh > logs/char_segmented_run_classifier_weibo_5282.log_to_commit &
grep "accuracy: " logs/char_segmented_run_classifier_weibo_5282.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.884000
I0825 02:38:41.867649 140125426329344 run_classifier.py:535] accuracy: 0.884000
INFO:tensorflow:accuracy: 0.884000
I0825 03:25:41.445204 139791583553280 run_classifier.py:535] accuracy: 0.884000
INFO:tensorflow:accuracy: 0.882900
I0825 04:13:00.078640 139910258935552 run_classifier.py:535] accuracy: 0.882900
INFO:tensorflow:accuracy: 0.883800
I0825 04:59:02.370945 140456418780928 run_classifier.py:535] accuracy: 0.883800
INFO:tensorflow:accuracy: 0.883100
I0825 05:46:42.145419 139793504081664 run_classifier.py:535] accuracy: 0.883100
INFO:tensorflow:accuracy: 0.883400
I0825 06:33:01.436408 140427604543232 run_classifier.py:535] accuracy: 0.883400
INFO:tensorflow:accuracy: 0.880700
I0825 07:18:35.484356 140296921216768 run_classifier.py:535] accuracy: 0.880700
INFO:tensorflow:accuracy: 0.882900
I0825 08:04:20.705508 140279174326016 run_classifier.py:535] accuracy: 0.882900
INFO:tensorflow:accuracy: 0.882500
I0825 08:49:58.663060 140405871785728 run_classifier.py:535] accuracy: 0.882500

(0.8830333333333333, 0.0009637888196533924)

# char_segmented, vocab=5282
nohup ./comp_bert/char_segmented/scripts/run_classifier_xnli_5282.sh > logs/char_segmented_run_classifier_xnli_5282.log_to_commit &
grep "accuracy: " logs/char_segmented_run_classifier_xnli_5282.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.597804
I0825 03:12:12.360621 139982536906496 run_classifier.py:535] accuracy: 0.597804
INFO:tensorflow:accuracy: 0.593214
I0825 04:28:29.407170 139859645028096 run_classifier.py:535] accuracy: 0.593214
INFO:tensorflow:accuracy: 0.585629
I0825 05:45:58.172901 139662334514944 run_classifier.py:535] accuracy: 0.585629
INFO:tensorflow:accuracy: 0.590818
I0825 07:04:27.972264 139636005553920 run_classifier.py:535] accuracy: 0.590818
INFO:tensorflow:accuracy: 0.587226
I0825 08:21:41.454043 140142765135616 run_classifier.py:535] accuracy: 0.587226

```


### char spaced

```bash

# char_spaced, vocab=5282
nohup ./comp_bert/char_spaced/scripts/run_classifier_chn_5282.sh > logs/char_spaced_run_classifier_chn_5282.log_to_commit &
grep "accuracy: " logs/char_spaced_run_classifier_chn_5282.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.875833
I0825 10:14:33.573439 140186692491008 run_classifier.py:535] accuracy: 0.875833
INFO:tensorflow:accuracy: 0.850833
I0825 10:44:57.506156 139651468158720 run_classifier.py:535] accuracy: 0.850833
INFO:tensorflow:accuracy: 0.880000
I0825 11:16:29.915384 140349509478144 run_classifier.py:535] accuracy: 0.880000
INFO:tensorflow:accuracy: 0.857500
I0825 11:55:30.085951 140467678656256 run_classifier.py:535] accuracy: 0.857500
INFO:tensorflow:accuracy: 0.861667
I0825 12:34:29.538506 140085880317696 run_classifier.py:535] accuracy: 0.861667
INFO:tensorflow:accuracy: 0.878333
I0825 13:13:29.617632 140485960984320 run_classifier.py:535] accuracy: 0.878333
INFO:tensorflow:accuracy: 0.870000
I0825 13:52:29.983161 140403633612544 run_classifier.py:535] accuracy: 0.870000
INFO:tensorflow:accuracy: 0.848333
I0825 14:31:31.973386 140713819076352 run_classifier.py:535] accuracy: 0.848333
INFO:tensorflow:accuracy: 0.872500
I0825 15:10:29.713615 139745210304256 run_classifier.py:535] accuracy: 0.872500

(0.8661110000000001, 0.01123543776529326)

# char_spaced, vocab=5282
nohup ./comp_bert/char_spaced/scripts/run_classifier_law_qa_5282.sh > logs/char_spaced_run_classifier_law_qa_5282.log_to_commit &
grep "accuracy: " logs/char_spaced_run_classifier_law_qa_5282.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.854861
I0825 10:35:56.871708 140546171787008 run_classifier.py:535] accuracy: 0.854861
INFO:tensorflow:accuracy: 0.854586
I0825 11:16:46.739145 140445734926080 run_classifier.py:535] accuracy: 0.854586
INFO:tensorflow:accuracy: 0.852382
I0825 11:54:37.950382 140129600419584 run_classifier.py:535] accuracy: 0.852382
INFO:tensorflow:accuracy: 0.855136
I0825 12:26:56.873805 140471937767168 run_classifier.py:535] accuracy: 0.855136

(0.85424125, 0.001090909110558719)

# char_spaced, vocab=5282
nohup ./comp_bert/char_spaced/scripts/run_classifier_lcqmc_5282.sh > logs/char_spaced_run_classifier_lcqmc_5282.log_to_commit &
grep "accuracy: " logs/char_spaced_run_classifier_lcqmc_5282.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.781440
I0826 02:30:04.916332 140525468677888 run_classifier.py:535] accuracy: 0.781440
INFO:tensorflow:accuracy: 0.773200
I0826 02:55:29.150156 140493949363968 run_classifier.py:535] accuracy: 0.773200
INFO:tensorflow:accuracy: 0.783600
I0826 03:25:17.444669 139789036857088 run_classifier.py:535] accuracy: 0.783600
INFO:tensorflow:accuracy: 0.788000
I0826 03:52:26.015984 140104987440896 run_classifier.py:535] accuracy: 0.788000
INFO:tensorflow:accuracy: 0.766320
I0826 04:17:50.537730 140687999338240 run_classifier.py:535] accuracy: 0.766320

(0.7785120000000001, 0.007763314755953161)

# char_spaced, vocab=5282
nohup ./comp_bert/char_spaced/scripts/run_classifier_nlpcc_dbqa_5282.sh > logs/char_spaced_run_classifier_nlpcc_dbqa_5282.log_to_commit &
grep "macro avg" logs/char_spaced_run_classifier_nlpcc_dbqa_5282.log_to_commit (xxx)



{'0': {'recall': 0.9691954141706259, 'f1-score': 0.9667490856642457, 'precision': 0.9643150755318056, 'support': 77456}, 'accuracy': 0.9366660125588697, 'macro avg': {'recall': 0.6441565306147248, 'f1-score': 0.6509852534397438, 'precision': 0.658675975943777, 'support': 81536}, 'weighted avg': {'recall': 0.9366660125588697, 'f1-score': 0.9351479172116365, 'precision': 0.933727175062831, 'support': 81536}, '1': {'recall': 0.3191176470588235, 'f1-score': 0.335221421215242, 'precision': 0.3530368763557484, 'support': 4080}}
  "macro avg": {
  "macro avg": {
  
  
{'accuracy': 0.9317479395604396, '0': {'recall': 0.9677752530468912, 'support': 77456, 'precision': 0.9606684694152174, 'f1-score': 0.9642087661189183}, 'weighted avg': {'recall': 0.9317479395604396, 'support': 81536, 'precision': 0.9270226861795478, 'f1-score': 0.9292963706111832}, '1': {'recall': 0.24779411764705883, 'support': 4080, 'precision': 0.28828058169375537, 'f1-score': 0.2665085013839462}, 'macro avg': {'recall': 0.607784685346975, 'support': 81536, 'precision': 0.6244745255544863, 'f1-score': 0.6153586337514323}}
  "macro avg": {
  "macro avg": {
  
  
  
{'weighted avg': {'precision': 0.9403521610034843, 'recall': 0.9439143445839875, 'f1-score': 0.9420207093943802, 'support': 81536}, '0': {'precision': 0.9672166878213264, 'recall': 0.9739723197686428, 'f1-score': 0.9705827484834645, 'support': 77456}, 'macro avg': {'precision': 0.6987821218140258, 'recall': 0.6736283167470665, 'f1-score': 0.6851863735854782, 'support': 81536}, '1': {'precision': 0.43034755580672507, 'recall': 0.3732843137254902, 'f1-score': 0.3997899986874918, 'support': 4080}, 'accuracy': 0.9439143445839875}
  "macro avg": {
  "macro avg": {
  
  
  
{'weighted avg': {'support': 81536, 'f1-score': 0.927472015211572, 'recall': 0.9290497448979592, 'precision': 0.9259610982764606}, 'macro avg': {'support': 81536, 'f1-score': 0.610300800229785, 'recall': 0.6056679617726042, 'precision': 0.615505571565405}, 'accuracy': 0.9290497448979592, '0': {'support': 77456, 'f1-score': 0.9627439994332709, 'recall': 0.9650123941334435, 'precision': 0.9604862440729366}, '1': {'support': 4080, 'f1-score': 0.2578576010262989, 'recall': 0.24632352941176472, 'precision': 0.27052489905787347}}
  "macro avg": {
  "macro avg": {
  
  
  
{'1': {'f1-score': 0.29656772932698183, 'recall': 0.29754901960784313, 'support': 4080, 'precision': 0.2955928901874848}, 'macro avg': {'f1-score': 0.6296926518281615, 'recall': 0.6300993910268095, 'support': 81536, 'precision': 0.6292891674587477}, 'weighted avg': {'f1-score': 0.9294789341261226, 'recall': 0.9293686224489796, 'support': 81536, 'precision': 0.9295896242024707}, 'accuracy': 0.9293686224489796, '0': {'f1-score': 0.9628175743293411, 'recall': 0.9626497624457757, 'support': 77456, 'precision': 0.9629854447300107}}
  "macro avg": {
  "macro avg": {
  
  [0.6509852534397438, 0.6153586337514323, 0.6851863735854782, 0.610300800229785, 0.6296926518281615, 0.6540865372933917]
  
{'accuracy': 0.9348999215070644, 'macro avg': {'recall': 0.6525144699482768, 'f1-score': 0.6540865372933917, 'support': 81536, 'precision': 0.6556996175369412}, 'weighted avg': {'recall': 0.9348999215070644, 'f1-score': 0.9345635448081261, 'support': 81536, 'precision': 0.9342318328963028}, '0': {'recall': 0.9663034497004751, 'f1-score': 0.9657548387096774, 'support': 77456, 'precision': 0.9652068503043434}, '1': {'recall': 0.33872549019607845, 'f1-score': 0.34241823587710607, 'support': 4080, 'precision': 0.34619238476953906}}


[0.6509852534397438, 0.6153586337514323, 0.6851863735854782, 0.610300800229785, 0.6296926518281615, 0.6540865372933917]
(0.6409350416879988, 0.025661740945204927)


# char_spaced, vocab=5282
nohup ./comp_bert/char_spaced/scripts/run_classifier_book_review_5282.sh > logs/char_spaced_run_classifier_book_review_5282.log_to_commit &
grep "accuracy: " logs/char_spaced_run_classifier_book_review_5282.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.769400
I0826 02:40:10.897957 140358112175872 run_classifier.py:535] accuracy: 0.769400
INFO:tensorflow:accuracy: 0.784900
I0826 03:00:11.122016 140530634475264 run_classifier.py:535] accuracy: 0.784900
INFO:tensorflow:accuracy: 0.777400
I0826 03:39:08.977522 140293294286592 run_classifier.py:535] accuracy: 0.777400
INFO:tensorflow:accuracy: 0.776600
I0826 04:18:10.371695 140534035511040 run_classifier.py:535] accuracy: 0.776600
INFO:tensorflow:accuracy: 0.783100
I0826 04:57:11.407596 139789934700288 run_classifier.py:535] accuracy: 0.783100

(0.77828, 0.00546823554723096)

# char_spaced, vocab=5282
nohup ./comp_bert/char_spaced/scripts/run_classifier_shopping_5282.sh > logs/char_spaced_run_classifier_shopping_5282.log_to_commit &
grep "accuracy: " logs/char_spaced_run_classifier_shopping_5282.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.913400
I0825 10:56:30.050683 140209176618752 run_classifier.py:535] accuracy: 0.913400
INFO:tensorflow:accuracy: 0.920000
I0825 11:50:59.064877 140392547890944 run_classifier.py:535] accuracy: 0.920000
INFO:tensorflow:accuracy: 0.915200
I0825 12:43:11.057611 140706956273408 run_classifier.py:535] accuracy: 0.915200

(0.9161999999999999, 0.0027856776554368435)

# char_spaced, vocab=5282
nohup ./comp_bert/char_spaced/scripts/run_classifier_weibo_5282.sh > logs/char_spaced_run_classifier_weibo_5282.log_to_commit &
grep "accuracy: " logs/char_spaced_run_classifier_weibo_5282.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.967300
I0826 02:50:49.243530 139761418401536 run_classifier.py:535] accuracy: 0.967300
INFO:tensorflow:accuracy: 0.966400
I0826 03:18:44.089919 140259455153920 run_classifier.py:535] accuracy: 0.966400
INFO:tensorflow:accuracy: 0.959500
I0826 03:49:28.290684 139932517443328 run_classifier.py:535] accuracy: 0.959500
INFO:tensorflow:accuracy: 0.961100
I0826 04:28:28.399928 139694382540544 run_classifier.py:535] accuracy: 0.961100
INFO:tensorflow:accuracy: 0.965900
I0826 05:07:28.429215 139703956391680 run_classifier.py:535] accuracy: 0.965900

(0.96404, 0.0031276828483719544)

# char_spaced, vocab=5282
nohup ./comp_bert/char_spaced/scripts/run_classifier_xnli_5282.sh > logs/char_spaced_run_classifier_xnli_5282.log_to_commit &
grep "accuracy: " logs/char_spaced_run_classifier_xnli_5282.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.587226
I0826 03:34:03.056624 140288743036672 run_classifier.py:535] accuracy: 0.587226
INFO:tensorflow:accuracy: 0.584431
I0826 04:11:56.819350 139659916760832 run_classifier.py:535] accuracy: 0.584431
INFO:tensorflow:accuracy: 0.592615
I0826 04:49:57.825774 140251107505920 run_classifier.py:535] accuracy: 0.592615
INFO:tensorflow:accuracy: 0.604391
I0826 05:28:13.188903 139908120168192 run_classifier.py:535] accuracy: 0.604391

(0.59216575, 0.007646666769743525)

```