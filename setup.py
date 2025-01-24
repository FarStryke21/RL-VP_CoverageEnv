from setuptools import setup, find_packages

setup(
    nname='viewpoint-env',  
    version='0.0.1',
    packages=find_packages(),  
    install_requires=[
        'gymnasium',
        'numpy',
        'open3d==0.18.0',
        'scipy',
        'matplotlib'
    ],
    python_requires='>=3.6',
    description='Coverage Environment for Training Agents using the RL-VP algorithm.',  
    author='Aman Chulawala',  
    author_email='aman.chulawala@gmail.com',  
)
