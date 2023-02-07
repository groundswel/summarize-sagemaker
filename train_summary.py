# -*- coding: utf-8 -*-
import pandas as pd
from simpletransformers.seq2seq import Seq2SeqModel, Seq2SeqArgs



train_data = []

with open("just_train_1.csv", "r") as file:
    for line in file:
        fields = line.strip().split("|")
        train_data.append([fields[-2], fields[-1]])


#print(train_data)


train_df = pd.DataFrame(train_data, columns=["input_text", "target_text"])


eval_data = train_data[-5:]
train_data = train_data[:-5]

eval_df = pd.DataFrame(eval_data, columns=["input_text", "target_text"])


# Configure the model
model_args = Seq2SeqArgs()
model_args.num_train_epochs = 1
model_args.evaluate_generated_text = True
model_args.evaluate_during_training = True
model_args.evaluate_during_training_verbose = True

print('model initializing')

model = Seq2SeqModel(
    encoder_decoder_type="bart",
    encoder_decoder_name="facebook/bart-large",
    args=model_args,
    use_cuda=False
)

print('model training')
# Train the model
model.train_model(train_df, eval_data=eval_df)

print('model evaluatiing')
# Evaluate the model
result = model.eval_model(eval_df)

# Use the model for prediction
pr_str='''Relative atomic mass (symbol: Ar; sometimes abbreviated RAM or r.a.m.), also known by the deprecated synonym atomic weight, is a dimensionless physical quantity defined as the ratio of the average mass of atoms of a chemical element in a given sample to the atomic mass constant. The atomic mass constant (symbol: mu) is defined as being 
1
/
12
 of the mass of a carbon-12 atom.[1][2] Since both quantities in the ratio are masses, the resulting value is dimensionless; hence the value is said to be relative.

For a single given sample, the relative atomic mass of a given element is the weighted arithmetic mean of the masses of the individual atoms (including their isotopes) that are present in the sample. This quantity can vary substantially between samples because the sample's origin (and therefore its radioactive history or diffusion history) may have produced unique combinations of isotopic abundances. For example, due to a different mixture of stable carbon-12 and carbon-13 isotopes, a sample of elemental carbon from volcanic methane will have a different relative atomic mass than one collected from plant or animal tissues.'''

print('model predict')

print(
    model.predict(
        [
            pr_str
        ]
    )
)

