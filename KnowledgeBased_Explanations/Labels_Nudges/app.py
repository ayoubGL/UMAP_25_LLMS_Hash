

from datetime import datetime
import csv
import re

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
  
  
  
# OpenAI api

import openai
from openai import OpenAI
client = OpenAI(
    # This is the default and can be omitted
    api_key=("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"),
)

# OpenAI model
  
  

def get_explanation(user,recipe, healthiness):
    # print('user---------, hashtag',user)
    bmi = user['user_bmi']
    eating_goal = user['eating_goals']
    physical_activity = user['behavior']
    sleep = user['sleep']
    depression = user['depression']
    # print('reciepes---------',recipe['fsa_score'])
    
    Fsa = recipe['fsa_score']
    calories = recipe['calories']
    fat = recipe['fat']
    protein = recipe['protein']
    title  = recipe['title']
    
    
    user_behavior = 'chose'
    

    healthy_prompt = f"Provide a concise, grammatically correct 3-line explanations to convince a user with a BMI of {bmi}, an eating goal to {eating_goal}, {sleep} hours of sleep, a {depression} depressed, and {physical_activity} active, to chose {title}.  Highlight the dish\'s healthy aspect, such as FSA score of {Fsa}, {calories} calories, {fat}g fat, and {protein}g protein."
    
    unhealthy_prompt = f"Provide a concise, grammatically correct 3-line explanation to discourage a user with a BMI of {bmi}, an eating goal to {eating_goal},{sleep} hours of sleep,  a {depression} depressed, and {physical_activity}  active,  from choosing  {title}. Highlight the dish\'s unhealthy aspect, such as FSA score of {Fsa}, {calories} calories, {fat}g fat, and {protein}g protein."
  
  
   
    
    if healthiness == 'unhealthy':
       prompt = unhealthy_prompt 
    else:
        prompt = healthy_prompt
    # print('prompt------',prompt) 
    
    chat_completion = client.chat.completions.create(
        messages=[
        {
            "role":'system',
            "content": 'you are a nutritionist '
        },
        {  
            "role": "user",
            "content": prompt,
        }],
    model="gpt-3.5-turbo",
    )

    hashtags = re.findall(r'#\w+', chat_completion.choices[0].message.content)
    
    return hashtags


# def sustaible_ranker(personalized_recommdations):
    
#     return sorted_recipes_base_sustb