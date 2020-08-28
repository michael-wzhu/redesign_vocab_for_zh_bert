# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 4:16 下午
# @Author  : jeffery
# @FileName: one_click.py
# @Description:

from pathlib import Path
from collections import defaultdict
import pandas as pd
import numpy as np
import gc
from tqdm import tqdm
import json

import os
import tensorflow.compat.v1 as tf


# def get_all_data(hosp, cate, all_data):
#     for idx, row in tqdm(hosp.iterrows()):
#         all_data[row['visit_no']] = {
#             'gender_code': row['gender_code'],
#             'birthday': row['birthday'],
#             'reg_date': row['reg_date'],
#             'Icd10Id': row['Icd10Id'],
#             'Icd10Name': row['Icd10Name'],
#             'hospital': cate
#         }


STORAGE_BUCKET = "gs://sbt0"

# input_dir_storage = os.path.join(
#                     STORAGE_BUCKET,
#                         "experiments/ehr_diagnose/datasets/outpatients-emr.zip"
#                         )
# input_dir_local = "outpatients-emr.zip"
#
# tf.gfile.Copy(input_dir_storage, input_dir_local, overwrite=True)


out_file = Path('corpus.txt')
to_dir_storage = os.path.join(
    STORAGE_BUCKET,
    "experiments/ehr_diagnose/datasets/corpus.txt"
)
tf.gfile.Copy(out_file, to_dir_storage, overwrite=True)


# base_dir = Path('outpatients-emr')
# # 读取诊断信息
# hosp1_csv = base_dir / 'hosp1.csv'
# hosp2_csv = base_dir / 'hosp2.csv'
# hosp3_csv = base_dir / 'hosp3.csv'
# hosp1 = pd.read_csv(hosp1_csv)
# hosp2 = pd.read_csv(hosp2_csv)
# hosp3 = pd.read_csv(hosp3_csv)
# print('hosp1 examples num:{} \t hosp2 examples num:{} \t hosp3 examples num:{} \t total examples num:{}'.format(
#     len(hosp1), len(hosp2), len(hosp3), (len(hosp1) + len(hosp2) + len(hosp3))))
#
# all_data = defaultdict(dict)
# get_all_data(hosp1, 'hosp1', all_data)
# get_all_data(hosp2, 'hosp2', all_data)
# get_all_data(hosp3, 'hosp3', all_data)
#
# # 向dataframe中写入相关文本
# for dir in base_dir.iterdir():
#     if dir.is_dir():
#         for f in dir.iterdir():
#             if f.is_file():
#                 dis_class = dir.name
#                 col_name = f.name.split('_')[:-2]
#                 if len(col_name) > 1:
#                     col_name = '_'.join(col_name)
#                 else:
#                     col_name = col_name[0]
#
#                 with f.open('r') as json_f:
#                     temp_dict = json.load(json_f)
#                     for data_item in temp_dict['data']:
#                         content = data_item['content']
#                         visit_no = data_item['visit_no']
#                         if visit_no not in all_data:
#                             continue
#
#                         all_data[visit_no]['dis_class'] = dis_class
#                         all_data[visit_no][col_name] = content
# # 合并后的数据转成csv
# datas = []
# for key, val in tqdm(all_data.items()):
#     temp_dict = dict()
#     temp_dict['visit_no'] = key
#     for sub_key, sub_val in val.items():
#         temp_dict[sub_key] = sub_val
#     datas.append(temp_dict)
# print('after data process, total sample number is {}'.format(len(datas)))
#
# data_pd = pd.DataFrame(datas)
# print('writing domain text ...')
# out_file = Path('corpus.txt')
# with out_file.open('w') as out_file:
#     for idx, row in tqdm(data_pd.iterrows()):
#         if not pd.isnull(row['cc']):
#             out_file.write('主诉\n' + row['cc'].strip() + '\n')
#         if not pd.isnull(row['hpi']):
#             out_file.write('现病史\n' + row['hpi'].strip() + '\n')
#         if not pd.isnull(row['pe']):
#             out_file.write('体格检查\n' + row['pe'].strip() + '\n')
#         if not pd.isnull(row['ae']):
#             out_file.write('辅助检查\n' + row['ae'].strip() + '\n')
#         if not pd.isnull(row['pacs_description']):
#             out_file.write('检查所见\n' + row['pacs_description'].strip() + '\n')
#         if not pd.isnull(row['pacs_impression']):
#             out_file.write('诊断意见\n' + row['pacs_impression'].strip() + '\n')
#         out_file.write('\n')
