from numpy import append
from tqdm import tqdm
from src.utils.main import read_yaml
import argparse
import shutil
import os
import logging
logging_str='[%(asctime)s: %(levelname)s: %(module)s]: %(message)s'
stage_logs='stage_logs'
os.makedirs(stage_logs,exist_ok=True)
logging.basicConfig(filename=os.path.join(stage_logs,'load_data.log'),level=logging.INFO,format=logging_str,filemode='a')
# shutil is for copying items
# source and destination
def copy_data_to_local(source,dest):
    for sf,df in tqdm(zip(source,dest)):
        for file in os.listdir(sf):
            sfile=os.path.join(sf,file)
            dfile=os.path.join(df,file)
            shutil.copy(sfile,dfile)
    logging.info('Successfully sent the remote to local storage')

    




if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--config','-c',default='config/config.yaml')
    logging.info('args have been readed')
    args=parser.parse_args()
    config_d=read_yaml(args.config)
    logging.info('yaml has been parsed')
    local_data_dir=config_d['local_data_path']
    for path in local_data_dir: 
        os.makedirs(path,exist_ok=True)
    remote_data_path=config_d['source_download_path']
    copy_data_to_local(remote_data_path,local_data_dir)



