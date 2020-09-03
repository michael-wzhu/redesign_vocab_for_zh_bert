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

# char_segmented, vocab=1321
nohup ./comp_bert/char_segmented/scripts/run_pretrain_1321.sh > logs/char_segmented_pretrain_1321.log & (xxx)


# char_spaced, vocab=21128
nohup ./comp_bert/char_spaced/scripts/run_pretrain_21128.sh > logs/char_spaced_pretrain_21128.log & 

# char_spaced, vocab=5282
nohup ./comp_bert/char_spaced/scripts/run_pretrain_5282.sh > logs/char_spaced_pretrain_5282.log & 

# char_spaced, vocab=1321
nohup ./comp_bert/char_spaced/scripts/run_pretrain_1321.sh > logs/char_spaced_pretrain_1321.log & 


```


## finetune


### on chn

```bash

# subchar_segmented, vocab=21128

nohup ./comp_bert/comp_segmented/scripts/run_classifier_chn_21128.sh > logs/subchar_segmented_run_classifier_chn_21128.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_chn_21128.log_to_commit (done)

def get_stat(a):
    score_list = [float(w.split(" ")[-1]) for w in a.split("\n")]
    return np.mean(score_list), np.std(score_list)
    
score_stats = get_stat(a)
print(get_stat(""""""))

(0.8543331999999999, 0.013010552984404622)

# subchar_segmented, vocab=5282
nohup ./comp_bert/comp_segmented/scripts/run_classifier_chn_5282.sh > logs/subchar_segmented_run_classifier_chn_5282.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_chn_5282.log_to_commit (done)

(0.835, 0.013038404810405314)


# subchar_segmented, vocab=1321
nohup ./comp_bert/comp_segmented/scripts/run_classifier_chn_1321.sh > logs/subchar_segmented_run_classifier_chn_1321.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_chn_1321.log_to_commit (done)

(0.8213332, 0.007389836869647427)

# subchar_spaced, vocab=21128
nohup ./comp_bert/comp_spaced/scripts/run_classifier_chn_21128.sh > logs/subchar_spaced_run_classifier_chn_21128.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_chn_21128.log_to_commit (xxx)

(0.8549075555555555, 0.008475085330427344)

# subchar_spaced, vocab=5282
nohup ./comp_bert/comp_spaced/scripts/run_classifier_chn_5282.sh > logs/subchar_spaced_run_classifier_chn_5282.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_chn_5282.log_to_commit (xxx)

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

(0.753184, 0.0050042925573950976)

# subchar_segmented, vocab=5282
nohup ./comp_bert/comp_segmented/scripts/run_classifier_lcqmc_5282.sh > logs/subchar_segmented_run_classifier_lcqmc_5282.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_lcqmc_5282.log_to_commit (done)

(0.76637, 0.0062204742584468274)

# subchar_segmented, vocab=1321
nohup ./comp_bert/comp_segmented/scripts/run_classifier_lcqmc_1321.sh > logs/subchar_segmented_run_classifier_lcqmc_1321.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_lcqmc_1321.log_to_commit (done)

(0.746768, 0.004577118744363078)

# subchar_spaced, vocab=21128
nohup ./comp_bert/comp_spaced/scripts/run_classifier_lcqmc_21128.sh > logs/subchar_spaced_run_classifier_lcqmc_21128.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_lcqmc_21128.log_to_commit (done)

(0.765856, 0.004760477286995519)

# subchar_spaced, vocab=5282
nohup ./comp_bert/comp_spaced/scripts/run_classifier_lcqmc_5282.sh > logs/subchar_spaced_run_classifier_lcqmc_5282.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_lcqmc_5282.log_to_commit (xxx)

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

(0.5627546000000001, 0.011163243070004348)

# subchar_segmented, vocab=5282
nohup ./comp_bert/comp_segmented/scripts/run_classifier_xnli_5282.sh > logs/subchar_segmented_run_classifier_xnli_5282.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_xnli_5282.log_to_commit (done)

(0.5582434, 0.006535726603829155)

# subchar_segmented, vocab=1321

