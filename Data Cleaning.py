# -*- coding: utf-8 -*-
"""
Created on Thu May 28 19:04:04 2020

@author: Sandeepan Paul
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

## Salary Parsing
df['hourly'] = df['Salary Estimate'].apply(lambda x:1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x:1 if 'employer provided salary' in x.lower() else 0)

df = df[df['Salary Estimate']!='-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))
min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = min_hr.apply(lambda  x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda  x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2


##Company Name Text Only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3],axis=1)

##City Field
df['job_headquarters_city'] = df['Headquarters'].apply(lambda x: x.split(',')[0])
df.job_headquarters_city.value_counts()


df['same_location'] = df.apply(lambda x:1 if x.Location == x.job_headquarters_city else 0, axis=1)

#Age of Company
df['company_age'] = df.Founded.apply(lambda x: x if x<1 else 2020-x)


##Parsing of Job description (python,etc)
#python
df['python_yn'] = df['Job Description'].apply(lambda x:1 if 'python' in str(x).lower() else 0)
df.python_yn.value_counts()

#R
df['R_yn'] = df['Job Description'].apply(lambda x:1 if 'R-Studio' in str(x).lower() or 'r studio' in str(x).lower() else 0)
df.R_yn.value_counts()

#Spark
df['spark_yn'] = df['Job Description'].apply(lambda x:1 if 'spark' in str(x).lower() else 0)
df.spark_yn.value_counts()

#AWS
df['aws_yn'] = df['Job Description'].apply(lambda x:1 if 'aws' in str(x).lower() else 0)
df.aws_yn.value_counts()

#Excel
df['excel_yn'] = df['Job Description'].apply(lambda x:1 if 'excel' in str(x).lower() else 0)
df.excel_yn.value_counts()

df.to_csv('glassdoor_jobs_cleaned.csv',index=False)
