### clone this repo
```
git clone https://github.com/catwhiskers/AWSLearningNotes.git
```

1. change directory to lightgbm/script

```
cd AWSLearningNotes/lightgbm/script
```

2. execute build_and_push.sh 
```
./build_and_push.sh ${accound_id} ${region} ${tagname}
```

3. configure your sagemaker training job in the following way - have your channel names the same as input parameters

for example - 

```
lightgbm config=train.config data=binary.train
```

You should put your `train.config` to a channel named as `config` and `binary.train` as `data`
 
Done 


