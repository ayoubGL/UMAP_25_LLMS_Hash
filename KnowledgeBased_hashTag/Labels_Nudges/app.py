

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
  
  
def get_hashtag(user,recipe, healthiness):
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
    
    if bmi <= 18:
        bmi = "lower"
    elif bmi > 19 and bmi <= 24:
        bmi = "normal"
    else:
        bmi = "higher"
    if eating_goal == "No Goal":
        eating_goal = "no eating goal"
    elif eating_goal == "Gain Weight":
        eating_goal = "an eating goal to gain weight"
    else:
        eating_goal = "no eating to reduce weight"
    
    if sleep == "≤7h":
        sleep = "few"
    elif sleep == "7-9h":
        sleep = "enough"
    else:
        sleep = "more"
    
    if physical_activity == "A lot (>9h)":
        physical_activity = "very"
    elif physical_activity == "Average (=6h)":
        physical_activity = "Medium"
    else:
        physical_activity = "not enough"
    
    
    
    healthy_prompt =f"Generate six grammatically correct hashtags to describe {title}. To generate the hashtags emphasize the ingredients of the dish and their healthiness, the FSA score of {Fsa} (6 out of 6 - good), {calories} calories, {fat}g fat, and {protein}g protein. The explanation should convince a user with {bmi} BMI, {eating_goal}, {sleep} hours of sleep, {depression}, and {physical_activity} activity to prepare this recipe."
    
    unhealthy_prompt =f"Generate six grammatically correct hashtags to describe {title} . To generate the hashtags emphasize the ingredients of the dish and their healthiness, the FSA score of {Fsa} (10 out of 12 - bad), {calories} calories, {fat}g fat, and {protein}g protein. The explanation should discourage a user with {bmi} BMI, {eating_goal}, {sleep} hours of sleep, {depression}, and {physical_activity} activity to prepare this recipe."

    # healthy_prompt = f"Generate six grammatically correct hashtags to convince a user with a BMI of {bmi}, an eating goal to {eating_goal}, {sleep} hours of sleep, a {depression} depressed, and {physical_activity} active, to chose {title}.  Highlight the dish\'s healthy aspect, such as FSA score of {Fsa}, {calories} calories, {fat}g fat, and {protein}g protein."
    
    # unhealthy_prompt = f"Generate six grammatically correct hashtags to dissuade a user with a BMI of {bmi}, an eating goal to {eating_goal},{sleep} hours of sleep,  a {depression} depressed, and {physical_activity}  active,  from choosing  {title}. Highlight the dish\'s unhealthy aspect, such as FSA score of {Fsa}, {calories} calories, {fat}g fat, and {protein}g protein."
  
  
  
   
    
    if healthiness == 'unhealthy':
       prompt = unhealthy_prompt 
    else:
        prompt = healthy_prompt
    # print('prompt------',prompt)  
    
    chat_completion = client.chat.completions.create(
    messages=[
        
        # {
        #     "role":'system',
        #     "content": 'you are a nutritionist '
        # },
        {  
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",
    )

    hashtags = re.findall(r'#\w+', chat_completion.choices[0].message.content)
   
    
    return hashtags


# 

# 

# prompt------ Generate 6 grammatically correct hashtags to convince a user with a BMI of 24.0, an eating goal of Lose Weight, ≤7h hours of sleep, a Not at all depressed, and Average (=6h) active, to chose Moroccan Tagine a healthy recipe with an FSA score of 6, 265 calories, 0.963675413g fat, and 14.1g protein.

# prompt------ Generate 6 grammatically correct hashtags to convince a user with a BMI of 24.0, an eating goal of Lose Weight, ≤7h hours of sleep, a Not at all depressed, and Average (=6h) active, to chose Imitation Meatloaf a healthy recipe with an FSA score of 6, 331 calories, 3.867334592g fat, and 17.4g protein.

# prompt------ Generate 6 grammatically correct hashtags to convince a user with a BMI of 24.0, an eating goal of Lose Weight, ≤7h hours of sleep, a Not at all depressed, and Average (=6h) active, to chose Thai Ginger Chicken (Gai Pad King) a healthy recipe with an FSA score of 4, 491 calories, 1.96719357g fat, and 30.2g protein.

# prompt------ Generate 6 grammatically correct hashtags to convince a user with a BMI of 24.0, an eating goal of Lose Weight, ≤7h hours of sleep, a Not at all depressed, and Average (=6h) active, to chose Terry's Texas Pinto Beans a healthy recipe with an FSA score of 4, 210 calories, 0.461532813g fat, and 13.2g protein.

# prompt------ Generate 6 grammatically correct hashtags to convince a user with a BMI of 24.0, an eating goal of Lose Weight, ≤7h hours of sleep, a Not at all depressed, and Average (=6h) active, to chose Tomato-Curry Lentil Stew a healthy recipe with an FSA score of 4, 206 calories, 0.274678112g fat, and 13.7g protein.

# prompt------ Generate 6 grammatically correct hashtags to prevent a user with a BMI of 24.0, an eating goal of Lose Weight, ≤7h hours of sleep, a Not at all depressed, and Average (=6h) active, to avoid Flank Steak with Avocado Salsa an unhealthy recipe with an FSA score of 10, 540 calories, 9.565638361g fat, and 25.7g protein.

# prompt------ Generate 6 grammatically correct hashtags to prevent a user with a BMI of 24.0, an eating goal of Lose Weight, ≤7h hours of sleep, a Not at all depressed, and Average (=6h) active, to avoid Hawaiian Chicken II an unhealthy recipe with an FSA score of 10, 540 calories, 4.739843486g fat, and 24.9g protein.

# prompt------ Generate 6 grammatically correct hashtags to prevent a user with a BMI of 24.0, an eating goal of Lose Weight, ≤7h hours of sleep, a Not at all depressed, and Average (=6h) active, to avoid Very Special Spaghetti Sauce an unhealthy recipe with an FSA score of 10, 508 calories, 9.136934845g fat, and 23.5g protein.

# prompt------ Generate 6 grammatically correct hashtags to prevent a user with a BMI of 24.0, an eating goal of Lose Weight, ≤7h hours of sleep, a Not at all depressed, and Average (=6h) active, to avoid Chicken with Quinoa and Veggies an unhealthy recipe with an FSA score of 10, 453 calories, 7.026971169g fat, and 23.8g protein.

# prompt------ Generate 6 grammatically correct hashtags to prevent a user with a BMI of 24.0, an eating goal of Lose Weight, ≤7h hours of sleep, a Not at all depressed, and Average (=6h) active, to avoid Sweet and Sour Drumettes an unhealthy recipe with an FSA score of 10, 487 calories, 7.842222952g fat, and 23.0g protein.

# ['1.', '#HealthyEatingGoals', '2.', '#LetSleepBeYourFriend', '3.', '#WellnessOverCalories', '4.', '#MindfulNutritionChoices', '5.', '#StayActiveStayHealthy', '6.', '#ChooseHealthierOptions']
# [20/Nov/2024 15:21:12] "GET /recipe_recommendations HTTP/1.1" 200 37438