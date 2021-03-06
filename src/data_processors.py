# -*- coding: utf-8 -*-
# @Author: bo.shi
# @Date:   2019-12-01 22:28:41
# @Last Modified by:   bo.shi
# @Last Modified time: 2019-12-02 18:36:50
# coding=utf-8
# Copyright 2019 The Google Research Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Utility functions for GLUE classification tasks."""

from __future__ import absolute_import
from __future__ import division

from __future__ import print_function

import json
import csv
import os
import six

import tensorflow as tf


def convert_to_unicode(text):
    """Converts `text` to Unicode (if it's not already), assuming utf-8 input."""
    if six.PY3:
        if isinstance(text, str):
            return text
        elif isinstance(text, bytes):
            return text.decode("utf-8", "ignore")
        else:
            raise ValueError("Unsupported string type: %s" % (type(text)))
    elif six.PY2:
        if isinstance(text, str):
            return text.decode("utf-8", "ignore")
        elif isinstance(text, unicode):
            return text
        else:
            raise ValueError("Unsupported string type: %s" % (type(text)))
    else:
        raise ValueError("Not running on Python2 or Python 3?")


class InputExample(object):
    """A single training/test example for simple sequence classification."""

    def __init__(self, guid, text_a, text_b=None, label=None):
        """Constructs a InputExample.
        Args:
          guid: Unique id for the example.
          text_a: string. The untokenized text of the first sequence. For single
            sequence tasks, only this sequence must be specified.
          text_b: (Optional) string. The untokenized text of the second sequence.
            Only must be specified for sequence pair tasks.
          label: (Optional) string. The label of the example. This should be
            specified for train and dev examples, but not for test examples.
        """
        self.guid = guid
        self.text_a = text_a
        self.text_b = text_b
        self.label = label


class PaddingInputExample(object):
    """Fake example so the num input examples is a multiple of the batch size.
    When running eval/predict on the TPU, we need to pad the number of examples
    to be a multiple of the batch size, because the TPU requires a fixed batch
    size. The alternative is to drop the last batch, which is bad because it means
    the entire output data won't be generated.
    We use this class instead of `None` because treating `None` as padding
    battches could cause silent errors.
    """


class DataProcessor(object):
    """Base class for data converters for sequence classification data sets."""

    def __init__(self, args):
        self.args = args

    def get_train_examples(self, data_dir):
        """Gets a collection of `InputExample`s for the train set."""
        raise NotImplementedError()

    def get_dev_examples(self, data_dir):
        """Gets a collection of `InputExample`s for the dev set."""
        raise NotImplementedError()

    def get_test_examples(self, data_dir):
        """Gets a collection of `InputExample`s for prediction."""
        raise NotImplementedError()

    def get_labels(self):
        """Gets the list of labels for this data set."""
        raise NotImplementedError()

    @classmethod
    def _read_tsv(cls, input_file, delimiter="\t", quotechar=None):
        """Reads a tab separated value file."""
        with tf.gfile.Open(input_file, "r") as f:
            reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)
            lines = []
            for line in reader:
                lines.append(line)
            return lines

    @classmethod
    def _read_txt(cls, input_file):
        """Reads a tab separated value file."""
        with tf.gfile.Open(input_file, "r") as f:
            reader = f.readlines()
            lines = []
            for line in reader:
                lines.append(line.strip().split("_!_"))
            return lines

    @classmethod
    def _read_jsonl(cls, input_file):
        """Reads a json-line file."""
        with tf.gfile.Open(input_file, "r") as f:
            reader = f.readlines()
            lines = []
            for line in reader:
                lines.append(json.loads(line.strip()))
            return lines


def _truncate_seq_pair(sent_a,
                       sent_b,
                       max_length):
    """Truncates a sequence pair in place to the maximum length."""

    # This is a simple heuristic which will always truncate the longer sequence
    # one token at a time. This makes more sense than truncating an equal percent
    # of sent from each, since if one sequence is very short then each token
    # that's truncated likely contains more information than a longer sequence.
    while True:
        total_length = len(sent_a) + len(sent_b)
        if total_length <= max_length:
            break

        if len(sent_a) > len(sent_b):
            sent_a = sent_a[: -1]
        else:
            sent_b = sent_b[: -1]


class XnliProcessor(DataProcessor):
    """Processor for the XNLI data set."""

    def get_train_examples(self, data_dir):
        """See base class."""
        return self._create_examples(
            self._read_jsonl(os.path.join(data_dir, "train.json")), "train")

    def get_dev_examples(self, data_dir):
        """See base class."""
        return self._create_examples(
            self._read_jsonl(os.path.join(data_dir, "dev.json")), "dev")

    def get_test_examples(self, data_dir):
        """See base class."""
        return self._create_examples(
            self._read_jsonl(os.path.join(data_dir, "test.json")), "test")

    def _create_examples(self, lines, set_type):
        """See base class."""
        examples = []
        for (i, line) in enumerate(lines):
            guid = "%s-%s" % (set_type, i)

            text_a = line['sentence1']
            if self.args.do_lower_case:
                text_a = text_a.lower()

            text_b = line['sentence2']
            if self.args.do_lower_case:
                text_b = text_b.lower()

            _truncate_seq_pair(
                text_a,
                text_b,
                self.args.max_num_chars
            )

            label = line['label'] if set_type != 'test' else '0'

            examples.append(
                InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label))
        return examples

    def get_labels(self):
        """See base class."""
        return ["0", "1", "2"]


