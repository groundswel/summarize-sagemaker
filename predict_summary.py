# -*- coding: utf-8 -*-
import pandas as pd
from simpletransformers.seq2seq import Seq2SeqModel, Seq2SeqArgs

model_args = Seq2SeqArgs()
model_args.num_train_epochs = 3
model_args.evaluate_generated_text = True
model_args.evaluate_during_training = True
model_args.evaluate_during_training_verbose = True

model_reloaded = Seq2SeqModel(
    encoder_decoder_type="bart",
    encoder_decoder_name="outputs",
    args=model_args,
    use_cuda=False
)


with open("just_summary_1.csv", "r") as file:
    for line in file:
        fields = line.strip().split("|")
        input_text = fields[-1]
        predict_text = model_reloaded.predict([input_text])
        print(f"{line}|{predict_text}")
