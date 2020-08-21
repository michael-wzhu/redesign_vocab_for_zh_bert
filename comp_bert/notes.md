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


# char_segmented, vocab=5282
nohup ./comp_bert/char_segmented/scripts/create_pretrain_data_5282_1_25.sh > char_segmented_create_pretrain_data_5282_1_25.log &
nohup ./comp_bert/char_segmented/scripts/create_pretrain_data_5282_26_65.sh > char_segmented_create_pretrain_data_5282_26_65.log &
nohup ./comp_bert/char_segmented/scripts/create_pretrain_data_5282_66_120.sh > char_segmented_create_pretrain_data_5282_66_120.log &

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



```


### on nlpcc_dbqa


```bash

# subchar_segmented, vocab=21128
nohup ./comp_bert/comp_segmented/scripts/run_classifier_nlpcc_dbqa_21128.sh > logs/subchar_segmented_run_classifier_nlpcc_dbqa_21128.log_to_commit &
grep "macro avg" logs/subchar_segmented_run_classifier_nlpcc_dbqa_21128.log_to_commit   (xxx)

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

```

### law_qa

```bash

# subchar_spaced, vocab=21128
nohup ./comp_bert/comp_spaced/scripts/run_classifier_law_qa_21128.sh > logs/subchar_spaced_run_classifier_law_qa_21128.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_law_qa_21128.log_to_commit  (xxx)



# subchar_spaced, vocab=5282
nohup ./comp_bert/comp_spaced/scripts/run_classifier_law_qa_5282.sh > logs/subchar_spaced_run_classifier_law_qa_5282.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_law_qa_5282.log_to_commit  (xxx)


# subchar_spaced, vocab=1321
nohup ./comp_bert/comp_spaced/scripts/run_classifier_law_qa_1321.sh > logs/subchar_spaced_run_classifier_law_qa_1321.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_law_qa_1321.log_to_commit  (xxx)


```




| model | chn | lcqmc |  xnli   |
| :----: | :----: | :----: |  :----: |
| comp_segmented, 21128	     |    0.8543, 0.01301       |    (0.7531, 0.005004)     |   (0.5628, 0.011163)     |   
| comp_segmented, 5282	     |     (0.8350, 0.013038)      |   (0.7664, 0.006220)      |   (0.5582434, 0.006536)   |
| comp_segmented, 1321	     |     (0.8213, 0.007389)      |   (0.7468, 0.004577)     |   (0.5249, 0.008236)    |
|  comp_spaced, 21128       |     (0.8549, 0.008475)      |   (0.7659, 0.004760)    |   (0.5632, 0.005602)    |
|  comp_spaced, 5282       |    (0.8479, 0.009510)       |   (0.7644, 0.006812)    |   (0.5660, 0.005889)   |
|  comp_spaced, 1321       |           |       |      |