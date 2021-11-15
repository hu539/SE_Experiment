# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 15:30:17 2021

@author: Sige Hu
"""
import os
import pickle
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


fn = os.path.join(PROJECT_ROOT, 'yourname_results_part1.txt')
with open(fn, 'rb') as handle:
    score_list = pickle.load(handle)
    
    