nohup ./comp_bert/comp_segmented/scripts/run_classifier_xnli_1321.sh > logs/subchar_segmented_run_classifier_xnli_1321.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_xnli_1321.log_to_commit (xxx)

(0.5249499999999999, 0.008236753243845553)

# subchar_spaced, vocab=21128
nohup ./comp_bert/comp_spaced/scripts/run_classifier_xnli_21128.sh > logs/subchar_spaced_run_classifier_xnli_21128.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_xnli_21128.log_to_commit (xxx)

(0.5632733999999999, 0.0056028395158169405)

# subchar_spaced, vocab=5282
nohup ./comp_bert/comp_spaced/scripts/run_classifier_xnli_5282.sh > logs/subchar_spaced_run_classifier_xnli_5282.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_xnli_5282.log_to_commit (xxx)

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

 [0.5778911758321731, 0.5727065298044567, 0.5760363372121583, 0.5784218478361854, 0.5626384782322722, 0.5759459700310551, 0.5802422900427759, 0.5914858439327211, 0.5688184735627756]
 
 (0.5760207718318415, 0.007514446592634158)

# subchar_segmented, vocab=1321
nohup ./comp_bert/comp_segmented/scripts/run_classifier_nlpcc_dbqa_1321.sh > logs/subchar_segmented_run_classifier_nlpcc_dbqa_1321.log_to_commit &
grep "macro avg" logs/subchar_segmented_run_classifier_nlpcc_dbqa_1321.log_to_commit   (xxx)

[0.5899387494882112,  0.560694862453139, 0.588238700244295, 0.5847137283631348, 0.57214836905220, 0.57551463779825, 0.5868775373026048, 0.5709862324265559, 0.5770636002878589]
 
 (0.5784640463795834, 0.009184937326831255)
 


# subchar_spaced, vocab=21128
nohup ./comp_bert/comp_spaced/scripts/run_classifier_nlpcc_dbqa_21128.sh > logs/subchar_spaced_run_classifier_nlpcc_dbqa_21128.log_to_commit &
grep "macro avg" logs/subchar_spaced_run_classifier_nlpcc_dbqa_21128.log_to_commit   (xxx)

grep "macro avg" logs/subchar_spaced_run_classifier_nlpcc_dbqa_21128.log_to_commit


(0.561314205854611, 0.011169201436428905)

# subchar_spaced, vocab=5282
nohup ./comp_bert/comp_spaced/scripts/run_classifier_nlpcc_dbqa_5282.sh > logs/subchar_spaced_run_classifier_nlpcc_dbqa_5282.log_to_commit &
grep "macro avg" logs/subchar_spaced_run_classifier_nlpcc_dbqa_5282.log_to_commit   (xxx)

[0.5729590917274643, 0.5757530998685632, 0.5686788012204421, 0.5929198025584119, 0.5723495499555522]

(0.5765320690660867, 0.008498212177321756)


# subchar_spaced, vocab=1321
nohup ./comp_bert/comp_spaced/scripts/run_classifier_nlpcc_dbqa_1321.sh > logs/subchar_spaced_run_classifier_nlpcc_dbqa_1321.log_to_commit &
grep "macro avg" logs/subchar_spaced_run_classifier_nlpcc_dbqa_1321.log_to_commit   (xxx)

(0.5960603200470805, 0.012279454565546266)


```


### on book_review

```bash

# subchar_segmented, vocab=21128
nohup ./comp_bert/comp_segmented/scripts/run_classifier_book_review_21128.sh > logs/subchar_segmented_run_classifier_book_review_21128.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_book_review_21128.log_to_commit  (xxx)

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

(0.75514, 0.00646949)

```


### on shopping

```bash

# subchar_segmented, vocab=21128
nohup ./comp_bert/comp_segmented/scripts/run_classifier_shopping_21128.sh > logs/subchar_segmented_run_classifier_shopping_21128.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_shopping_21128.log_to_commit  (xxx)

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

(0.9674500000000001, 0.003512620104708165)

# subchar_spaced, vocab=5282
nohup ./comp_bert/comp_spaced/scripts/run_classifier_weibo_5282.sh > logs/subchar_spaced_run_classifier_weibo_5282.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_weibo_5282.log_to_commit  (xxx)

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

