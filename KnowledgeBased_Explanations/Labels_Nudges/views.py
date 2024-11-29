from django.forms import formset_factory
from django.db.models import Count
import datetime
import pandas as pd
from random import choice, sample
import random
from sys import prefix
from django import forms
from django.db import reset_queries
from django.forms.models import ModelForm
from django.http import request
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from pandas.core.indexes import category

from Labels_Nudges.app import get_top_recommendations, get_explanation
from .forms import Personal_infoForm,  ChoiceEvaluationForm, ProfileForm
# from django.forms import formset_factory, modelformset_factory
from .models import  Personal_info, HealthyRecipe, UnhealthyRecipe, SelectedRecipe,EvaluateChoices, Recommendations, Profile
# from .app import *
# Create your views here.
# person_id = 0
import string
import random
#<<<<<<< HEAD
import re 


def home(request):
    request.session['person_id'] = 0
    #prolific_id = , msg)
    #prolific_id = str(prolific_id.group(1))
    full_url = request.get_full_path()
    #request.GET['PROLIFIC_PID']
    print('Full',request.get_full_path())
    #print(full_url)
    if 'PROLIFIC_PID' in full_url:
        prolific_id = re.search("PROLIFIC_PID=(.*?)&STUDY_ID",full_url)
        print('Idd----',prolific_id)
        request.session['prolific_id'] = str(prolific_id.group(1))
        #print("----------",prolific_id.group(1))
    else:
        request.session['prolific_id'] = '000'
    return render(request, 'Labels_Nudges/homes.html')




def personal_info(request):
    user_selected = Personal_info.objects.filter(id = request.session['person_id'])
    if user_selected:
        Personal_info.objects.filter(id=request.session['person_id']).delete()
    if request.method == 'POST':
        personl_info = Personal_infoForm(request.POST)
        if personl_info.is_valid():
            answer = personl_info.save(commit=False)
            
            rd_str =''.join(random.choice(string.ascii_lowercase) for _ in range(5))
            time_now = datetime.datetime.now().strftime('%H%M%S')
            gene_session = 'dars'+time_now +'_'+str(answer.id)+rd_str
            personl_info.instance.session_id = gene_session

            answer = personl_info.save(commit=True)
            
            request.session['person_id'] = answer.id
            gene_session = 'dars'+time_now +'_'+str(answer.id)+rd_str
            personl_info.instance.session_id = request.session['prolific_id']
            
            request.session['session_id'] = gene_session
            answer = personl_info.save(commit=True)

            request.session['person_id'] = answer.id
            return redirect('Labels_Nudges:profileBuilder')
    else:
        personl_info = Personal_infoForm()
    return render(request, 'Labels_Nudges/personal_info.html', context={'form': personl_info})


def profileBuilder(request):
    user_selected = Profile.objects.filter(person_id = request.session['person_id'])
    if user_selected:
        Profile.objects.filter(person_id=request.session['person_id']).delete()
  
    if request.method == 'POST':
        profile_Form = ProfileForm(request.POST)
        person = request.session['person_id']
        ProfileM = Profile()
        if profile_Form.is_valid():
            # print("-----------here we are")
            # ChoiceEvaltion.person = request.session['person_id']
            profile_ = profile_Form.save(commit=False)
            profile_.person_id = person
            # ChoiceEvaltion.person_id = profile_form.foriengkey
            # profile_.session_id = request.session['prolific_id']
            profile_.save()
            return redirect('Labels_Nudges:recipe_recommendations')
    else:
         profile_Form = ProfileForm()
    return render(request, 'Labels_Nudges/ProfileBuilder.html', context={'form': profile_Form})










def random_recipes(category):
    size = len(HealthyRecipe.objects.filter(category = category))
    ten_pr = size // 10
    if ten_pr < 5:
        ten_pr = size // 2
    h_recipes = HealthyRecipe.objects.filter(category = category).order_by('-NumberRatings').values_list('id', flat=True)[:ten_pr]
    uh_recipes = UnhealthyRecipe.objects.filter(category = category).order_by('-NumberRatings').values_list('id',flat=True)[:ten_pr]
    # print(f'len ------------------------- {len(h_recipes)} {size}')
    # unh_recipes = UnhealthyRecipe.objects.filter(category = category).order_by('-NumberRatings').values_list('id', flat=True)[:ten_pr]
    h_5 = sample(list(h_recipes), 5)
    uh_5 = sample(list(uh_recipes),5)
    return h_5, uh_5




