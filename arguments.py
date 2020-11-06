# -*- coding: utf-8 -*-
'''
@author: zhonghongfly@foxmail.com
@license: (C) Copyright 2020
@desc: 参数配置
@DateTime: Created on 2020/9/27, at 下午 03:45 by PyCharm
'''

BERT_BASE_DIR = 'E:\\chinese_L-12_H-768_A-12\\'
arg_dic = {
    "data_dir": './data/',  # 数据目录
    "output_dir": './output/',  # ckpt 输出目录
    'pb_model_dir': './pb/',
    "bert_config_file": BERT_BASE_DIR + 'bert_config.json',
    "task_name": 'cnews',  # "The name of the task to train.
    "vocab_file": BERT_BASE_DIR + 'vocab.txt',  # The vocabulary file that the BERT model was trained on.
    "init_checkpoint": BERT_BASE_DIR + 'bert_model.ckpt',
    # "Initial checkpoint (usually from a pre-trained BERT model).
    "do_lower_case": True,
    "max_seq_length": 502,
    "overlap_len": 100,
    "do_train": False,
    "do_eval": False,
    "do_predict": True,
    "train_batch_size": 6,
    "eval_batch_size": 8,
    "predict_batch_size": 8,
    "learning_rate": 3e-5,
    "num_train_epochs": 5,
    "warmup_proportion": 0.1,  # "Proportion of training to perform linear learning rate warmup for. "
    # "E.g., 0.1 = 10% of training."
    "save_checkpoints_steps": 100,  # How often to save the model checkpoint."
    "iterations_per_loop": 1000,  # "How many steps to make in each estimator call.

    "use_tpu": False,
    "tpu_name": False,
    "tpu_zone": False,
    "gcp_project": False,
    "master": False,
    "num_tpu_cores": False,  # "Only used if `use_tpu` is True. Total number of TPU cores to use."
}