class ChnSentiCorpDataProcessor(DataProcessor):
    """Processor for the ChnSentiCorp data set."""

    def __init__(self, args):
        super(ChnSentiCorpDataProcessor, self).__init__(args)
        self.args = args

    def get_train_examples(self, data_dir):
        """See base class."""
        return self._create_examples(
            self._read_jsonl(os.path.join(data_dir, "train.json")), "train")

    def get_dev_examples(self, data_dir):
        """See base class."""
        return self._create_examples(
            self._read_jsonl(os.path.join(data_dir, "dev.json")), "dev")

    def get_test_examples(self, data_dir):
        """See base class."""
        return self._create_examples(
            self._read_jsonl(os.path.join(data_dir, "test.json")), "test")

    def get_labels(self):
        """See base class."""
        labels = []
        for i in range(2):
            labels.append(str(i))
        return labels

    def _create_examples(self, lines, set_type):
        """Creates examples for the training and dev sets."""
        examples = []
        for (i, line) in enumerate(lines):
            guid = "%s-%s" % (set_type, i)
            text_a = line['sentence']
            text_a = text_a.strip()[: self.args.max_num_chars]
            if self.args.do_lower_case:
                text_a = text_a.lower()
            text_b = None
            label = line['label'] if set_type != 'test' else "0"
            examples.append(
                InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label))
        return examples


class BookReviewProcessor(DataProcessor):
    """Processor for the ChnSentiCorp data set."""

    def __init__(self, args):
        super(BookReviewProcessor, self).__init__(args)
        self.args = args

    def get_train_examples(self, data_dir):
        """See base class."""
        return self._create_examples(
            self._read_jsonl(os.path.join(data_dir, "train.json")), "train")

    def get_dev_examples(self, data_dir):
        """See base class."""
        return self._create_examples(
            self._read_jsonl(os.path.join(data_dir, "dev.json")), "dev")

    def get_test_examples(self, data_dir):
        """See base class."""
        return self._create_examples(
            self._read_jsonl(os.path.join(data_dir, "test.json")), "test")

    def get_labels(self):
        """See base class."""
        labels = []
        for i in range(2):
            labels.append(str(i))
        return labels

    def _create_examples(self, lines, set_type):
        """Creates examples for the training and dev sets."""
        examples = []
        for (i, line) in enumerate(lines):
            guid = "%s-%s" % (set_type, i)
            text_a = line['sentence1']
            text_a = text_a.strip()[: self.args.max_num_chars]
            if self.args.do_lower_case:
                text_a = text_a.lower()
            text_b = None
            label = line['label'] if set_type != 'test' else "0"
            examples.append(
                InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label))
        return examples


class ShoppingProcessor(DataProcessor):
    """Processor for the ChnSentiCorp data set."""

    def __init__(self, args):
        super(ShoppingProcessor, self).__init__(args)
        self.args = args

    def get_train_examples(self, data_dir):
        """See base class."""
        return self._create_examples(
            self._read_jsonl(os.path.join(data_dir, "train.json")), "train")

    def get_dev_examples(self, data_dir):
        """See base class."""
        return self._create_examples(
            self._read_jsonl(os.path.join(data_dir, "dev.json")), "dev")

    def get_test_examples(self, data_dir):
        """See base class."""
        return self._create_examples(
            self._read_jsonl(os.path.join(data_dir, "test.json")), "test")

    def get_labels(self):
        """See base class."""
        labels = []
        for i in range(2):
            labels.append(str(i))
        return labels

    def _create_examples(self, lines, set_type):
        """Creates examples for the training and dev sets."""
        examples = []
        for (i, line) in enumerate(lines):
            guid = "%s-%s" % (set_type, i)
            text_a = line['sentence1']
            text_a = text_a.strip()[: self.args.max_num_chars]
            if self.args.do_lower_case:
                text_a = text_a.lower()
            text_b = None
            label = line['label'] if set_type != 'test' else "0"
            examples.append(
                InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label))
        return examples


