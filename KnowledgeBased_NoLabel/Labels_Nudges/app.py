from datetime import datetime
import csv


from collections import defaultdict
import os
import pandas as pd


# 'caloriesLevel', 'fatLevel', 'magnesiumLevel',
#        'sodiumLevel', 'proteinLevel', 'sugarLevel', 'InstructionLevel',
#        'fiberLevel', 'carbsLevel', 'TimeLevel', 'VibB6Level',
#        'IngredientsLevel', 'magLevel'


def get_top_recommendations(user_input,healhiness):

    # read data
    recipes = pd.read_csv('./static/Data_csv/'+healhiness+'features.csv')
    recipes['score'] = 0

    recipes.loc[recipes.caloriesLevel == user_input['BMI'][0], 'score'] += 1
    recipes.loc[recipes.carbsLevel == user_input['BMI'][1], 'score'] += 1
    recipes.loc[recipes.proteinLevel == user_input['BMI'][2], 'score'] += 1
    
    recipes.loc[recipes.caloriesLevel == user_input['eatingGoals'][0], 'score'] += 1
    recipes.loc[recipes.fatLevel == user_input['eatingGoals'][1], 'score'] += 1
  
    recipes.loc[recipes.proteinLevel == user_input['behaviour'][0], 'score'] += 1
    recipes.loc[recipes.caloriesLevel == user_input['behaviour'][1], 'score'] += 1
    
    recipes.loc[recipes.magnesiumLevel == user_input['sleep'][0], 'score'] += 1
    recipes.loc[recipes.fiberLevel == user_input['sleep'][1], 'score'] += 1
    recipes.loc[recipes.proteinLevel == user_input['sleep'][2], 'score'] += 1
    recipes.loc[recipes.VibB6Level == user_input['sleep'][3], 'score'] += 1
    recipes.loc[recipes.fatLevel == user_input['sleep'][4], 'score'] += 1
    
    recipes.loc[recipes.proteinLevel == user_input['depression'][0], 'score'] += 1
    recipes.loc[recipes.carbsLevel == user_input['depression'][1], 'score'] += 1
    
    recipes.loc[(recipes.recipe_prep_time >= user_input['cookingTime'][0]) & ((recipes.recipe_prep_time <= user_input['cookingTime'][1])), 'score'] += 1

    recipes.loc[recipes.IngredientsLevel == user_input['CookingExp'][0], 'score'] += 1
    recipes.loc[recipes.InstructionLevel == user_input['CookingExp'][1], 'score'] += 1



    ids_recipes = recipes.sort_values(by=['score'], ascending=False)[:5]['id']
    
    
    return list(ids_recipes)
  