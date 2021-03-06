

### 准备 zh_wiki

0. char_no_space (保持wiki数据的原有样貌)
    - data_proc/char2char_no_space_mp.sh
    - outputs: ${STORAGE_BUCKET}/data/corpus/char_spaced_lower/zhwiki-latest-pages-articles_${i}_char_spaced_lower.txt

1. char_spaced (中文字与字之间拆开):
    - data_proc/char2char_spaced_mp.sh
    - outputs: ${STORAGE_BUCKET}/data/corpus/char_spaced_lower/zhwiki-latest-pages-articles_${i}_char_spaced_lower.txt

2. char_segmented (中文字与字之间拆开)
    - data_proc/char2char_segmented_mp.sh
    - outputs: ${STORAGE_BUCKET}/data/corpus/char_segmented_lower/zhwiki-latest-pages-articles_${i}_char_segmented_lower.txt

3. 合并文件
    - data_proc/merge_file_utils.py



### 建立词汇表

'''bash

- nohup python3 data_proc/build_vocab_spm.py > build_vocab_0624.log &

'''
    


|  | #vocab=21128 | #vocab=10564 |  #vocab=5282   |
| :----: | :----: | :----: | 
| char_no_space	     |      char_no_space_21128     |   char_no_space_10564      |   
|  char_spaced       |     char_spaced_21128      |   char_spaced_10564    |   
|  char_segmented       |       char_segmented_21128    |     char_segmented_10564       |


```bash
# /home/michaelwzhu91_gmail_com/redesign_vocab_for_zh_bert/data_proc/tokenizers/sentencepiece/char_no_space-10564-clean.model
# /home/michaelwzhu91_gmail_com/redesign_vocab_for_zh_bert/data_proc/tokenizers/sentencepiece/char_no_space-10564-clean.vocab


# /home/michaelwzhu91_gmail_com/redesign_vocab_for_zh_bert/data_proc/tokenizers/sentencepiece/char_no_space-21128-clean.model
# /home/michaelwzhu91_gmail_com/redesign_vocab_for_zh_bert/data_proc/tokenizers/sentencepiece/char_no_space-21128-clean.vocab


```


### 准备预训练 tfrecords

    - max sentence length = 128
    - dupe_factor = 1
    
```bash

# debug
python3 src/char_spaced/create_pretraining_data.py --input_file=datasets/zh_sample/wiki.valid.raw --output_file=experiments/zh_sample/wiki.valid.%s.tfrecord --do_lower_case=True --do_whole_word_mask=True --max_seq_length=128 --max_predictions_per_seq=13 --masked_lm_prob=0.1 --dupe_factor=2 --bert_tokenizer_name data_proc/tokenizers/char_spaced_21128-vocab.txt


# 启动VMs

$ export PROJECT_NAME=subchar-transformers
$ gcloud config set project ${PROJECT_NAME}
$ ctpu up --tpu-size=v2-8 --machine-type=n1-standard-16 --zone=us-central1-f --tf-version=1.15 --name=h-bert-8


# char_spaced, vocab=21128

./src/char_spaced/scripts/create_pretrain_data_21128_1_75.sh
./src/char_spaced/scripts/create_pretrain_data_21128_76_150.sh
./src/char_spaced/scripts/create_pretrain_data_21128_151_218.sh

# char_segmented, vocab=31692

./src/char_segmented/scripts/create_pretrain_data_31692_1_75.sh
./src/char_segmented/scripts/create_pretrain_data_31692_76_150.sh
./src/char_segmented/scripts/create_pretrain_data_31692_151_218.sh

# char_segmented, vocab=21128

./src/char_segmented/scripts/create_pretrain_data_21128_1_75.sh
./src/char_segmented/scripts/create_pretrain_data_21128_76_150.sh
./src/char_segmented/scripts/create_pretrain_data_21128_151_218.sh

# char_segmented, vocab=10564

./src/char_segmented/scripts/create_pretrain_data_10564_1_75.sh
./src/char_segmented/scripts/create_pretrain_data_10564_76_150.sh
./src/char_segmented/scripts/create_pretrain_data_10564_151_218.sh

# char_no_space, vocab=21128

./src/char_no_space/scripts/create_pretrain_data_21128_1_75.sh
./src/char_no_space/scripts/create_pretrain_data_21128_76_150.sh
./src/char_no_space/scripts/create_pretrain_data_21128_151_218.sh


# char_no_space, vocab=10564

./src/char_no_space/scripts/create_pretrain_data_10564_1_75.sh
./src/char_no_space/scripts/create_pretrain_data_10564_76_150.sh
./src/char_no_space/scripts/create_pretrain_data_10564_151_218.sh


```

### 预训练

    - max sentence length = 128
    - dupe_factor = 1
    
```bash

# debug
### run pretrain

# char_segmented, vocab=10564
nohup ./src/char_segmented/scripts/run_pretrain_10564.sh > pretrain_char_segmented_10564.log &

# char_segmented, vocab=21128
nohup ./src/char_segmented/scripts/run_pretrain_21128.sh > pretrain_char_segmented_21128.log &

# char_segmented, vocab=31692
nohup ./src/char_segmented/scripts/run_pretrain_31692.sh > pretrain_char_segmented_31692.log &


# char_spaced, vocab=21128
nohup ./src/char_spaced/scripts/run_pretrain_21128.sh > pretrain_char_spaced_21128.log &


# char_no_space, vocab=21128
nohup ./src/char_no_space/scripts/run_pretrain_21128.sh > pretrain_char_no_space_21128.log &

# char_no_space, vocab=10564
nohup ./src/char_no_space/scripts/run_pretrain_10564.sh > pretrain_char_no_space_10564.log &



```



### finetune


