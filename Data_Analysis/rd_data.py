# this script is to use as a modele to read data from separate folders and produce a dataframe format

import pandas 
def read_data(condition,study, steps):
    path = '../'+condition+'/' + study +'/'+ steps + '_15.csv'
    # print('---',path)
    return pandas.read_csv(path)

def struct_data(condition):
	# Rec Conditoin
	

    # Condition 
    base = 'Baseline'  # 
    fsa = 'MTL'
    Full = 'Full'

    # Steps
    steps = ['personal_info','recommendations','selectedrecipe','evaluatechoices']

    if condition == "KB":
    	steps.append('profile')

    # create a dic to store all DF of each condition at one

    B = {}
    M = {}
    F = {}

    # For each comdition read data per step
    for i in steps:
        bn ='B_' + i
        mm = 'M_' + i
        fn = 'F_' + i
        B[bn] = read_data(condition,base,i)
        M[mm] = read_data(condition,fsa,i)
        F[fn] = read_data(condition,Full,i)
    return B, M, F

# Respondent that finished all steps

def finishedres(condition, t):
    finishedall = condition[t+'_evaluatechoices'].person
    if t == 'F':
        finishedall = condition[t+'_evaluatechoices'].person.loc[0:59]
    personal = t + '_personal_info'
    for i in condition.keys():
        if i == personal:
            condition[i] = condition[i][condition[i].id.isin(finishedall)]
        else :            
            condition[i] = condition[i][condition[i].person.isin(finishedall)]
    return None