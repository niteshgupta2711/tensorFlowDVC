from src.utils.main import read_yaml
import argparse
import os
import numpy as np
def load_base_model(config,params):
    config_=read_yaml(config)
    artifacts_dir=config_['artifacts']['ARTIFACTS_DIR']
    base_model_folder=config_['artifacts']['BASE_MODEL_DIR']
    base_model_dir=os.path.join(artifacts_dir,base_model_folder)
    os.makedirs(base_model_dir,exist_ok=True)
    base_model_name=config_['artifacts']['BASE_MODEL_NAME']
    base_model_path=os.path.join(base_model_dir,base_model_name)
    vgg16model=get_vgg16(input_shape,model_path)




if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--config','-c',default='config/config.yaml')
    parser.add_argument('--param','-p',default='params.yaml')
    args=parser.parse_args()
    config_d=read_yaml(args.config)
    param_d=read_yaml(args.param)

    load_base_model(config_d,param_d)