```bash

######################################
# char_no_space, vocab=21128
######################################

# on chn
nohup ./src/char_no_space/scripts/run_classifier_chn_21128.sh > char_no_space_chn_21128.log &

# on book_review
nohup ./src/char_no_space/scripts/run_classifier_book_review_21128.sh > char_no_space_book_review_21128.log &

# on shopping
nohup ./src/char_no_space/scripts/run_classifier_shopping_21128.sh > char_no_space_shopping_21128.log &

# on weibo
nohup ./src/char_no_space/scripts/run_classifier_weibo_21128.sh > char_no_space_weibo_21128.log &


# on lcqmc
nohup ./src/char_no_space/scripts/run_classifier_lcqmc_21128.sh > char_no_space_lcqmc_21128.log &

# on xnli
nohup ./src/char_no_space/scripts/run_classifier_xnli_21128.sh > char_no_space_xnli_21128.log &


# on law_qa
nohup ./src/char_no_space/scripts/run_classifier_law_qa_21128.sh > char_no_space_law_qa_21128.log &

# on nlpcc_dbqa
nohup ./src/char_no_space/scripts/run_classifier_nlpcc_dbqa_21128.sh > char_no_space_nlpcc_dbqa_21128.log &


######################################
# char_segmented, vocab=21128
######################################

# on chn
nohup ./src/char_segmented/scripts/run_classifier_chn_21128.sh > char_segmented_chn_21128.log &

# on book_review
nohup ./src/char_segmented/scripts/run_classifier_book_review_21128.sh > char_segmented_book_review_21128.log &

# on shopping
nohup ./src/char_segmented/scripts/run_classifier_shopping_21128.sh > char_segmented_shopping_21128.log &

# on weibo
nohup ./src/char_segmented/scripts/run_classifier_weibo_21128.sh > char_segmented_weibo_21128.log &

# on lcqmc
nohup ./src/char_segmented/scripts/run_classifier_lcqmc_21128.sh > char_segmented_lcqmc_21128.log &

# on xnli
nohup ./src/char_segmented/scripts/run_classifier_xnli_21128.sh > char_segmented_xnli_21128.log &

# on law_qa
nohup ./src/char_segmented/scripts/run_classifier_law_qa_21128.sh > char_segmented_law_qa_21128.log &

# on nlpcc_dbqa
nohup ./src/char_segmented/scripts/run_classifier_nlpcc_dbqa_21128.sh > char_segmented_nlpcc_dbqa_21128.log &


######################################
# char_segmented, vocab=10564
######################################

# on chn
nohup ./src/char_segmented/scripts/run_classifier_chn_10564.sh > char_segmented_chn_10564.log &

# on book_review
nohup ./src/char_segmented/scripts/run_classifier_book_review_10564.sh > char_segmented_book_review_10564.log &

# on nlpcc_dbqa
nohup ./src/char_segmented/scripts/run_classifier_nlpcc_dbqa_10564.sh > char_segmented_nlpcc_dbqa_10564.log &


######################################
# char_segmented, vocab=31692
######################################

# on chn
nohup ./src/char_segmented/scripts/run_classifier_chn_31692.sh > char_segmented_chn_31692.log &

# on book_review
nohup ./src/char_segmented/scripts/run_classifier_book_review_31692.sh > char_segmented_book_review_31692.log &

# on nlpcc_dbqa
nohup ./src/char_segmented/scripts/run_classifier_nlpcc_dbqa_31692.sh > char_segmented_nlpcc_dbqa_31692.log &



######################################
# char_spaced, vocab=21128
######################################

# on chn
nohup ./src/char_spaced/scripts/run_classifier_chn_21128.sh > char_spaced_chn_21128.log &

# on book_review
nohup ./src/char_spaced/scripts/run_classifier_book_review_21128.sh > char_spaced_book_review_21128.log &

# on shopping
nohup ./src/char_spaced/scripts/run_classifier_shopping_21128.sh > char_spaced_shopping_21128.log &

# on weibo
nohup ./src/char_spaced/scripts/run_classifier_weibo_21128.sh > char_spaced_weibo_21128.log &


# on lcqmc
nohup ./src/char_spaced/scripts/run_classifier_lcqmc_21128.sh > char_spaced_lcqmc_21128.log &

# on xnli
nohup ./src/char_spaced/scripts/run_classifier_xnli_21128.sh > char_spaced_xnli_21128.log &

# on law_qa
nohup ./src/char_spaced/scripts/run_classifier_law_qa_21128.sh > char_spaced_law_qa_21128.log &

# on nlpcc_dbqa
nohup ./src/char_spaced/scripts/run_classifier_nlpcc_dbqa_21128.sh > char_spaced_nlpcc_dbqa_21128.log &







```




### results


