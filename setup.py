from setuptools import setup
setup(version='0.0.1',
author='Nitesh',
author_email='mail',
long_description='long description',
description='description',
packages=['src'],
name='lib_name',
install_requires=['pandas','dvc','tensorflow','pandas','tqdm','matplotlib','PyYAML','boto3'],
python_version='>=3.7'
)
 # conda create --prefix ./env -y
 # .gitignore env/
 # ls -la for git ignore