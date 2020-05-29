# -*- coding: utf-8 -*-
"""
Created on Thu May 28 12:37:33 2020

@author: Sandeepan Paul
"""

import glassdoor_scraper as gs
import pandas as pd
path = "D:/DScience/MachineLearningPractical/SalaryProj/chromedriver"

df = gs.get_jobs('data scientist', 1000, False, path, 30)

df.to_csv('glassdoor_jobs.csv', index=False)