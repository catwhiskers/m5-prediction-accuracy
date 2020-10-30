from __future__ import absolute_import

import sys
import time
import os
import subprocess
from subprocess import PIPE

from util import ExitSignalHandler
from util import write_failure_file, print_json_object, load_json_object, save_model_artifacts, get_files_in_path

hyperparameters_file_path = "/opt/ml/input/config/hyperparameters.json"
inputdataconfig_file_path = "/opt/ml/input/config/inputdataconfig.json"
resource_file_path = "/opt/ml/input/config/resourceconfig.json"
data_files_path = "/opt/ml/input/data/"
failure_file_path = "/opt/ml/output/failure"
model_artifacts_path = "/opt/ml/model/"

training_job_name_env = "TRAINING_JOB_NAME"
training_job_arn_env = "TRAINING_JOB_ARN"


def lightgbm_train(input_files, hyperparameters): 
    command_args = ["/usr/local/bin/lightgbm"]  
   
    command_args.append('config=/train.conf') 
    for k, v in hyperparameters.items():
        print(k,v)
        command_args.append(k+'='+v) 
    for k, v in input_files.items():
        print(k,v)
        command_args.append(k+'='+v[0]) 
    command_args.append("output_model="+os.path.join(model_artifacts_path, "model.txt"))    

    subprocess.call(command_args)
    
def run():
    try:
        print("\nRunning training...")
        model_data_files = {} 
        hyperparameters = {} 
        if os.path.exists(hyperparameters_file_path):
            hyperparameters = load_json_object(hyperparameters_file_path)
            print('\nHyperparameters configuration:')
            print_json_object(hyperparameters)
        if os.path.exists(inputdataconfig_file_path):
            input_data_config = load_json_object(inputdataconfig_file_path)
            print('\nInput data configuration:')
            print_json_object(input_data_config)
            
            for key in input_data_config:
                print('\nList of files in {0} channel: '.format(key))
                channel_path = data_files_path + key + '/'
                files = get_files_in_path(channel_path)
                model_data_files[key] = files
        
        if os.path.exists(resource_file_path):
            resource_config = load_json_object(resource_file_path)
            print('\nResource configuration:')
            print_json_object(resource_config)
            
        if (training_job_name_env in os.environ):
            print("\nTraining job name: ")
            print(os.environ[training_job_name_env])
        
        if (training_job_arn_env in os.environ):
            print("\nTraining job ARN: ")
            print(os.environ[training_job_arn_env])
            
        # This object is used to handle SIGTERM and SIGKILL signals.
        signal_handler = ExitSignalHandler()
        lightgbm_train(model_data_files, hyperparameters) 
        

        
        
        print("\nTraining completed!")
    except Exception as e:
        write_failure_file(failure_file_path, str(e))
        print(e, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if (sys.argv[1] == "train"):
        run()
    else:
        print("Missing required argument 'train'.", file=sys.stderr)
        sys.exit(1)