(0.8505369999999999, 0.002830235149241156)

# subchar_segmented, vocab=5282
nohup ./comp_bert/comp_segmented/scripts/run_classifier_law_qa_5282.sh > logs/subchar_segmented_run_classifier_law_qa_5282.log_to_commit &
grep "accuracy: " logs/subchar_segmented_run_classifier_law_qa_5282.log_to_commit  (xxx)

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

(0.8564584, 0.0010361688279426522)


# subchar_spaced, vocab=5282
nohup ./comp_bert/comp_spaced/scripts/run_classifier_law_qa_5282.sh > logs/subchar_spaced_run_classifier_law_qa_5282.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_law_qa_5282.log_to_commit  (xxx)

[0.855412, 0.866153, 0.863674, 0.849628, 0.858166, 0.861471, 0.856238, 0.852658, 0.857615, 0.856238 ]

(0.8577253, 0.004708174657975195)

# subchar_spaced, vocab=1321
nohup ./comp_bert/comp_spaced/scripts/run_classifier_law_qa_1321.sh > logs/subchar_spaced_run_classifier_law_qa_1321.log_to_commit &
grep "accuracy: " logs/subchar_spaced_run_classifier_law_qa_1321.log_to_commit  (xxx)

(0.8530430000000001, 0.001367239847283553)

```

### char segmented

```bash

# char_segmented, vocab=21128
nohup ./comp_bert/char_segmented/scripts/run_classifier_chn_21128.sh > logs/char_segmented_run_classifier_chn_21128.log_to_commit &
grep "accuracy: " logs/char_segmented_run_classifier_chn_21128.log_to_commit (xxx)

(0.8779999, 0.008859971788329797)

# char_segmented, vocab=5282
nohup ./comp_bert/char_segmented/scripts/run_classifier_chn_5282.sh > logs/char_segmented_run_classifier_chn_5282.log_to_commit &
grep "accuracy: " logs/char_segmented_run_classifier_chn_5282.log_to_commit (done)

(0.87625, 0.004583000000000004)

# char_segmented, vocab=1321
nohup ./comp_bert/char_segmented/scripts/run_classifier_chn_1321.sh > logs/char_segmented_run_classifier_chn_1321.log_to_commit &
grep "accuracy: " logs/char_segmented_run_classifier_chn_1321.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.843333
I0831 02:08:18.983088 140567618004736 run_classifier.py:535] accuracy: 0.843333
INFO:tensorflow:accuracy: 0.863333
I0831 02:30:04.917122 139946388580096 run_classifier.py:535] accuracy: 0.863333
INFO:tensorflow:accuracy: 0.841667
I0831 03:09:04.901158 140025240880896 run_classifier.py:535] accuracy: 0.841667
INFO:tensorflow:accuracy: 0.865000
I0831 03:48:05.090171 140002125584128 run_classifier.py:535] accuracy: 0.865000
INFO:tensorflow:accuracy: 0.865000
I0831 04:27:05.012256 140673547450112 run_classifier.py:535] accuracy: 0.865000
INFO:tensorflow:accuracy: 0.866667
I0831 05:06:04.958561 140217538144000 run_classifier.py:535] accuracy: 0.866667
INFO:tensorflow:accuracy: 0.840000
I0831 05:45:04.809899 139815625443072 run_classifier.py:535] accuracy: 0.840000
INFO:tensorflow:accuracy: 0.853333
I0831 06:24:04.927959 139689404622592 run_classifier.py:535] accuracy: 0.853333
INFO:tensorflow:accuracy: 0.878333
I0831 07:03:04.942304 140003493299968 run_classifier.py:535] accuracy: 0.878333
INFO:tensorflow:accuracy: 0.874167
I0831 07:42:05.079901 140004593911552 run_classifier.py:535] accuracy: 0.874167

(0.8590833, 0.013008819447205808)