# --- Boost presentation -------
def nutrition_labels(request): 
    if request.method == "POST":
            return redirect('Labels_Nudges:recipe_recommendations')
    else:        
            return render(request, 'Labels_Nudges/boost.html')



def mtl_color(cnt):
    colors = ['green','orange','red']
    level = ['Low','Medium','High']
            # 5 salts (color, level)
    return [ (colors[cnt[0]-1], level[cnt[0]-1]), (colors[cnt[1]-1], level[cnt[1]-1]), (colors[cnt[2]-1], level[cnt[2]-1]), (colors[cnt[3]-1], level[cnt[3]-1]), (colors[cnt[4]-1], level[cnt[4]-1])    ]


def recipe_recommendations(request):

        # add rating of current user to rating matrix
    person = request.session['person_id']

    

    # extract the user input and food category
    
    real_user_input = Profile.objects.filter(
        person_id = person
    ).values_list('Height','Weight','CookingExp','EatingGoals','SleepHours','PhysicalActivity','Depression','CookingTime')
    
    # user profile 
    
    # Height = real_user_input[]
    
    # {'BMI': 'LowCalories', 'CookingExp': 'Low', 'eatingGoals': 'No Goal', 'sleep': '≤7h', 'behaviour': 'Average (=6h)', 'depression': 'Not at all', 'cookingTime': '30-60min'}
    
    height, weight, cookingExp, eatingGoals,sleep, behavior,  depression, cookingTime= real_user_input[0][0],real_user_input[0][1],real_user_input[0][2],real_user_input[0][3],real_user_input[0][4],real_user_input[0][5], real_user_input[0][6], real_user_input[0][7]
    
    BMI = weight//(height/100)**2
    user_bmi = BMI
    user_eating_goals = eatingGoals
    user_sleep = sleep
    user_behavior = behavior
    user_depression = depression
    
    # print(BMI, user_bmi, '<----------')
    
    if BMI <= 18:
        BMIL = ['HighCalories','HighCarb','HighProtein']
    elif BMI > 19 and BMI <= 24:
        BMIL = ['NormalCalories','NormalCarbs','NormalProtein']
    else:
        BMIL = ['LowCalories','LowCarbs','LowProtein']

    
    if eatingGoals == 'GainWeight':
        eating_goalL = ['HighCalories','HighFat']
    elif eatingGoals == 'NoGoal':
        eating_goalL = ['NormalCalories','LowFat']
    else :
        eating_goalL = ['LowCalories','LowFat']

    
    if behavior == 'A lot 9h':
        behaviorL = ['HighProtein','HighCalories']
    elif behavior == 'Average (=6h)':
        behaviorL = ['NormalProtein','NormalCalories']
    else:
        behaviorL = ['NormalProtein','NormalCalories']

        
    if sleep == '≤7h':
        sleepL = [ 'HighMagn','HighFiber','HighProtein','HighVitB','LowFat']
    elif sleep == 'Average (=6h)':
        sleepL= ['NormalMagn','NormalFiber','NormalProtein','NormalVitB','NormalFat']
    else:
        sleepL = [ 'LowMagn','NormalFiber','NormalProtein','LowVitB','NormalFat']

    
    if  depression == 'Quite a lot':
        depressionL = ['HighProtein', 'LowCarbs']
    elif depression == 'Not at all':
        depressionL =  ['NormalProtein', 'NormalCarbs']
    else:
        depressionL =  ['NormalProtein', 'NormalCarbs']
        
    if  cookingTime == '≤30min':
        CookingTimeL = [0,30]
    
    elif cookingTime == '30-60min':
        CookingTimeL = [30,60]
    else:
        CookingTimeL = [60,1000]
    
    if  cookingExp == 'Low' or cookingExp == 'Very Low':
        cookingExpL = ['Simple','LowIngredient']
    elif cookingExp == 'Medium':
        cookingExpL = ['Simple','NormalIngredient']
    else:
        cookingExpL = ['complexe','HighIngredient']
        
    
    
    
    
    BMI='HighCalories' if BMI < 25     else 'LowCalories'
 
        
        
    user_preferences = {
        'BMI':BMIL,
        'CookingExp':cookingExpL,
        'eatingGoals':eating_goalL,
        'sleep':sleepL,
        'behaviour':behaviorL,
        'depression':depressionL,
        'cookingTime':CookingTimeL   
    }
    
  

    KB_explanation_user_= {
        'user_bmi' : user_bmi,
        'sleep': user_sleep,
        'behavior':behavior,
        'depression': user_depression,
        'eating_goals': user_eating_goals,
    }
    # print('------------',KB_explanation_user_)
    

    healthyRecommendations_id = get_top_recommendations(user_preferences, 'H')
    UnhealthyRecommendations_id = get_top_recommendations(user_preferences, 'U')

    
    
    

    # get recommendation
    recom_size = 5
    htop_n_for_target_user = healthyRecommendations_id
    
    unhtop_n_for_target_user  = UnhealthyRecommendations_id
 
    id_h_recipes = [] 


    [id_h_recipes.append(int(i)) for i in htop_n_for_target_user]

    id_unh_recipes = []
    [id_unh_recipes.append(int(i)) for i in unhtop_n_for_target_user]

    
