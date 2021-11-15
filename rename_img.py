# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 15:33:10 2021

@author: Sige Hu
"""

"""
use to rename the file
"""

import os
from shutil import copyfile, copy

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(PROJECT_ROOT,'dataset_DIV\png_HR_rsz510_new')
dest_path = os.path.join(file_path,'algo2_sige')
dest_path1 = os.path.join(file_path,'algo1_sige')



for file in os.listdir(file_path):
    if file.endswith("_SE_final.png"):
            copy(os.path.join(file_path,file),dest_path)
    else:
        if file.endswith('.png'):
#            print(file)
            copy(os.path.join(file_path,file),dest_path1)

for file in os.listdir(dest_path):
    if not file.startswith('algo2_'):
        print(file)
        new_file = 'algo2_' + file
        new_file = new_file.split('_SE_final')[0] + new_file.split('_SE_final')[1]
        print(new_file)
        if not os.path.exists(os.path.join(dest_path,new_file)):
            os.rename(os.path.join(dest_path,file), os.path.join(dest_path,new_file))
        else:
            os.remove(os.path.join(dest_path,file))
    
    
for file in os.listdir(dest_path1):
    if not file.startswith('algo1_'):    
        print(file)
        new_file = 'algo1_' + file
        print(new_file)
        if not os.path.exists(os.path.join(dest_path1,new_file)):
            os.rename(os.path.join(dest_path1,file), os.path.join(dest_path1,new_file))
        else:
            os.remove(os.path.join(dest_path1,file))        