# char_segmented, vocab=21128
nohup ./comp_bert/char_segmented/scripts/run_classifier_law_qa_21128.sh > logs/char_segmented_run_classifier_law_qa_21128.log_to_commit &
grep "accuracy: " logs/char_segmented_run_classifier_law_qa_21128.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.864500
I0831 02:17:39.876800 140586305767168 run_classifier.py:535] accuracy: 0.864500
INFO:tensorflow:accuracy: 0.868907
I0831 02:43:12.073811 139837110535936 run_classifier.py:535] accuracy: 0.868907
INFO:tensorflow:accuracy: 0.862848
I0831 03:22:11.632139 140268192581376 run_classifier.py:535] accuracy: 0.862848
INFO:tensorflow:accuracy: 0.861471
I0831 04:01:11.803442 140615954417408 run_classifier.py:535] accuracy: 0.861471
INFO:tensorflow:accuracy: 0.855136
I0831 04:40:12.565528 139974747219712 run_classifier.py:535] accuracy: 0.855136
INFO:tensorflow:accuracy: 0.861471
I0831 05:19:12.323092 139699404187392 run_classifier.py:535] accuracy: 0.861471
INFO:tensorflow:accuracy: 0.860369
I0831 05:58:12.146895 140049178490624 run_classifier.py:535] accuracy: 0.860369
INFO:tensorflow:accuracy: 0.855963
I0831 06:37:12.598335 139835647055616 run_classifier.py:535] accuracy: 0.855963
INFO:tensorflow:accuracy: 0.857064
I0831 07:16:11.866567 139787860535040 run_classifier.py:535] accuracy: 0.857064
INFO:tensorflow:accuracy: 0.855136
I0831 07:55:12.142047 140057624135424 run_classifier.py:535] accuracy: 0.855136

# char_segmented, vocab=5282
nohup ./comp_bert/char_segmented/scripts/run_classifier_law_qa_5282.sh > logs/char_segmented_run_classifier_law_qa_5282.log_to_commit &
grep "accuracy: " logs/char_segmented_run_classifier_law_qa_5282.log_to_commit (xxx)

(0.8567, )


# char_segmented, vocab=1321
nohup ./comp_bert/char_segmented/scripts/run_classifier_law_qa_1321.sh > logs/char_segmented_run_classifier_law_qa_1321.log_to_commit &
grep "accuracy: " logs/char_segmented_run_classifier_law_qa_1321.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.849077
I0831 02:18:07.561636 140453460285184 run_classifier.py:535] accuracy: 0.849077
INFO:tensorflow:accuracy: 0.854035
I0831 02:41:20.711360 139801248675584 run_classifier.py:535] accuracy: 0.854035
INFO:tensorflow:accuracy: 0.854310
I0831 03:17:36.026962 139997704513280 run_classifier.py:535] accuracy: 0.854310
INFO:tensorflow:accuracy: 0.852382
I0831 03:56:35.847050 140253659477760 run_classifier.py:535] accuracy: 0.852382
INFO:tensorflow:accuracy: 0.854586
I0831 04:35:36.636660 140607682094848 run_classifier.py:535] accuracy: 0.854586
INFO:tensorflow:accuracy: 0.860369
I0831 05:14:36.601303 140110769444608 run_classifier.py:535] accuracy: 0.860369
INFO:tensorflow:accuracy: 0.856238
I0831 05:53:36.775516 140238066153216 run_classifier.py:535] accuracy: 0.856238
INFO:tensorflow:accuracy: 0.855687
I0831 06:32:36.824619 139824657745664 run_classifier.py:535] accuracy: 0.855687
INFO:tensorflow:accuracy: 0.860644
I0831 07:11:36.677894 140172091832064 run_classifier.py:535] accuracy: 0.860644
INFO:tensorflow:accuracy: 0.854861
I0831 07:50:36.828375 140037327681280 run_classifier.py:535] accuracy: 0.854861

# char_segmented, vocab=21128
nohup ./comp_bert/char_segmented/scripts/run_classifier_lcqmc_21128.sh > logs/char_segmented_run_classifier_lcqmc_21128.log_to_commit &
grep "accuracy: " logs/char_segmented_run_classifier_lcqmc_21128.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.796000
I0831 02:41:43.369814 140707169711872 run_classifier.py:535] accuracy: 0.796000
INFO:tensorflow:accuracy: 0.788640
I0831 03:10:27.587275 139870376634112 run_classifier.py:535] accuracy: 0.788640
INFO:tensorflow:accuracy: 0.790880
I0831 03:38:35.949828 139940784248576 run_classifier.py:535] accuracy: 0.790880
INFO:tensorflow:accuracy: 0.779120
I0831 04:05:42.737850 139783300335360 run_classifier.py:535] accuracy: 0.779120
INFO:tensorflow:accuracy: 0.786000
I0831 04:32:51.364475 140218041108224 run_classifier.py:535] accuracy: 0.786000