#  Extract recipes


    # extract 5 healthy recipes
    h_0_recipe = HealthyRecipe.objects.get(id=id_h_recipes[0])
    h_1_recipe = HealthyRecipe.objects.get(id=id_h_recipes[1])
    h_2_recipe = HealthyRecipe.objects.get(id=id_h_recipes[2])
    h_3_recipe = HealthyRecipe.objects.get(id=id_h_recipes[3])
    h_4_recipe = HealthyRecipe.objects.get(id=id_h_recipes[4])
    # extract 5 unhhealthy recipes
    unh_0_recipe = UnhealthyRecipe.objects.get(id=id_unh_recipes[0])
    unh_1_recipe = UnhealthyRecipe.objects.get(id=id_unh_recipes[1])
    unh_2_recipe = UnhealthyRecipe.objects.get(id=id_unh_recipes[2])
    unh_3_recipe = UnhealthyRecipe.objects.get(id=id_unh_recipes[3])
    unh_4_recipe = UnhealthyRecipe.objects.get(id=id_unh_recipes[4])
    
    # selected recipe model
    selected_recipe = SelectedRecipe() 
    
    
 
    
    # get healthy explanation
    h_0_features = {
        'title': h_0_recipe.Name,
        'fsa_score':h_0_recipe.Fsa_new, 
        'calories':h_0_recipe.calories_kCal,
        'fat':h_0_recipe.fat_100g,
        'protein':h_0_recipe.protein_g,
    }
    h_1_features = {
        'title': h_1_recipe.Name,
        'fsa_score':h_1_recipe.Fsa_new, 
        'calories':h_1_recipe.calories_kCal,
        'fat':h_1_recipe.fat_100g,
        'protein':h_1_recipe.protein_g,
    }
    h_2_features = {
        'title': h_2_recipe.Name,
        'fsa_score':h_2_recipe.Fsa_new, 
        'calories':h_2_recipe.calories_kCal,
        'fat':h_2_recipe.fat_100g,
        'protein':h_2_recipe.protein_g,
    }
    h_3_features = {
        'title': h_3_recipe.Name,
        'title': h_0_recipe.Name,
        'fsa_score':h_3_recipe.Fsa_new, 
        'calories':h_3_recipe.calories_kCal,
        'fat':h_3_recipe.fat_100g,
        'protein':h_3_recipe.protein_g,
    }
    h_4_features = {
        'title': h_3_recipe.Name,
        'fsa_score':h_4_recipe.Fsa_new, 
        'calories':h_4_recipe.calories_kCal,
        'fat':h_4_recipe.fat_100g,
        'protein':h_4_recipe.protein_g,
    }
    
    h_0_explanation = get_explanation(KB_explanation_user_, h_0_features, 'healthy')
    h_1_explanation = get_explanation(KB_explanation_user_, h_1_features, 'healthy')
    h_2_explanation = get_explanation(KB_explanation_user_, h_2_features, 'healthy')
    h_3_explanation = get_explanation(KB_explanation_user_, h_3_features, 'healthy')
    h_4_explanation = get_explanation(KB_explanation_user_, h_4_features, 'healthy')
    
    
    # get unhealthy explanation
    unh_0_features = {
        'title': unh_0_recipe.Name,
        'fsa_score':unh_0_recipe.Fsa_new, 
        'calories':unh_0_recipe.calories_kCal,
        'fat':unh_0_recipe.fat_100g,
        'protein':unh_0_recipe.protein_g,
    }
    unh_1_features = {
        'title': unh_1_recipe.Name,
        'fsa_score':unh_1_recipe.Fsa_new, 
        'calories':unh_1_recipe.calories_kCal,
        'fat':unh_1_recipe.fat_100g,
        'protein':unh_1_recipe.protein_g,
    }
    unh_2_features = {
        'title': unh_2_recipe.Name,
        'fsa_score':unh_2_recipe.Fsa_new, 
        'calories':unh_2_recipe.calories_kCal,
        'fat':unh_2_recipe.fat_100g,
        'protein':unh_2_recipe.protein_g,
    }
    unh_3_features = {
        'title': unh_3_recipe.Name,
        'fsa_score':unh_3_recipe.Fsa_new, 
        'calories':unh_3_recipe.calories_kCal,
        'fat':unh_3_recipe.fat_100g,
        'protein':unh_3_recipe.protein_g,
    }
    unh_4_features = {
        'title': unh_4_recipe.Name,
        'fsa_score':unh_4_recipe.Fsa_new, 
        'calories':unh_4_recipe.calories_kCal,
        'fat':unh_4_recipe.fat_100g,
        'protein':unh_4_recipe.protein_g,
    }
    
    unh_0_explanation = get_explanation(KB_explanation_user_, unh_0_features, 'unhealthy')
    unh_1_explanation = get_explanation(KB_explanation_user_, unh_1_features, 'unhealthy')
    unh_2_explanation = get_explanation(KB_explanation_user_, unh_2_features, 'unhealthy')
    unh_3_explanation = get_explanation(KB_explanation_user_, unh_3_features, 'unhealthy')
    unh_4_explanation = get_explanation(KB_explanation_user_, unh_4_features, 'unhealthy')
    
    print(unh_0_explanation)
    # ,unh_1_hashtags,unh_2_hashtags,unh_3_hashtags,unh_4_hashtags)
    
    # initialise healthy forms with extracted data
    if request.method == "POST":
                # if the user already select a recipe
        person = request.session['person_id']
        user_selected = SelectedRecipe.objects.filter(person_id = person)
        if user_selected:
            SelectedRecipe.objects.filter(person_id=person).delete()

        user_selected = Recommendations.objects.filter(person_id = request.session['person_id'])
        if user_selected:
            Recommendations.objects.filter(person_id=request.session['person_id']).delete()


        # print('Request POST------------',request.POST)
        recipe_name = request.POST.get('recipe_name')
        recipe_id = request.POST.get('recipe_id')
        recipe_h  = request.POST.get('healthiness')
        recipe_exp = request.POST.get('expl')

        if recipe_h == 'healthy':
            nutri__fsa = HealthyRecipe.objects.filter(id=recipe_id).values_list('Nutri_score','Fsa_new')
        else:
            nutri__fsa = UnhealthyRecipe.objects.filter(id=recipe_id).values_list('Nutri_score','Fsa_new')
        selected_recipe.Nutri_score = nutri__fsa[0][0]
        selected_recipe.fsa_score = nutri__fsa[0][1]
        selected_recipe.person_id= person
        selected_recipe.recipe_name = recipe_name
        selected_recipe.recipe_id = recipe_id
        selected_recipe.healthiness = recipe_h
        selected_recipe.llm_explanation = recipe_exp
        selected_recipe.session_id = request.session['session_id']
        selected_recipe.save()

    # save recommendations
        h_recommendations = Recommendations()
        h_recommendations.person_id = person
        h_recommendations.recommended_recipes = [h_0_recipe.id,h_1_recipe.id,h_2_recipe.id,h_3_recipe.id,h_4_recipe.id]
        h_recommendations.llm_nudges = [h_0_explanation,h_1_explanation,h_2_explanation,h_3_explanation,h_4_explanation]
        h_recommendations.healthiness = 'Healthy'
        h_recommendations.save()

        unh_recommendations = Recommendations()
        unh_recommendations.person_id = person
        unh_recommendations.recommended_recipes = [unh_0_recipe.id,unh_1_recipe.id,unh_2_recipe.id,unh_3_recipe.id,unh_4_recipe.id]
        unh_recommendations.llm_nudges = [unh_0_explanation,unh_1_explanation,unh_2_explanation,unh_3_explanation,unh_4_explanation]
        unh_recommendations.healthiness = 'Unhealthy'
        unh_recommendations.save()

        return redirect('Labels_Nudges:choice_evaluation')
    else:
      
        
        h_0 = [h_0_recipe.Name, id_h_recipes[0], 'healthy', h_0_recipe.image_link, int(float(h_0_recipe.calories_kCal)),
                                 int(float(h_0_recipe.Servings)),int(float(h_0_recipe.size_g) // float(h_0_recipe.Servings)), h_0_recipe.salt_g,h_0_recipe.sugar_g,h_0_recipe.fat_g,h_0_recipe.saturate_g]
        
        h_1 = [h_1_recipe.Name, id_h_recipes[1], 'healthy', h_1_recipe.image_link, int(float(h_1_recipe.calories_kCal)),
                                 int(float(h_1_recipe.Servings)),int(float(h_1_recipe.size_g) // float(h_1_recipe.Servings)), h_1_recipe.salt_g,h_1_recipe.sugar_g,h_1_recipe.fat_g,h_1_recipe.saturate_g]
        
        h_2 = [h_2_recipe.Name, id_h_recipes[2], 'healthy', h_2_recipe.image_link, int(float(h_2_recipe.calories_kCal)), 
                               int(float(h_2_recipe.Servings)),int(float(h_2_recipe.size_g) // float(h_2_recipe.Servings)), h_2_recipe.salt_g,h_2_recipe.sugar_g,h_2_recipe.fat_g,h_2_recipe.saturate_g]
        
        h_3 = [h_3_recipe.Name, id_h_recipes[3], 'healthy', h_3_recipe.image_link, int(float(h_3_recipe.calories_kCal)),
                                 int(float(h_3_recipe.Servings)),int(float(h_3_recipe.size_g) // float(h_3_recipe.Servings)), h_3_recipe.salt_g,h_3_recipe.sugar_g,h_3_recipe.fat_g,h_3_recipe.saturate_g]
        
        h_4 = [h_4_recipe.Name, id_h_recipes[4], 'healthy', h_4_recipe.image_link, int(float(h_4_recipe.calories_kCal)), 
                                int(float(h_4_recipe.Servings)),int(float(h_4_recipe.size_g) // float(h_4_recipe.Servings)), h_4_recipe.salt_g,h_4_recipe.sugar_g,h_4_recipe.fat_g,h_4_recipe.saturate_g]
        
        
     
        

        h_salt =[int(float(h_0_recipe.salt_count)),int(float(h_1_recipe.salt_count)),int(float(h_2_recipe.salt_count)),int(float(h_3_recipe.salt_count)),int(float(h_4_recipe.salt_count))]
        h_sugar = [int(float(h_0_recipe.sugar_count)),int(float(h_1_recipe.sugar_count)),int(float(h_2_recipe.sugar_count)), int(float(h_3_recipe.sugar_count)), int(float(h_4_recipe.sugar_count))]
        h_fat =[int(float(h_0_recipe.fat_count)), int(float(h_1_recipe.fat_count)), int(float(h_2_recipe.fat_count)),int(float(h_3_recipe.fat_count)),int(float(h_4_recipe.fat_count))]
        h_satfat =[ int(float(h_0_recipe.satfat_count)),int(float(h_1_recipe.satfat_count)),int(float(h_2_recipe.satfat_count)),int(float(h_3_recipe.satfat_count)), int(float(h_4_recipe.satfat_count))]


        salt_h = [mtl_color(h_salt),h_0[7], h_1[7], h_2[7], h_3[7], h_4[7]] 
        sugar_h = [ mtl_color(h_sugar),h_0[8],h_1[8], h_2[8], h_3[8], h_4[8]] 
        fat_h = [mtl_color(h_fat),h_0[9], h_1[9], h_2[9], h_3[9], h_4[9]] 
        satfat_h = [ mtl_color(h_satfat),h_0[10], h_1[10], h_2[10], h_3[10], h_4[10]]



        unh_0 = [unh_0_recipe.Name, id_unh_recipes[0], 'unhealthy', unh_0_recipe.image_link, int(float(unh_0_recipe.calories_kCal)), int(float(unh_0_recipe.Servings)),int(float(unh_0_recipe.size_g) // float(unh_0_recipe.Servings)),unh_0_recipe.salt_g,unh_0_recipe.sugar_g,unh_0_recipe.fat_g,unh_0_recipe.saturate_g]
       
        unh_1 = [unh_1_recipe.Name, id_unh_recipes[1], 'unhealthy', unh_1_recipe.image_link, int(float(unh_1_recipe.calories_kCal)),int(float(unh_1_recipe.Servings)),int(float(unh_1_recipe.size_g) // float(unh_1_recipe.Servings)),unh_1_recipe.salt_g,unh_1_recipe.sugar_g,unh_1_recipe.fat_g,unh_1_recipe.saturate_g]
       
        unh_2 = [unh_2_recipe.Name, id_unh_recipes[2], 'unhealthy', unh_2_recipe.image_link, int(float(unh_2_recipe.calories_kCal)), int(float(unh_2_recipe.Servings)),int(float(unh_3_recipe.size_g) // float(unh_3_recipe.Servings)),unh_2_recipe.salt_g,unh_2_recipe.sugar_g,unh_2_recipe.fat_g,unh_2_recipe.saturate_g]
       
        unh_3 = [unh_3_recipe.Name, id_unh_recipes[3], 'unhealthy', unh_3_recipe.image_link, int(float(unh_3_recipe.calories_kCal)), int(float(unh_3_recipe.Servings)),int(float(unh_3_recipe.size_g) // float(unh_3_recipe.Servings)),unh_3_recipe.salt_g,unh_3_recipe.sugar_g,unh_3_recipe.fat_g,unh_3_recipe.saturate_g]
       
        unh_4 = [unh_4_recipe.Name, id_unh_recipes[4], 'unhealthy', unh_4_recipe.image_link, int(float(unh_4_recipe.calories_kCal)), int(float(unh_4_recipe.Servings)),int(float(unh_4_recipe.size_g) // float(unh_4_recipe.Servings)),unh_4_recipe.salt_g,unh_4_recipe.sugar_g,unh_4_recipe.fat_g,unh_4_recipe.saturate_g]
        
    
        unh_salt =[int(float(unh_0_recipe.salt_count)),int(float(unh_1_recipe.salt_count)),int(float(unh_2_recipe.salt_count)),int(float(unh_3_recipe.salt_count)),int(float(unh_4_recipe.salt_count))]
        unh_sugar = [int(float(unh_0_recipe.sugar_count)),int(float(unh_1_recipe.sugar_count)),int(float(unh_2_recipe.sugar_count)), int(float(unh_3_recipe.sugar_count)), int(float(unh_4_recipe.sugar_count))]
        unh_fat =[int(float(unh_0_recipe.fat_count)), int(float(unh_1_recipe.fat_count)), int(float(unh_2_recipe.fat_count)),int(float(unh_3_recipe.fat_count)),int(float(unh_4_recipe.fat_count))]
        unh_satfat =[ int(float(unh_0_recipe.satfat_count)),int(float(unh_1_recipe.satfat_count)),int(float(unh_2_recipe.satfat_count)),int(float(unh_3_recipe.satfat_count)), int(float(unh_4_recipe.satfat_count))]
        
        


        salt_unh = [mtl_color(unh_salt),unh_0[7],unh_1[7],unh_2[7],unh_3[7],unh_4[7]] 
        sugar_unh = [ mtl_color(unh_sugar),unh_0[8],unh_1[8],unh_2[8],unh_3[8],unh_4[8]] 
        fat_unh = [mtl_color(unh_fat),unh_0[9],unh_1[9],unh_2[9],unh_3[9],unh_4[9]] 
        satfat_unh = [ mtl_color(unh_satfat),unh_0[10],unh_1[10],unh_2[10],unh_3[10],unh_4[10]] 

    # send forms
    return render(request,'Labels_Nudges/recipe_recommendations.html',context={'h_':htop_n_for_target_user, 
                                                'unh_':unhtop_n_for_target_user,
                                                'h_0':h_0,
                                                'h_0_explanation':h_0_explanation,
                                                'h_1':h_1,
                                                'h_1_explanation':h_1_explanation,
                                                'h_2':h_2,
                                                'h_2_explanation':h_2_explanation,
                                                'h_3':h_3,
                                                'h_3_explanation':h_3_explanation,
                                                'h_4':h_4,
                                                'h_4_explanation':h_4_explanation,
                                                'unh_0':unh_0,
                                                'unh_0_explanation':unh_0_explanation,
                                                'unh_1':unh_1,
                                                'unh_1_explanation':unh_1_explanation,
                                                'unh_2':unh_2,
                                                'unh_2_explanation':unh_2_explanation,
                                                'unh_3':unh_3,
                                                'unh_3_explanation':unh_3_explanation,
                                                'unh_4':unh_4,
                                                'unh_4_explanation':unh_4_explanation,
                                                'h_salt':salt_h,
                                                'h_sugar':sugar_h,
                                                'h_fat':fat_h,
                                                'h_satfat':satfat_h,
                                                'unh_salt':salt_unh,
                                                'unh_sugar':sugar_unh,
                                                'unh_fat':fat_unh,
                                                'unh_satfat':satfat_unh
   
                                                })


def choice_evaluation(request):
    user_selected = EvaluateChoices.objects.filter(person_id = request.session['person_id'])
    if user_selected:
        EvaluateChoices.objects.filter(person_id=request.session['person_id']).delete()
  
    if request.method == 'POST':
        evaluation_form = ChoiceEvaluationForm(request.POST)
        person = request.session['person_id']
        ChoiceEvaltion = EvaluateChoices()
        if evaluation_form.is_valid():
            # print("-----------here we are")
            # ChoiceEvaltion.person = request.session['person_id']
            evaluation_ = evaluation_form.save(commit=False)
            evaluation_.person_id = person
            # ChoiceEvaltion.person_id = evaluation_form.foriengkey
            evaluation_.session_id = request.session['prolific_id']
#<<<<<<< HEAD
#=======
            #evaluation_.prolific_id = request.session['prolific_id']
#>>>>>>> e60f18877d25637f05dff25cde799b8906f7dcab
            evaluation_.save()
            return redirect('Labels_Nudges:thank_u')
    else:
         evaluation_form = ChoiceEvaluationForm()
    return render(request, 'Labels_Nudges/choice_evaluation.html', context={'eval_form': evaluation_form})

def thank_u(request):
    return render(request, 'Labels_Nudges/thanks.html', context={'session_id':request.session['session_id']})

def error_404(request,exception):
    data = {}
    return render(request, 'Labels_Nudges/404.html',data)
def error_500(request):
        data = {}
        return render(request,'Labels_Nudges/404.html', data)





