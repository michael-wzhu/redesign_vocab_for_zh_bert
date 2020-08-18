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

# subchar_spaced, vocab=1321
nohup ./comp_bert/comp_spaced/scripts/create_pretrain_data_1321_1_25.sh > logs/comp_spaced_create_pretrain_data_1321_1_25.log &
nohup ./comp_bert/comp_spaced/scripts/create_pretrain_data_1321_26_40.sh > logs/comp_spaced_create_pretrain_data_1321_26_40.log &
nohup ./comp_bert/comp_spaced/scripts/create_pretrain_data_1321_41_85.sh > logs/comp_spaced_create_pretrain_data_1321_41_85.log &
nohup ./comp_bert/comp_spaced/scripts/create_pretrain_data_1321_86_130.sh > logs/comp_spaced_create_pretrain_data_1321_86_130.log &
nohup ./comp_bert/comp_spaced/scripts/create_pretrain_data_1321_131_175.sh > logs/comp_spaced_create_pretrain_data_1321_131_175.log &
nohup ./comp_bert/comp_spaced/scripts/create_pretrain_data_1321_176_218.sh > logs/comp_spaced_create_pretrain_data_1321_176_218.log &


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

# subchar_segmented, vocab=1321
nohup ./comp_bert/comp_segmented/scripts/run_classifier_chn_1321.sh > logs/subchar_segmented_run_classifier_chn_1321.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_chn_1321.log_to_commit (done)

I0816 00:58:11.826314 140210183026432 run_classifier.py:535] accuracy: 0.818333
INFO:tensorflow:accuracy: 0.819167
I0816 01:19:43.956153 140659666052864 run_classifier.py:535] accuracy: 0.819167
INFO:tensorflow:accuracy: 0.835833
I0816 01:56:17.189684 140058013034240 run_classifier.py:535] accuracy: 0.835833
INFO:tensorflow:accuracy: 0.818333
I0816 02:35:16.322833 140063805449984 run_classifier.py:535] accuracy: 0.818333
INFO:tensorflow:accuracy: 0.815000
I0816 03:14:16.310876 140641165555456 run_classifier.py:535] accuracy: 0.815000


# subchar_spaced, vocab=21128
nohup ./comp_bert/comp_spaced/scripts/run_classifier_chn_21128.sh > logs/subchar_spaced_run_classifier_chn_21128.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_chn_21128.log_to_commit (xxx)

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

# subchar_segmented, vocab=5282
nohup ./comp_bert/comp_segmented/scripts/run_classifier_lcqmc_5282.sh > logs/subchar_segmented_run_classifier_lcqmc_5282.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_lcqmc_5282.log_to_commit (done)

I0816 05:13:20.132289 139764198987520 run_classifier.py:535] accuracy: 0.770160
INFO:tensorflow:accuracy: 0.769760
I0816 05:50:36.097698 140664251246336 run_classifier.py:535] accuracy: 0.769760
INFO:tensorflow:accuracy: 0.770160
I0816 06:16:48.525429 139632845608704 run_classifier.py:535] accuracy: 0.770160
INFO:tensorflow:accuracy: 0.755600
I0816 06:42:46.548686 140300511172352 run_classifier.py:535] accuracy: 0.755600

# subchar_segmented, vocab=1321
nohup ./comp_bert/comp_segmented/scripts/run_classifier_lcqmc_1321.sh > logs/subchar_segmented_run_classifier_lcqmc_1321.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_lcqmc_1321.log_to_commit (done)

I0816 04:59:59.052143 139844458825472 run_classifier.py:535] accuracy: 0.740160
INFO:tensorflow:accuracy: 0.754000
I0816 05:39:10.810330 140268642195200 run_classifier.py:535] accuracy: 0.754000
INFO:tensorflow:accuracy: 0.748960
I0816 06:05:10.869757 140249215497984 run_classifier.py:535] accuracy: 0.748960
INFO:tensorflow:accuracy: 0.745440
I0816 06:30:57.283895 140280868562688 run_classifier.py:535] accuracy: 0.745440
INFO:tensorflow:accuracy: 0.745280
I0816 06:56:44.459246 140255385433856 run_classifier.py:535] accuracy: 0.745280


# subchar_spaced, vocab=21128
nohup ./comp_bert/comp_spaced/scripts/run_classifier_lcqmc_21128.sh > logs/subchar_spaced_run_classifier_lcqmc_21128.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_lcqmc_21128.log_to_commit (xxx)

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


```



### on xnli

```bash

# subchar_segmented, vocab=21128
nohup ./comp_bert/comp_segmented/scripts/run_classifier_xnli_21128.sh > logs/subchar_segmented_run_classifier_xnli_21128.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_xnli_21128.log_to_commit

I0813 05:08:50.479553 140252936034048 run_classifier.py:535] accuracy: 0.554291
INFO:tensorflow:accuracy: 0.577246
I0813 06:04:54.744012 140718557275904 run_classifier.py:535] accuracy: 0.577246
INFO:tensorflow:accuracy: 0.566068
I0813 06:45:24.131435 139821034039040 run_classifier.py:535] accuracy: 0.566068
INFO:tensorflow:accuracy: 0.570060
I0813 07:25:45.793235 139746511324928 run_classifier.py:535] accuracy: 0.570060
INFO:tensorflow:accuracy: 0.546108
I0813 08:06:17.681382 140012420654848 run_classifier.py:535] accuracy: 0.546108

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

```