# char_segmented, vocab=5282
nohup ./comp_bert/char_segmented/scripts/run_classifier_lcqmc_5282.sh > logs/char_segmented_run_classifier_lcqmc_5282.log_to_commit &
grep "accuracy: " logs/char_segmented_run_classifier_lcqmc_5282.log_to_commit (xxx)

(0.7878933333333333, 0.004185222680920177)

# char_segmented, vocab=1321
nohup ./comp_bert/char_segmented/scripts/run_classifier_lcqmc_1321.sh > logs/char_segmented_run_classifier_lcqmc_1321.log_to_commit &
grep "accuracy: " logs/char_segmented_run_classifier_lcqmc_1321.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.741520
I0831 03:12:21.663674 140398927644416 run_classifier.py:535] accuracy: 0.741520
INFO:tensorflow:accuracy: 0.737120
I0831 04:08:53.587929 140139013891840 run_classifier.py:535] accuracy: 0.737120
INFO:tensorflow:accuracy: 0.742560
I0831 05:04:14.117447 140104488167168 run_classifier.py:535] accuracy: 0.742560
INFO:tensorflow:accuracy: 0.733040
I0831 05:59:30.112943 140267461965568 run_classifier.py:535] accuracy: 0.733040
INFO:tensorflow:accuracy: 0.747200
I0831 06:55:36.729611 140470802142976 run_classifier.py:535] accuracy: 0.747200

# char_segmented, vocab=21128
nohup ./comp_bert/char_segmented/scripts/run_classifier_nlpcc_dbqa_21128.sh > logs/char_segmented_run_classifier_nlpcc_dbqa_21128.log_to_commit &
grep "macro avg" logs/char_segmented_run_classifier_nlpcc_dbqa_21128.log_to_commit (xxx)

[0.5910643602119752, 0.6199981444990108, 0.6352135531937637, 0.6313336761151621, 0.5873476585546951]


# char_segmented, vocab=5282
nohup ./comp_bert/char_segmented/scripts/run_classifier_nlpcc_dbqa_5282.sh > logs/char_segmented_run_classifier_nlpcc_dbqa_5282.log_to_commit &
grep "macro avg" logs/char_segmented_run_classifier_nlpcc_dbqa_5282.log_to_commit (xxx)

[0.6292427120633968, 0.627510595399419, 0.6039284089881783]
(0.620227238816998, 0.011546686317612926)

# char_segmented, vocab=1321
nohup ./comp_bert/char_segmented/scripts/run_classifier_nlpcc_dbqa_1321.sh > logs/char_segmented_run_classifier_nlpcc_dbqa_1321.log_to_commit &
grep "macro avg" logs/char_segmented_run_classifier_nlpcc_dbqa_1321.log_to_commit (xxx)

 [0.6348036510575531, 0.650506921505267, 0.6406299835764606, 0.6354838791725048, 0.656227061371951]