class WeiboProcessor(DataProcessor):
    """Processor for the ChnSentiCorp data set."""

    def __init__(self, args):
        super(WeiboProcessor, self).__init__(args)
        self.args = args

    def get_train_examples(self, data_dir):
        """See base class."""
        return self._create_examples(
            self._read_jsonl(os.path.join(data_dir, "train.json")), "train")

    def get_dev_examples(self, data_dir):
        """See base class."""
        return self._create_examples(
            self._read_jsonl(os.path.join(data_dir, "dev.json")), "dev")

    def get_test_examples(self, data_dir):
        """See base class."""
        return self._create_examples(
            self._read_jsonl(os.path.join(data_dir, "test.json")), "test")

    def get_labels(self):
        """See base class."""
        labels = []
        for i in range(2):
            labels.append(str(i))
        return labels

    def _create_examples(self, lines, set_type):
        """Creates examples for the training and dev sets."""
        examples = []
        for (i, line) in enumerate(lines):
            guid = "%s-%s" % (set_type, i)
            text_a = line['sentence1']
            text_a = text_a.strip()[: self.args.max_num_chars]
            if self.args.do_lower_case:
                text_a = text_a.lower()
            text_b = None
            label = line['label'] if set_type != 'test' else "0"
            examples.append(
                InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label))
        return examples


class LCQMCProcessor(DataProcessor):
    """Processor for the internal data set. sentence pair classification"""

    def get_train_examples(self, data_dir):
        """See base class."""
        return self._create_examples(
            self._read_jsonl(os.path.join(data_dir, "train.json")), "train")

    def get_dev_examples(self, data_dir):
        """See base class."""
        return self._create_examples(
            self._read_jsonl(os.path.join(data_dir, "dev.json")), "dev")

    def get_test_examples(self, data_dir):
        """See base class."""
        return self._create_examples(
            self._read_jsonl(os.path.join(data_dir, "test.json")), "test")

    def get_labels(self):
        """See base class."""
        return ["0", "1"]

    def _create_examples(self, lines, set_type):
        """Creates examples for the training and dev sets."""
        examples = []
        for (i, line) in enumerate(lines):
            guid = "%s-%s" % (set_type, i)
            text_a = line['sentence1']
            if self.args.do_lower_case:
                text_a = text_a.lower()
            text_b = line['sentence2']
            if self.args.do_lower_case:
                text_b = text_b.lower()

            _truncate_seq_pair(
                text_a,
                text_b,
                self.args.max_num_chars
            )

            label = line['label'] if set_type != 'test' else "0"
            examples.append(
                InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label))
        return examples


class LawQAProcessor(DataProcessor):
    """Processor for the internal data set. sentence pair classification"""

    def get_train_examples(self, data_dir):
        """See base class."""
        return self._create_examples(
            self._read_jsonl(os.path.join(data_dir, "train.json")), "train")

    def get_dev_examples(self, data_dir):
        """See base class."""
        return self._create_examples(
            self._read_jsonl(os.path.join(data_dir, "dev.json")), "dev")

    def get_test_examples(self, data_dir):
        """See base class."""
        return self._create_examples(
            self._read_jsonl(os.path.join(data_dir, "test.json")), "test")

    def get_labels(self):
        """See base class."""
        return ["0", "1"]

    def _create_examples(self, lines, set_type):
        """Creates examples for the training and dev sets."""
        examples = []
        for (i, line) in enumerate(lines):
            guid = "%s-%s" % (set_type, i)
            text_a = line['sentence1']
            if self.args.do_lower_case:
                text_a = text_a.lower()
            text_b = line['sentence2']
            if self.args.do_lower_case:
                text_b = text_b.lower()

            _truncate_seq_pair(
                text_a,
                text_b,
                self.args.max_num_chars
            )

            label = line['label'] if set_type != 'test' else "0"
            examples.append(
                InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label))
        return examples


class NlpccDbqaProcessor(DataProcessor):
    """Processor for the internal data set. sentence pair classification"""

    def get_train_examples(self, data_dir):
        """See base class."""
        return self._create_examples(
            self._read_jsonl(os.path.join(data_dir, "train.json")), "train")

    def get_dev_examples(self, data_dir):
        """See base class."""
        return self._create_examples(
            self._read_jsonl(os.path.join(data_dir, "dev.json")), "dev")

    def get_test_examples(self, data_dir):
        """See base class."""
        return self._create_examples(
            self._read_jsonl(os.path.join(data_dir, "test.json")), "test")

    def get_labels(self):
        """See base class."""
        return ["0", "1"]

    def _create_examples(self, lines, set_type):
        """Creates examples for the training and dev sets."""
        examples = []
        for (i, line) in enumerate(lines):
            guid = "%s-%s" % (set_type, i)
            text_a = line['sentence1']
            if self.args.do_lower_case:
                text_a = text_a.lower()
            text_b = line['sentence2']
            if self.args.do_lower_case:
                text_b = text_b.lower()

            _truncate_seq_pair(
                text_a,
                text_b,
                self.args.max_num_chars
            )

            label = line['label'] if set_type != 'test' else "0"
            examples.append(
                InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label))
        return examples