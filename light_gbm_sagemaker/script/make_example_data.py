
path_mapping = {
        "binary.train": "data", 
        "train.conf": "conf"
}

channel_mapping = {
        "data": "binary.train", 
        "conf": "train.conf" 
}


from shutil import copyfile
import sys 
import os 

def move_files(prefix, cdir):
    files = os.listdir(cdir)
    for basename in files:
        if basename not in path_mapping: 
            continue 
        
        to_path = os.path.join (prefix, path_mapping[basename], basename) 
        if not os.path.exists(os.path.join(prefix, path_mapping[basename])):
            os.mkdir(os.path.join(prefix, path_mapping[basename]))
        copyfile(os.path.join(cdir, basename), to_path)

import json 
def write_file_list(dst_config_file): 
    f = open(dst_config_file, 'w')
    json.dump(channel_mapping, f)
 

if __name__=="__main__":
    dst_data_folder = sys.argv[1]
    src_folder = sys.argv[2]
    dst_config_folder = sys.argv[3]
    move_files(dst_data_folder, src_folder)
    write_file_list(dst_config_folder)