# char_segmented, vocab=21128
nohup ./comp_bert/char_segmented/scripts/run_classifier_book_review_21128.sh > logs/char_segmented_run_classifier_book_review_21128.log_to_commit &
grep "accuracy: " logs/char_segmented_run_classifier_book_review_21128.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.791000
I0831 03:05:12.765842 140594469185280 run_classifier.py:535] accuracy: 0.791000
INFO:tensorflow:accuracy: 0.791400
I0831 03:58:38.989512 139881134327552 run_classifier.py:535] accuracy: 0.791400
INFO:tensorflow:accuracy: 0.791800
I0831 04:51:21.195221 139650386831104 run_classifier.py:535] accuracy: 0.791800
INFO:tensorflow:accuracy: 0.791800
I0831 05:43:33.525408 139865634887424 run_classifier.py:535] accuracy: 0.791800
INFO:tensorflow:accuracy: 0.793600
I0831 06:36:33.638868 140122240722688 run_classifier.py:535] accuracy: 0.793600
INFO:tensorflow:accuracy: 0.787600
I0831 07:29:48.995024 140435482461952 run_classifier.py:535] accuracy: 0.787600
INFO:tensorflow:accuracy: 0.798300
I0831 08:22:22.136859 139625085228800 run_classifier.py:535] accuracy: 0.798300
INFO:tensorflow:accuracy: 0.794000
I0831 09:13:45.109544 140026615813888 run_classifier.py:535] accuracy: 0.794000
INFO:tensorflow:accuracy: 0.790300
I0831 10:05:19.190850 140305590376192 run_classifier.py:535] accuracy: 0.790300
INFO:tensorflow:accuracy: 0.780400
I0831 10:57:41.597379 139848525969152 run_classifier.py:535] accuracy: 0.780400

# char_segmented, vocab=5282
nohup ./comp_bert/char_segmented/scripts/run_classifier_book_review_5282.sh > logs/char_segmented_run_classifier_book_review_5282.log_to_commit &
grep "accuracy: " logs/char_segmented_run_classifier_book_review_5282.log_to_commit (xxx)

(0.7853, 0.002000)

# char_segmented, vocab=1321
nohup ./comp_bert/char_segmented/scripts/run_classifier_book_review_1321.sh > logs/char_segmented_run_classifier_book_review_1321.log_to_commit &
grep "accuracy: " logs/char_segmented_run_classifier_book_review_1321.log_to_commit (xxx)

INFO:tensorflow:accuracy: 0.758600
I0831 03:06:14.792983 140329991968512 run_classifier.py:535] accuracy: 0.758600
INFO:tensorflow:accuracy: 0.759300
I0831 03:57:58.180694 140297981953792 run_classifier.py:535] accuracy: 0.759300
INFO:tensorflow:accuracy: 0.765300
I0831 04:51:03.022579 140298098378496 run_classifier.py:535] accuracy: 0.765300
INFO:tensorflow:accuracy: 0.765300
I0831 05:44:48.174316 139814760544000 run_classifier.py:535] accuracy: 0.765300
INFO:tensorflow:accuracy: 0.762900
I0831 06:36:55.253487 140212991416064 run_classifier.py:535] accuracy: 0.762900
INFO:tensorflow:accuracy: 0.759600
I0831 07:29:06.885867 140057815582464 run_classifier.py:535] accuracy: 0.759600
INFO:tensorflow:accuracy: 0.760800
I0831 08:22:05.150632 140298969437952 run_classifier.py:535] accuracy: 0.760800
INFO:tensorflow:accuracy: 0.762900
I0831 09:14:24.695644 140106846488320 run_classifier.py:535] accuracy: 0.762900
INFO:tensorflow:accuracy: 0.757400
I0831 10:07:05.190570 139795207890688 run_classifier.py:535] accuracy: 0.757400
INFO:tensorflow:accuracy: 0.767400
I0831 10:59:03.713218 140145807386368 run_classifier.py:535] accuracy: 0.767400


# char_segmented, vocab=5282
nohup ./comp_bert/char_segmented/scripts/run_classifier_shopping_5282.sh > logs/char_segmented_run_classifier_shopping_5282.log_to_commit &
grep "accuracy: " logs/char_segmented_run_classifier_shopping_5282.log_to_commit (xxx)

(0.9224625, 0.002232116428414979)

# char_segmented, vocab=5282
nohup ./comp_bert/char_segmented/scripts/run_classifier_weibo_5282.sh > logs/char_segmented_run_classifier_weibo_5282.log_to_commit &
grep "accuracy: " logs/char_segmented_run_classifier_weibo_5282.log_to_commit (xxx)

(0.8830333333333333, 0.0009637888196533924)

# char_segmented, vocab=5282
nohup ./comp_bert/char_segmented/scripts/run_classifier_xnli_5282.sh > logs/char_segmented_run_classifier_xnli_5282.log_to_commit &
grep "accuracy: " logs/char_segmented_run_classifier_xnli_5282.log_to_commit (xxx)


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