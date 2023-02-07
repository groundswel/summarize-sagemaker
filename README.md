# summarize-smaker
Code to use machine learning to summarize texts. We use a sagemaker notebook instance but can be applicable elsehwere too. 

Assuming you have your training data in a csv file where each field is seperated by a "|" .  Similarly the data to summarize is also in a csv file with each field seperated by "|". The difference is that the training data csv file also has an additional filed appended at the end of each row with the target data i.e in this context the summary of the field previous to it. 

Upload both the csv files to S3. Spin up a SageMaker notebook instance (probably m3.2xlarge or bigger) and download the csv files to the notebook instance. Consider changing to a filesystem that has enough space to hold the model data. 

Run train_summary.py which will split the training data from the training file and train the model. You can change the number of epochs as desired. If GPU is available to you turn it on by specifying use_cuda to True. 

Once the model is successfully tested the output will be saved to outputs folder. 

Run the predict_summary.py script which will generate the prediction and append the predicted text next to each row. The output will be directed to standad output so you can use any method to redirect it to a file. 
