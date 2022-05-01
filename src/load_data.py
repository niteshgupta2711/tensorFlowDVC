from tqdm import tqdm
from src.utils.main import read_yaml
import argparse
import shutil
import os
# shutil is for copying items
# source and destination
def copy_data_to_local(source,dest):
    for sf,df in tqdm(zip(source,dest)):
        for file in os.listdir(sf):
            sfile=os.path.join(sf,file)
            dfile=os.path.join(df,file)
            shutil.copy(sfile,dfile)


    




if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--config','-c',default='config/config.yaml')
    args=parser.parse_args()
    config_d=read_yaml(args.config)
    local_data_dir=config_d['local_data_path']
    for path in local_data_dir: 

        os.makedirs(path,exist_ok=True)
    remote_data_path=config_d['source_download_path']
    copy_data_to_local(remote_data_path,local_data_dir)



