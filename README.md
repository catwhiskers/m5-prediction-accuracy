# m5-prediction-accuracy

## Objective 

Demo how to use AWS SageMaker to perform machine learning tasks. Dataset used is [sales data of Walmart](https://www.kaggle.com/c/m5-forecasting-accuracy). We employ machine learning algorithms to predict forthcoming 28 days sales unit of each item in each store. 

## Structure 

### Preparation 
Open a SageMaker notebook. FYI - I use ml.c5.2xlarge with 5GB EBS to run the code in this repository.  

### Data analysis and preprocessing 

[The notebook](https://github.com/catwhiskers/m5-prediction-accuracy/blob/main/01-data-analysis-and-preparation.ipynb) This notebook shows how to do data analysis and preprocessing on [SageMaker notebook](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html). Packages are pre-installed therefore we can execute the notebook directly without machine provisioning. 

## Performing training and prediction by a SageMaker built-in algorithm - xgboost 

On SageMaker, there are many built-in algorithms can be used directly. There is the [list](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html) to referece. All algorithms are managed in form of docker images, and are hosted on ECR (Elastic Container Registry). In this [notebook](https://github.com/catwhiskers/m5-prediction-accuracy/blob/main/02-training-built-in-and-byoc.ipynb), We use xgboost 1.0-1 to perform training and inferencing

## Performing training by your own algorithm

On SageMaker, you can define your own algorithms to use. This [notebook](https://github.com/catwhiskers/m5-prediction-accuracy/blob/main/03-training-bring-your-own-container.ipynb) demonstrate how to perform bring your own container.  

## SageMaker Experiment and Debugger 

It is important to facilitate efficient communication between data scientists. [SageMaker Experiments](https://aws.amazon.com/blogs/aws/amazon-sagemaker-experiments-organize-track-and-compare-your-machine-learning-trainings/) enables the team exchange the experiment information transparently. Moreover, results of the experiments can be easily reproduced; since the input/output artifacts in the experiments are kept in AWS S3, the hyperparameters, types of machines and algorithm used are recorded as well. 

It is also important to have a machanism to monitor the experiments and detect the troubles encountered early. To do troubleshooting further, record the criticle metrics and/or tensors are necessary. [SageMaker Debugger](https://aws.amazon.com/blogs/aws/amazon-sagemaker-debugger-debug-your-machine-learning-models/) provides the machanism for team to do training job monitoring and [this notebook](https://github.com/catwhiskers/m5-prediction-accuracy/blob/main/04-experiment-and-debugger.ipynb) demonstrate how to use SageMaker Experiments and Debugger 