```bash

######################################
# char_no_space, vocab=21128
######################################

# on chn
nohup ./src/char_no_space/scripts/run_classifier_chn_21128.sh > char_no_space_chn_21128.log &

I0625 08:34:57.072785 140186398181120 run_classifier.py:535] accuracy: 0.870833
INFO:tensorflow:accuracy: 0.890000
I0625 09:02:00.653930 139887414482688 run_classifier.py:535] accuracy: 0.890000
INFO:tensorflow:accuracy: 0.870833
I0625 09:39:51.633414 140707338786560 run_classifier.py:535] accuracy: 0.870833
INFO:tensorflow:accuracy: 0.890833
I0625 10:18:51.692997 140167771346688 run_classifier.py:535] accuracy: 0.890833
INFO:tensorflow:accuracy: 0.888333
I0625 10:57:51.628335 140701942486784 run_classifier.py:535] accuracy: 0.888333
INFO:tensorflow:accuracy: 0.883333
I0625 11:36:51.682042 140690909275904 run_classifier.py:535] accuracy: 0.883333
INFO:tensorflow:accuracy: 0.890000
I0625 12:15:51.709899 139907844753152 run_classifier.py:535] accuracy: 0.890000
INFO:tensorflow:accuracy: 0.890000
I0625 12:54:51.690732 139650832303872 run_classifier.py:535] accuracy: 0.890000
INFO:tensorflow:accuracy: 0.889167
I0625 13:33:51.643221 140567440525056 run_classifier.py:535] accuracy: 0.889167


# on book_review
nohup ./src/char_no_space/scripts/run_classifier_book_review_21128.sh > char_no_space_book_review_21128.log &

I0627 14:05:23.687632 140514682889984 run_classifier.py:544] accuracy: 0.783500
INFO:tensorflow:accuracy: 0.781100
I0627 14:41:53.192856 139753834088192 run_classifier.py:544] accuracy: 0.781100


# on shopping
nohup ./src/char_no_space/scripts/run_classifier_shopping_21128.sh > char_no_space_shopping_21128.log &

I0627 14:11:03.796394 140247161861888 run_classifier.py:544] accuracy: 0.927500
INFO:tensorflow:accuracy: 0.935900
I0627 14:47:04.182286 140251302438656 run_classifier.py:544] accuracy: 0.935900
INFO:tensorflow:accuracy: 0.931600
I0627 15:23:07.295916 140692436125440 run_classifier.py:544] accuracy: 0.931600
INFO:tensorflow:accuracy: 0.934800
I0627 15:59:08.812093 140663781717760 run_classifier.py:544] accuracy: 0.934800
INFO:tensorflow:accuracy: 0.936100
I0627 16:35:13.572341 140038585972480 run_classifier.py:544] accuracy: 0.936100
INFO:tensorflow:accuracy: 0.931100
I0627 17:13:28.820768 139967690110720 run_classifier.py:544] accuracy: 0.931100
INFO:tensorflow:accuracy: 0.934300
I0627 17:52:28.841369 139652966725376 run_classifier.py:544] accuracy: 0.934300
INFO:tensorflow:accuracy: 0.934700
I0627 18:31:28.356868 140075201926912 run_classifier.py:544] accuracy: 0.934700
INFO:tensorflow:accuracy: 0.932500
I0627 19:10:28.603378 140094287222528 run_classifier.py:544] accuracy: 0.932500
INFO:tensorflow:accuracy: 0.931400
I0627 19:49:28.570019 140170002900736 run_classifier.py:544] accuracy: 0.931400
INFO:tensorflow:accuracy: 0.934800
I0627 20:28:28.651374 139830219233024 run_classifier.py:544] accuracy: 0.934800

# on weibo
nohup ./src/char_no_space/scripts/run_classifier_weibo_21128.sh > char_no_space_weibo_21128.log &

I0627 14:05:36.937934 140623430149888 run_classifier.py:544] accuracy: 0.969900
INFO:tensorflow:accuracy: 0.970400
I0627 14:37:36.086590 140450222708480 run_classifier.py:544] accuracy: 0.970400
INFO:tensorflow:accuracy: 0.971300
I0627 15:08:16.471827 140485892560640 run_classifier.py:544] accuracy: 0.971300
INFO:tensorflow:accuracy: 0.971200
I0627 15:42:52.578143 140210740971264 run_classifier.py:544] accuracy: 0.971200
INFO:tensorflow:accuracy: 0.972000
I0627 16:21:52.730109 140135472842496 run_classifier.py:544] accuracy: 0.972000
INFO:tensorflow:accuracy: 0.971400
I0627 17:00:51.577145 140533658928896 run_classifier.py:544] accuracy: 0.971400
INFO:tensorflow:accuracy: 0.971300
I0627 17:39:52.428884 140460927371008 run_classifier.py:544] accuracy: 0.971300
INFO:tensorflow:accuracy: 0.972000
I0627 18:18:52.231157 140542168372992 run_classifier.py:544] accuracy: 0.972000
INFO:tensorflow:accuracy: 0.971700
I0627 18:57:52.039505 140485660763904 run_classifier.py:544] accuracy: 0.971700
INFO:tensorflow:accuracy: 0.971400
I0627 19:36:52.702689 139783719491328 run_classifier.py:544] accuracy: 0.971400
INFO:tensorflow:accuracy: 0.971300
I0627 20:15:52.076200 140543185344256 run_classifier.py:544] accuracy: 0.971300

# on lcqmc
nohup ./src/char_no_space/scripts/run_classifier_lcqmc_21128.sh > char_no_space_lcqmc_21128.log &

I0625 08:57:35.222099 139759991002880 run_classifier.py:535] accuracy: 0.800480
INFO:tensorflow:accuracy: 0.791040
I0625 09:32:40.882872 140551859885824 run_classifier.py:535] accuracy: 0.791040
INFO:tensorflow:accuracy: 0.787200
I0625 10:07:35.781635 140572554417920 run_classifier.py:535] accuracy: 0.787200
INFO:tensorflow:accuracy: 0.790000
I0625 10:43:13.702753 139680034756352 run_classifier.py:535] accuracy: 0.790000
INFO:tensorflow:accuracy: 0.794880
I0625 11:17:54.807642 140256508110592 run_classifier.py:535] accuracy: 0.794880
INFO:tensorflow:accuracy: 0.795120
I0625 11:52:42.480173 139899870062336 run_classifier.py:535] accuracy: 0.795120
INFO:tensorflow:accuracy: 0.789760
I0625 12:27:38.878863 139919720097536 run_classifier.py:535] accuracy: 0.789760
INFO:tensorflow:accuracy: 0.796160
I0625 13:02:26.042905 140708189382400 run_classifier.py:535] accuracy: 0.796160
INFO:tensorflow:accuracy: 0.789200
I0625 13:38:16.225615 140466079901440 run_classifier.py:535] accuracy: 0.789200
INFO:tensorflow:accuracy: 0.802720
I0625 14:13:22.289383 139683859838720 run_classifier.py:535] accuracy: 0.802720
INFO:tensorflow:accuracy: 0.797440
I0625 14:48:53.349266 139934904473344 run_classifier.py:535] accuracy: 0.797440

# on xnli
nohup ./src/char_no_space/scripts/run_classifier_xnli_21128.sh > char_no_space_xnli_21128.log &

I0625 09:17:50.684335 140132312758016 run_classifier.py:535] accuracy: 0.606786
INFO:tensorflow:accuracy: 0.595409
I0625 10:12:00.395455 140323901515520 run_classifier.py:535] accuracy: 0.595409
INFO:tensorflow:accuracy: 0.597405
I0625 11:05:54.806347 140470934234880 run_classifier.py:535] accuracy: 0.597405
INFO:tensorflow:accuracy: 0.595409
I0625 11:59:54.126637 139934138722048 run_classifier.py:535] accuracy: 0.595409
INFO:tensorflow:accuracy: 0.594411
I0625 12:53:59.015857 140275322590976 run_classifier.py:535] accuracy: 0.594411
INFO:tensorflow:accuracy: 0.601996
I0625 13:48:44.908273 140242032445184 run_classifier.py:535] accuracy: 0.601996
INFO:tensorflow:accuracy: 0.595808
I0625 14:45:43.144626 139981879277312 run_classifier.py:535] accuracy: 0.595808
INFO:tensorflow:accuracy: 0.591617
I0625 15:42:31.669061 140613053298432 run_classifier.py:535] accuracy: 0.591617
INFO:tensorflow:accuracy: 0.592016
I0625 16:37:07.936761 140422334502656 run_classifier.py:535] accuracy: 0.592016
INFO:tensorflow:accuracy: 0.586826
I0625 17:31:53.777163 140227519424256 run_classifier.py:535] accuracy: 0.586826
INFO:tensorflow:accuracy: 0.592216
I0625 18:28:50.720183 140089922041600 run_classifier.py:535] accuracy: 0.592216

# on law_qa
nohup ./src/char_no_space/scripts/run_classifier_law_qa_21128.sh > char_no_space_law_qa_21128.log &

I0627 14:04:25.634783 139762074269440 run_classifier.py:544] accuracy: 0.848251
INFO:tensorflow:accuracy: 0.850454
I0627 14:43:25.510234 139936190932736 run_classifier.py:544] accuracy: 0.850454
INFO:tensorflow:accuracy: 0.856238
I0627 15:22:25.677923 140587721942784 run_classifier.py:544] accuracy: 0.856238
INFO:tensorflow:accuracy: 0.854035
I0627 16:01:25.458806 140045263140608 run_classifier.py:544] accuracy: 0.854035
INFO:tensorflow:accuracy: 0.858717
I0627 16:40:25.694281 139732792604416 run_classifier.py:544] accuracy: 0.858717
INFO:tensorflow:accuracy: 0.858166
I0627 17:19:25.380357 140004155852544 run_classifier.py:544] accuracy: 0.858166
INFO:tensorflow:accuracy: 0.845222
I0627 17:58:25.484821 139622408111872 run_classifier.py:544] accuracy: 0.845222
INFO:tensorflow:accuracy: 0.852933
I0627 18:37:25.946979 139674845009664 run_classifier.py:544] accuracy: 0.852933
INFO:tensorflow:accuracy: 0.853759
I0627 19:16:25.637765 140123282474752 run_classifier.py:544] accuracy: 0.853759
INFO:tensorflow:accuracy: 0.862848
I0627 19:55:25.756171 139998535964416 run_classifier.py:544] accuracy: 0.862848
INFO:tensorflow:accuracy: 0.851281
I0627 20:34:25.598933 140418457687808 run_classifier.py:544] accuracy: 0.851281


# on nlpcc_dbqa
nohup ./src/char_no_space/scripts/run_classifier_nlpcc_dbqa_21128.sh > char_no_space_nlpcc_dbqa_21128.log &

grep "'weighted avg'" char_no_space_nlpcc_dbqa_21128.log

* macro avg

0.5610755928059543
0.5437964261157965
0.5740917350960472
0.5431556863531445
0.5469877876150465
0.5509554357702582
0.54869186735131
0.5510971301622875
0.5476722596692032
0.5525761402539562
0.578442021898753


######################################
# char_segmented, vocab=21128
######################################

# on chn
nohup ./src/char_segmented/scripts/run_classifier_chn_21128.sh > char_segmented_chn_21128.log &

I0625 08:58:25.863686 140174344152832 run_classifier.py:535] accuracy: 0.896667
INFO:tensorflow:accuracy: 0.904167
I0625 09:25:40.947104 140340012877568 run_classifier.py:535] accuracy: 0.904167
INFO:tensorflow:accuracy: 0.883333
I0625 09:59:33.081110 139710519240448 run_classifier.py:535] accuracy: 0.883333
INFO:tensorflow:accuracy: 0.895000
I0625 10:38:32.765349 140058235381504 run_classifier.py:535] accuracy: 0.895000
INFO:tensorflow:accuracy: 0.890833
I0625 11:17:32.490834 139808439076608 run_classifier.py:535] accuracy: 0.890833
INFO:tensorflow:accuracy: 0.894167
I0625 11:56:32.701845 140309810296576 run_classifier.py:535] accuracy: 0.894167
INFO:tensorflow:accuracy: 0.893333
I0625 12:35:32.735002 140173993477888 run_classifier.py:535] accuracy: 0.893333
INFO:tensorflow:accuracy: 0.898333
I0625 13:14:32.742059 140705761072896 run_classifier.py:535] accuracy: 0.898333
INFO:tensorflow:accuracy: 0.894167
I0625 13:55:16.821156 140158698764032 run_classifier.py:535] accuracy: 0.894167


# on book_review
nohup ./src/char_segmented/scripts/run_classifier_book_review_21128.sh > char_segmented_book_review_21128.log &

I0626 16:34:09.458597 140223559988992 run_classifier.py:539] accuracy: 0.786900
INFO:tensorflow:accuracy: 0.785100
I0626 17:10:57.989873 139780732901120 run_classifier.py:542] accuracy: 0.785100
INFO:tensorflow:accuracy: 0.781600
I0626 17:47:48.164272 139988952721152 run_classifier.py:542] accuracy: 0.781600
INFO:tensorflow:accuracy: 0.784500
I0626 18:24:38.965309 140535196116736 run_classifier.py:544] accuracy: 0.784500
INFO:tensorflow:accuracy: 0.788100
I0626 19:02:05.461433 140122663479040 run_classifier.py:544] accuracy: 0.788100
INFO:tensorflow:accuracy: 0.784900
I0626 19:41:05.318490 140520895993600 run_classifier.py:544] accuracy: 0.784900
INFO:tensorflow:accuracy: 0.788300
I0626 20:20:05.502975 140582523287296 run_classifier.py:544] accuracy: 0.788300
INFO:tensorflow:accuracy: 0.785700
I0626 20:59:05.209247 140191005640448 run_classifier.py:544] accuracy: 0.785700
INFO:tensorflow:accuracy: 0.781400
I0626 21:38:04.974490 139811833816832 run_classifier.py:544] accuracy: 0.781400
INFO:tensorflow:accuracy: 0.789400
I0626 22:17:05.002029 140329493042944 run_classifier.py:544] accuracy: 0.789400
INFO:tensorflow:accuracy: 0.786100
I0626 22:56:05.026485 140666603480832 run_classifier.py:544] accuracy: 0.786100

# on shopping
nohup ./src/char_segmented/scripts/run_classifier_shopping_21128.sh > char_segmented_shopping_21128.log &

I0626 16:42:45.014677 139706451801856 run_classifier.py:539] accuracy: 0.937200
INFO:tensorflow:accuracy: 0.937000
I0626 17:19:13.610166 140331727755008 run_classifier.py:542] accuracy: 0.937000
INFO:tensorflow:accuracy: 0.934000
I0626 17:56:28.484545 139797409773312 run_classifier.py:542] accuracy: 0.934000
INFO:tensorflow:accuracy: 0.935900
I0626 18:33:04.879758 139623253673728 run_classifier.py:544] accuracy: 0.935900
INFO:tensorflow:accuracy: 0.934000
I0626 19:11:45.017466 140204922074880 run_classifier.py:544] accuracy: 0.934000
INFO:tensorflow:accuracy: 0.931600
I0626 19:50:45.251961 140145401206528 run_classifier.py:544] accuracy: 0.931600
INFO:tensorflow:accuracy: 0.932600
I0626 20:29:45.227342 139898683111168 run_classifier.py:544] accuracy: 0.932600
INFO:tensorflow:accuracy: 0.931700
I0626 21:08:45.164308 139772613547776 run_classifier.py:544] accuracy: 0.931700
INFO:tensorflow:accuracy: 0.935100
I0626 21:47:44.975813 140304445880064 run_classifier.py:544] accuracy: 0.935100
INFO:tensorflow:accuracy: 0.938100
I0626 22:26:45.143396 140700736444160 run_classifier.py:544] accuracy: 0.938100
INFO:tensorflow:accuracy: 0.933100
I0626 23:05:44.918116 140676097095424 run_classifier.py:544] accuracy: 0.933100


# on weibo
nohup ./src/char_segmented/scripts/run_classifier_weibo_21128.sh > char_segmented_weibo_21128.log &

I0626 17:18:29.324935 139830247569152 run_classifier.py:542] accuracy: 0.971900
INFO:tensorflow:accuracy: 0.970300
I0626 17:50:52.481071 140180149032704 run_classifier.py:542] accuracy: 0.970300
INFO:tensorflow:accuracy: 0.971600
I0626 18:23:02.270341 140201233737472 run_classifier.py:544] accuracy: 0.971600
INFO:tensorflow:accuracy: 0.970900
I0626 18:57:20.596820 139820237289216 run_classifier.py:544] accuracy: 0.970900
INFO:tensorflow:accuracy: 0.971200
I0626 19:36:20.998445 140494269212416 run_classifier.py:544] accuracy: 0.971200
INFO:tensorflow:accuracy: 0.972900
I0626 20:15:21.164277 140454088382208 run_classifier.py:544] accuracy: 0.972900
INFO:tensorflow:accuracy: 0.970600
I0626 20:54:20.516360 140164919486208 run_classifier.py:544] accuracy: 0.970600
INFO:tensorflow:accuracy: 0.972000
I0626 21:33:20.694598 139799362733824 run_classifier.py:544] accuracy: 0.972000
INFO:tensorflow:accuracy: 0.970200
I0626 22:12:20.208873 140338539292416 run_classifier.py:544] accuracy: 0.970200
INFO:tensorflow:accuracy: 0.971700
I0626 22:51:23.147711 140070196573952 run_classifier.py:544] accuracy: 0.971700
INFO:tensorflow:accuracy: 0.971800
I0626 23:30:21.088183 139825327044352 run_classifier.py:544] accuracy: 0.971800

# on lcqmc
nohup ./src/char_segmented/scripts/run_classifier_lcqmc_21128.sh > char_segmented_lcqmc_21128.log &


I0625 14:45:49.595400 140195560449792 run_classifier.py:535] accuracy: 0.820640
INFO:tensorflow:accuracy: 0.821520
I0625 15:49:53.077821 139712619656960 run_classifier.py:535] accuracy: 0.821520
INFO:tensorflow:accuracy: 0.807120
I0625 16:51:38.151077 140593971283712 run_classifier.py:535] accuracy: 0.807120
INFO:tensorflow:accuracy: 0.814240
I0625 17:55:11.204228 140348063557376 run_classifier.py:535] accuracy: 0.814240
INFO:tensorflow:accuracy: 0.823120
I0625 18:57:00.029197 140514801723136 run_classifier.py:535] accuracy: 0.823120
INFO:tensorflow:accuracy: 0.825760
I0625 19:58:00.269811 140181441361664 run_classifier.py:535] accuracy: 0.825760
INFO:tensorflow:accuracy: 0.817840
I0625 20:59:17.209644 140542805874432 run_classifier.py:535] accuracy: 0.817840
INFO:tensorflow:accuracy: 0.813760
I0625 22:01:25.233415 140486236055296 run_classifier.py:535] accuracy: 0.813760
INFO:tensorflow:accuracy: 0.815280
I0625 23:05:06.251900 140161596344064 run_classifier.py:535] accuracy: 0.815280
INFO:tensorflow:accuracy: 0.825520
I0626 00:06:51.560539 140067961165568 run_classifier.py:535] accuracy: 0.825520
INFO:tensorflow:accuracy: 0.812160
I0626 01:08:32.903674 140557941769984 run_classifier.py:535] accuracy: 0.812160


# on xnli
nohup ./src/char_segmented/scripts/run_classifier_xnli_21128.sh > char_segmented_xnli_21128.log &

I0625 15:17:19.600876 140490938377984 run_classifier.py:535] accuracy: 0.612176
INFO:tensorflow:accuracy: 0.619162
I0625 16:47:08.541044 139900143146752 run_classifier.py:535] accuracy: 0.619162
INFO:tensorflow:accuracy: 0.624152
I0625 18:18:25.365472 139965689779968 run_classifier.py:535] accuracy: 0.624152
INFO:tensorflow:accuracy: 0.613772
I0625 19:48:30.910618 140621511526144 run_classifier.py:535] accuracy: 0.613772
INFO:tensorflow:accuracy: 0.616766
I0625 21:18:32.037894 140661901244160 run_classifier.py:535] accuracy: 0.616766
INFO:tensorflow:accuracy: 0.625150
I0625 22:48:05.097165 140624661415680 run_classifier.py:535] accuracy: 0.625150
INFO:tensorflow:accuracy: 0.619760
I0626 00:18:04.560271 140427712444160 run_classifier.py:535] accuracy: 0.619760
INFO:tensorflow:accuracy: 0.621956
I0626 01:48:17.036787 140084187600640 run_classifier.py:535] accuracy: 0.621956
INFO:tensorflow:accuracy: 0.625150
I0626 03:17:39.121293 140616046860032 run_classifier.py:535] accuracy: 0.625150
INFO:tensorflow:accuracy: 0.613772
I0626 04:46:57.572167 139894134437632 run_classifier.py:535] accuracy: 0.613772
INFO:tensorflow:accuracy: 0.621956
I0626 06:16:46.509672 140178131744512 run_classifier.py:535] accuracy: 0.621956


# on law_qa
nohup ./src/char_segmented/scripts/run_classifier_law_qa_21128.sh > char_segmented_law_qa_21128.log &


I0626 19:04:44.454269 140113567323904 run_classifier.py:545] accuracy: 0.855412
INFO:tensorflow:accuracy: 0.854310
I0626 19:39:17.974401 140023656277760 run_classifier.py:545] accuracy: 0.854310
INFO:tensorflow:accuracy: 0.859543
I0626 20:14:33.460065 140717547841280 run_classifier.py:545] accuracy: 0.859543
INFO:tensorflow:accuracy: 0.849628
I0626 20:51:08.859391 140203611109120 run_classifier.py:545] accuracy: 0.849628
INFO:tensorflow:accuracy: 0.866979
I0626 21:27:52.586356 140095502542592 run_classifier.py:545] accuracy: 0.866979
INFO:tensorflow:accuracy: 0.860644
I0626 22:03:23.567004 139854162118400 run_classifier.py:545] accuracy: 0.860644
INFO:tensorflow:accuracy: 0.863674
I0626 23:19:01.057456 139742752724736 run_classifier.py:545] accuracy: 0.863674
INFO:tensorflow:accuracy: 0.856789
I0626 23:57:54.602181 139915018958592 run_classifier.py:545] accuracy: 0.856789
INFO:tensorflow:accuracy: 0.858717
I0627 00:37:01.458080 140547782862592 run_classifier.py:545] accuracy: 0.858717
INFO:tensorflow:accuracy: 0.854586
I0627 01:15:56.111657 139795924260608 run_classifier.py:545] accuracy: 0.854586


# on nlpcc_dbqa
nohup ./src/char_segmented/scripts/run_classifier_nlpcc_dbqa_21128.sh > char_segmented_nlpcc_dbqa_21128.log &

* macro avg f1
0.7110703717821407
0.7158790871797146
0.668946790284818
0.638946790284818
0.6539240826051832
0.6401362756635662
0.6626274820884439
0.6805668845806947


######################################
# char_segmented, vocab=10564
######################################

# on chn
nohup ./src/char_segmented/scripts/run_classifier_chn_10564.sh > char_segmented_chn_10564.log &

I0627 15:28:42.623456 140285393336064 run_classifier.py:544] accuracy: 0.900000
INFO:tensorflow:accuracy: 0.895000
I0627 16:01:34.262805 139774384129792 run_classifier.py:544] accuracy: 0.895000
INFO:tensorflow:accuracy: 0.890833
I0627 16:35:10.891569 139713118324480 run_classifier.py:544] accuracy: 0.890833
INFO:tensorflow:accuracy: 0.893333
I0627 17:08:16.479279 139851673409280 run_classifier.py:544] accuracy: 0.893333
INFO:tensorflow:accuracy: 0.884167
I0627 17:46:06.969177 139917025822464 run_classifier.py:544] accuracy: 0.884167
INFO:tensorflow:accuracy: 0.895000
I0627 18:25:07.307997 140354503591680 run_classifier.py:544] accuracy: 0.895000
INFO:tensorflow:accuracy: 0.902500
I0627 19:04:05.565606 140414964172544 run_classifier.py:544] accuracy: 0.902500
INFO:tensorflow:accuracy: 0.883333
I0627 19:43:05.026529 140071632992000 run_classifier.py:544] accuracy: 0.883333
INFO:tensorflow:accuracy: 0.883333
I0627 20:22:06.857652 140318162622208 run_classifier.py:544] accuracy: 0.883333
INFO:tensorflow:accuracy: 0.901667
I0627 21:01:05.713776 140413694879488 run_classifier.py:544] accuracy: 0.901667
INFO:tensorflow:accuracy: 0.888333
I0627 21:40:05.793964 140221530199808 run_classifier.py:544] accuracy: 0.888333


# on book_review
nohup ./src/char_segmented/scripts/run_classifier_book_review_10564.sh > char_segmented_book_review_10564.log &

I0627 15:04:10.378492 140159645439744 run_classifier.py:544] accuracy: 0.779500
INFO:tensorflow:accuracy: 0.778600
I0627 16:03:22.102826 139688184698624 run_classifier.py:544] accuracy: 0.778600
INFO:tensorflow:accuracy: 0.776400
I0627 17:03:54.857486 140226910689024 run_classifier.py:544] accuracy: 0.776400
INFO:tensorflow:accuracy: 0.782600
I0627 18:04:04.683559 140294636017408 run_classifier.py:544] accuracy: 0.782600
INFO:tensorflow:accuracy: 0.785300
I0627 19:03:55.854121 140530756429568 run_classifier.py:544] accuracy: 0.785300
INFO:tensorflow:accuracy: 0.781200
I0627 20:03:47.087578 139839796700928 run_classifier.py:544] accuracy: 0.781200
INFO:tensorflow:accuracy: 0.780000
I0627 21:03:00.472827 140248503088896 run_classifier.py:544] accuracy: 0.780000
INFO:tensorflow:accuracy: 0.779800
I0627 22:02:33.949743 140488191309568 run_classifier.py:544] accuracy: 0.779800
INFO:tensorflow:accuracy: 0.789200
I0627 23:01:35.105038 139972090660608 run_classifier.py:544] accuracy: 0.789200
INFO:tensorflow:accuracy: 0.784400
I0628 00:03:41.141481 139982385362688 run_classifier.py:544] accuracy: 0.784400
INFO:tensorflow:accuracy: 0.776800
I0628 01:02:14.181799 139797458536192 run_classifier.py:544] accuracy: 0.776800

# on nlpcc_dbqa
nohup ./src/char_segmented/scripts/run_classifier_nlpcc_dbqa_10564.sh > char_segmented_nlpcc_dbqa_10564.log &

grep "weighted avg" char_segmented_nlpcc_dbqa_10564.log

* macro avg f1

0.655767072282652
0.6493078255075954
0.6100314295553507
0.6525184299542839




######################################
# char_segmented, vocab=31692
######################################

# on chn
nohup ./src/char_segmented/scripts/run_classifier_chn_31692.sh > char_segmented_chn_31692.log &

I0627 14:40:40.893581 140190218352384 run_classifier.py:544] accuracy: 0.890000
INFO:tensorflow:accuracy: 0.895833
I0627 15:14:20.189674 140335415895808 run_classifier.py:544] accuracy: 0.895833
INFO:tensorflow:accuracy: 0.895000
I0627 15:47:50.767106 140012586780416 run_classifier.py:544] accuracy: 0.895000
INFO:tensorflow:accuracy: 0.885000
I0627 16:21:01.652197 140065717708544 run_classifier.py:544] accuracy: 0.885000
INFO:tensorflow:accuracy: 0.900000
I0627 16:58:55.962467 140601998886656 run_classifier.py:544] accuracy: 0.900000
INFO:tensorflow:accuracy: 0.911667
I0627 17:37:56.110481 140524775122688 run_classifier.py:544] accuracy: 0.911667
INFO:tensorflow:accuracy: 0.902500
I0627 18:16:56.618967 140018564093696 run_classifier.py:544] accuracy: 0.902500
INFO:tensorflow:accuracy: 0.901667
I0627 18:55:56.748795 140510751565568 run_classifier.py:544] accuracy: 0.901667
INFO:tensorflow:accuracy: 0.893333
I0627 19:34:56.797709 139662073030400 run_classifier.py:544] accuracy: 0.893333
INFO:tensorflow:accuracy: 0.892500
I0627 20:13:57.973125 140169445930752 run_classifier.py:544] accuracy: 0.892500
INFO:tensorflow:accuracy: 0.904167
I0627 20:52:56.755581 140191734798080 run_classifier.py:544] accuracy: 0.904167

# on book_review
nohup ./src/char_segmented/scripts/run_classifier_book_review_31692.sh > char_segmented_book_review_31692.log &

I0627 15:08:23.549530 139815454402304 run_classifier.py:544] accuracy: 0.792500
INFO:tensorflow:accuracy: 0.783200
I0627 16:08:57.264279 139990266271488 run_classifier.py:544] accuracy: 0.783200
INFO:tensorflow:accuracy: 0.788900
I0627 17:08:54.024188 140303199041280 run_classifier.py:544] accuracy: 0.788900
INFO:tensorflow:accuracy: 0.781600
I0627 18:08:45.340214 139982612621056 run_classifier.py:544] accuracy: 0.781600
INFO:tensorflow:accuracy: 0.787400
I0627 19:08:15.143123 140703319348992 run_classifier.py:544] accuracy: 0.787400
INFO:tensorflow:accuracy: 0.793400
I0627 20:09:33.201308 140260118611712 run_classifier.py:544] accuracy: 0.793400
INFO:tensorflow:accuracy: 0.785800
I0627 21:10:20.403388 139710741100288 run_classifier.py:544] accuracy: 0.785800
INFO:tensorflow:accuracy: 0.780500
I0627 22:09:58.633494 140280271128320 run_classifier.py:544] accuracy: 0.780500
INFO:tensorflow:accuracy: 0.786600
I0627 23:09:19.557101 140636684560128 run_classifier.py:544] accuracy: 0.786600
INFO:tensorflow:accuracy: 0.787600
I0628 00:09:56.246774 140312171026176 run_classifier.py:544] accuracy: 0.787600
INFO:tensorflow:accuracy: 0.786700
I0628 01:10:26.672925 139946796328704 run_classifier.py:544] accuracy: 0.786700

# on nlpcc_dbqa
nohup ./src/char_segmented/scripts/run_classifier_nlpcc_dbqa_31692.sh > char_segmented_nlpcc_dbqa_31692.log &

grep "'weighted avg'" char_segmented_nlpcc_dbqa_31692.log

0.6447832867529677
0.6435315633687011
0.6490856157500807



######################################
# char_spaced, vocab=21128
######################################

# on chn
nohup ./src/char_spaced/scripts/run_classifier_chn_21128.sh > char_spaced_chn_21128.log &

I0625 14:12:59.441497 139799922214656 run_classifier.py:535] accuracy: 0.886667
INFO:tensorflow:accuracy: 0.889167
I0625 14:46:37.380629 140216368776960 run_classifier.py:535] accuracy: 0.889167
INFO:tensorflow:accuracy: 0.881667
I0625 15:20:04.865940 140557377472256 run_classifier.py:535] accuracy: 0.881667
INFO:tensorflow:accuracy: 0.885000
I0625 15:53:49.025910 140003048650496 run_classifier.py:535] accuracy: 0.885000
INFO:tensorflow:accuracy: 0.887500
I0625 16:31:32.878565 140119954544384 run_classifier.py:535] accuracy: 0.887500
INFO:tensorflow:accuracy: 0.882500
I0625 17:10:33.882998 139832593098496 run_classifier.py:535] accuracy: 0.882500
INFO:tensorflow:accuracy: 0.875833
I0625 17:49:31.970525 139939757262592 run_classifier.py:535] accuracy: 0.875833
INFO:tensorflow:accuracy: 0.888333
I0625 18:28:33.083540 139630640600832 run_classifier.py:535] accuracy: 0.888333
INFO:tensorflow:accuracy: 0.886667
I0625 19:07:33.063277 140618574092032 run_classifier.py:535] accuracy: 0.886667
INFO:tensorflow:accuracy: 0.891667
I0625 19:46:32.624346 140349633349376 run_classifier.py:535] accuracy: 0.891667
INFO:tensorflow:accuracy: 0.884167
I0625 20:25:32.652000 139773329577728 run_classifier.py:535] accuracy: 0.884167


# on book_review
nohup ./src/char_spaced/scripts/run_classifier_book_review_21128.sh > char_spaced_book_review_21128.log &

I0626 19:02:30.576723 139928236152576 run_classifier.py:541] accuracy: 0.788600
INFO:tensorflow:accuracy: 0.777800
I0626 19:55:45.939733 140455630616320 run_classifier.py:545] accuracy: 0.777800
INFO:tensorflow:accuracy: 0.781200
I0626 20:49:19.753121 140656131352320 run_classifier.py:545] accuracy: 0.781200
INFO:tensorflow:accuracy: 0.779400
I0626 21:42:44.208271 139797249730304 run_classifier.py:545] accuracy: 0.779400
INFO:tensorflow:accuracy: 0.787100
I0626 22:37:36.597840 139697417254656 run_classifier.py:545] accuracy: 0.787100
INFO:tensorflow:accuracy: 0.783700
I0626 23:33:13.833997 140276409448192 run_classifier.py:545] accuracy: 0.783700
INFO:tensorflow:accuracy: 0.784100
I0627 00:27:47.317484 139807284107008 run_classifier.py:545] accuracy: 0.784100
INFO:tensorflow:accuracy: 0.780500
I0627 01:23:38.773835 140610549257984 run_classifier.py:545] accuracy: 0.780500
INFO:tensorflow:accuracy: 0.779100
I0627 02:18:35.160511 140530184636160 run_classifier.py:545] accuracy: 0.779100
INFO:tensorflow:accuracy: 0.777000
I0627 03:12:46.204100 140548202546944 run_classifier.py:545] accuracy: 0.777000
INFO:tensorflow:accuracy: 0.779100
I0627 04:07:47.952792 139772749129472 run_classifier.py:545] accuracy: 0.779100


# on shopping
nohup ./src/char_spaced/scripts/run_classifier_shopping_21128.sh > char_spaced_shopping_21128.log &

I0626 19:07:52.003728 140147919939328 run_classifier.py:541] accuracy: 0.928600
INFO:tensorflow:accuracy: 0.933200
I0626 20:01:27.113018 139889509963520 run_classifier.py:545] accuracy: 0.933200
INFO:tensorflow:accuracy: 0.931700
I0626 20:54:35.009366 140249643308800 run_classifier.py:545] accuracy: 0.931700
INFO:tensorflow:accuracy: 0.930600
I0626 21:49:42.477229 139942298560256 run_classifier.py:545] accuracy: 0.930600
INFO:tensorflow:accuracy: 0.931400
I0626 22:44:41.548982 139732325525248 run_classifier.py:545] accuracy: 0.931400
INFO:tensorflow:accuracy: 0.929400
I0626 23:39:30.824568 139688776468224 run_classifier.py:545] accuracy: 0.929400
INFO:tensorflow:accuracy: 0.929000
I0627 00:35:51.513256 140282383120128 run_classifier.py:545] accuracy: 0.929000
INFO:tensorflow:accuracy: 0.933300
I0627 01:30:42.341514 140081729402624 run_classifier.py:545] accuracy: 0.933300
INFO:tensorflow:accuracy: 0.929800
I0627 02:24:39.133209 140334722033408 run_classifier.py:545] accuracy: 0.929800
INFO:tensorflow:accuracy: 0.935600
I0627 03:18:46.200610 140257712305920 run_classifier.py:545] accuracy: 0.935600
INFO:tensorflow:accuracy: 0.927300
I0627 04:14:33.316837 140225034270464 run_classifier.py:545] accuracy: 0.927300


# on weibo
nohup ./src/char_spaced/scripts/run_classifier_weibo_21128.sh > char_spaced_weibo_21128.log &

I0626 19:11:22.180476 140526216247040 run_classifier.py:541] accuracy: 0.969200
INFO:tensorflow:accuracy: 0.968800
I0626 20:04:59.522454 139892373481216 run_classifier.py:545] accuracy: 0.968800
INFO:tensorflow:accuracy: 0.971100
I0626 20:57:41.396372 140283771266816 run_classifier.py:545] accuracy: 0.971100
INFO:tensorflow:accuracy: 0.969700
I0626 21:52:27.023586 139895317055232 run_classifier.py:545] accuracy: 0.969700
INFO:tensorflow:accuracy: 0.971100
I0626 22:49:07.047807 140175750166272 run_classifier.py:545] accuracy: 0.971100
INFO:tensorflow:accuracy: 0.969400
I0626 23:43:45.225913 140530740795136 run_classifier.py:545] accuracy: 0.969400
INFO:tensorflow:accuracy: 0.970800
I0627 00:37:51.003207 140478436607744 run_classifier.py:545] accuracy: 0.970800
INFO:tensorflow:accuracy: 0.968800
I0627 01:32:28.450074 139696432916224 run_classifier.py:545] accuracy: 0.968800
INFO:tensorflow:accuracy: 0.971300
I0627 02:26:11.890143 140017755899648 run_classifier.py:545] accuracy: 0.971300
INFO:tensorflow:accuracy: 0.970600
I0627 03:18:52.936230 140684947420928 run_classifier.py:545] accuracy: 0.970600
INFO:tensorflow:accuracy: 0.971200
I0627 04:11:55.544014 140185865148160 run_classifier.py:545] accuracy: 0.971200

# on lcqmc
nohup ./src/char_spaced/scripts/run_classifier_lcqmc_21128.sh > char_spaced_lcqmc_21128.log &

I0625 09:09:37.295477 140275260217088 run_classifier.py:535] accuracy: 0.804480
INFO:tensorflow:accuracy: 0.816480
I0625 09:44:58.446396 140099488716544 run_classifier.py:535] accuracy: 0.816480
INFO:tensorflow:accuracy: 0.806400
I0625 10:20:31.595667 139835475322624 run_classifier.py:535] accuracy: 0.806400
INFO:tensorflow:accuracy: 0.811520
I0625 10:55:52.987402 140310448822016 run_classifier.py:535] accuracy: 0.811520
INFO:tensorflow:accuracy: 0.809440
I0625 11:31:39.313083 140650658879232 run_classifier.py:535] accuracy: 0.809440
INFO:tensorflow:accuracy: 0.807600
I0625 12:08:45.753945 140355089905408 run_classifier.py:535] accuracy: 0.807600
INFO:tensorflow:accuracy: 0.805520
I0625 12:44:26.540078 140576462640896 run_classifier.py:535] accuracy: 0.805520
INFO:tensorflow:accuracy: 0.795680
I0625 13:20:13.292735 140605406238464 run_classifier.py:535] accuracy: 0.795680
INFO:tensorflow:accuracy: 0.811200
I0625 13:56:27.592695 140382787372800 run_classifier.py:535] accuracy: 0.811200
INFO:tensorflow:accuracy: 0.814720
I0625 14:32:00.044955 140380944635648 run_classifier.py:535] accuracy: 0.814720
INFO:tensorflow:accuracy: 0.813680
I0625 15:09:34.755544 139799816853248 run_classifier.py:535] accuracy: 0.813680


# on xnli
nohup ./src/char_spaced/scripts/run_classifier_xnli_21128.sh > char_spaced_xnli_21128.log &

I0625 10:02:45.280204 139729098888960 run_classifier.py:535] accuracy: 0.597804
INFO:tensorflow:accuracy: 0.609980
I0625 11:32:07.780232 140705068947200 run_classifier.py:535] accuracy: 0.609980
INFO:tensorflow:accuracy: 0.614970
I0625 13:02:12.961430 140336102856448 run_classifier.py:535] accuracy: 0.614970
INFO:tensorflow:accuracy: 0.608184
I0625 14:32:03.184250 140378091616000 run_classifier.py:535] accuracy: 0.608184
INFO:tensorflow:accuracy: 0.606986
I0625 16:03:10.273684 139969135384320 run_classifier.py:535] accuracy: 0.606986
INFO:tensorflow:accuracy: 0.604990
I0625 17:31:47.357995 140090601514752 run_classifier.py:535] accuracy: 0.604990
INFO:tensorflow:accuracy: 0.609780
I0625 19:02:57.075620 140502969456384 run_classifier.py:535] accuracy: 0.609780
INFO:tensorflow:accuracy: 0.607186
I0625 20:31:52.357685 140328398190336 run_classifier.py:535] accuracy: 0.607186
INFO:tensorflow:accuracy: 0.604391
I0625 22:00:16.183439 139656243328768 run_classifier.py:535] accuracy: 0.604391
INFO:tensorflow:accuracy: 0.600998
I0625 23:31:01.611439 140616977094400 run_classifier.py:535] accuracy: 0.600998
INFO:tensorflow:accuracy: 0.608583
I0626 00:59:22.489453 140673256810240 run_classifier.py:535] accuracy: 0.608583


# on law_qa
nohup ./src/char_spaced/scripts/run_classifier_law_qa_21128.sh > char_spaced_law_qa_21128.log &

I0627 07:44:09.768380 140144534927104 run_classifier.py:544] accuracy: 0.849077
INFO:tensorflow:accuracy: 0.857890
I0627 08:12:32.868910 139693480359680 run_classifier.py:544] accuracy: 0.857890
INFO:tensorflow:accuracy: 0.857064
I0627 08:51:33.289990 140656823428864 run_classifier.py:544] accuracy: 0.857064
INFO:tensorflow:accuracy: 0.855412
I0627 09:30:33.164101 140205349771008 run_classifier.py:544] accuracy: 0.855412
INFO:tensorflow:accuracy: 0.858992
I0627 10:09:33.507439 139862502569728 run_classifier.py:544] accuracy: 0.858992
INFO:tensorflow:accuracy: 0.847150
I0627 10:48:33.071874 139900365072128 run_classifier.py:544] accuracy: 0.847150
INFO:tensorflow:accuracy: 0.858166
I0627 11:27:33.064129 140169037788928 run_classifier.py:544] accuracy: 0.858166
INFO:tensorflow:accuracy: 0.852382
I0627 12:06:33.476964 139688656287488 run_classifier.py:544] accuracy: 0.852382
INFO:tensorflow:accuracy: 0.855412
I0627 12:45:33.331864 140689610348288 run_classifier.py:544] accuracy: 0.855412
INFO:tensorflow:accuracy: 0.850730
I0627 13:24:33.374700 140027493340928 run_classifier.py:544] accuracy: 0.850730


# on nlpcc_dbqa
nohup ./src/char_spaced/scripts/run_classifier_nlpcc_dbqa_21128.sh > char_spaced_nlpcc_dbqa_21128.log &

grep "'weighted avg'" char_spaced_nlpcc_dbqa_21128.log

0.6308357644825466
0.6810172487329283
0.6271846482416104
0.6151076534420672
0.6619500192118919


```
