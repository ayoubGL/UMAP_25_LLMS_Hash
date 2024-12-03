from tkinter.tix import Select
from django import forms
from django.core.exceptions import ValidationError
from django.db import close_old_connections, models
from django.db.models import fields
from django.forms import widgets
from .models import  HealthyRecipe, Personal_info, UnhealthyRecipe,EvaluateChoices, Profile
from django_starfield import Stars
from django.forms import formset_factory, modelformset_factory

class Personal_infoForm(forms.ModelForm):
    class Meta:
        model = Personal_info
        exclude = ('id', 'created', 'title', 'session_id')
        widgets = {
            'gender': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'age': forms.Select(attrs={'class': 'form-select form-select-sm clabel'}),
            'country': forms.Select(attrs={'class': 'form-select form-select-sm clabel', 'required': True}),
            'education': forms.Select(attrs={'class': 'form-select form-select-sm clabel'}),
            
            ## Food knowledge
            
            'FK_9'  : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            'FK_10' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            'FK_11' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            'FK_12' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),

            'sus_1' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            'sus_2' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            'sus_3' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            'sus_4' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            #


        }
        labels = {
            'gender': 'Gender',
            'age': 'Age',
            'country': 'Country of residence',
            'education': 'Your highest completed education',
            
            'FK_9' : 'Compared with an average person, I know a lot about healthy eating',
            'FK_10': 'I think I know enough about healthy eating to feel pretty confident when choosing a recipe',
            'FK_11': 'I know a lot about how to evaluate the healthiness of a recipe',
            'FK_12': 'I do NOT feel very knowledgeable about healthy eating',
            
            'sus_1': 'I believe that sustainable diet is important in my everyday life',
            'sus_2': 'Compared with average person, I know  about the environmental impact of food production',
            'sus_3': 'I believe that individual choices can make a difference in environmental sustainability',
            'sus_4': 'I believe that sustainable eating is complex',
        
        }



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('id', 'created', 'title', 'person')
        widgets = {
            
            ## User profile
            'Height':forms.NumberInput(attrs={ 'placeholder':'cm'}),
            'Weight':forms.NumberInput(attrs={ 'placeholder':'kg'}),
    

            
            'RecipeWebUsage': forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            'HomeCook': forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            'CookingExp':forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
             'EatingGoals':forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
             'EatingGoals':forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
             'CookingTime':forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
             
            
            
             'Mood':forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
             'PhysicalActivity':forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
             'SleepHours':forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
             'Depression':forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),


        }
        labels = {
            
            
            'RecipeWebUsage': 'Recipe website usage?',
            'HomeCook':'Frequency of preparing home-cooked meals?',
            'CookingExp':'Cooking experience?',
            'EatingGoals':'What is your eating goals?',
            'Depression':'To what extent are you feeling depressed?',
            'PhysicalActivity':'How much physical activity do you do in a week?',
            'SleepHours' : 'How many hours of sleep do you usually get?',
            'CookingTime':'The time I have  available for cooking'
        }

    







likert_scale = [ 
('1','Strongly Disagree'),
('2','Disagree'),
('3','Neutral'),
('4','Agree'),
('5','Strongly Agree')
]
popularity_stars = [
    ('3.8','3 stars'),
    ('4','4 stars'),
    ('0','No preferences')
]


class ChoiceEvaluationForm(forms.ModelForm):
    class Meta:
        model = EvaluateChoices
        exclude = ('id', 'created', 'title','person','session_id')
        widgets = {

            # choice satisfaction
            'liked_recipes': forms.Select(attrs={'class': 'form-select form-select-sm clabel', 'required': True}),
            'prepare_recipes': forms.Select(attrs={'class': 'form-select form-select-sm clabel', 'required': True}),
            'fit_preference': forms.Select(attrs={'class': 'form-select form-select-sm clabel', 'required': True}),
            'know_many': forms.Select(attrs={'class': 'form-select form-select-sm clabel', 'required': True}),
            'recommend_recipe': forms.Select(attrs={'class': 'form-select form-select-sm clabel', 'required': True}),
            
            # choice difficulty
            'many_to_choose': forms.Select(attrs={'class': 'form-select form-select-sm clabel', 'required': True}),
            'diet_restriction': forms.Select(attrs={'class': 'form-select form-select-sm clabel', 'required': True}),
            'easy_choice': forms.Select(attrs={'class': 'form-select form-select-sm clabel', 'required': True}),
            'choice_overwhelming': forms.Select(attrs={'class': 'form-select form-select-sm clabel', 'required': True}),

            # Perceived effort
            'sys_time': forms.Select(attrs={'class': 'form-select form-select-sm clabel', 'required': True}),
            'unders_sys': forms.Select(attrs={'class': 'form-select form-select-sm clabel', 'required': True}),
            'many_actions': forms.Select(attrs={'class': 'form-select form-select-sm clabel', 'required': True}),
            
            # hashtag evaluations
            'understandability':forms.Select(attrs={'class': 'form-select form-select-sm clabel', 'required': True}),
            'satisfaction':forms.Select(attrs={'class': 'form-select form-select-sm clabel', 'required': True}),
            'effectiveness':forms.Select(attrs={'class': 'form-select form-select-sm clabel', 'required': True}),
            'persuasiveness':forms.Select(attrs={'class': 'form-select form-select-sm clabel', 'required': True}),
            'nudge_eval':forms.Select(attrs={'class': 'form-select form-select-sm clabel', 'required': True}),
        }
        labels = {
            
            # Choice satisfaction 
            'liked_recipes':"I like the recipe I've chosen",
            'prepare_recipes':"I think I will prepare the recipe I've chosen",
            'fit_preference': 'The chosen recipe fits my preferences',
            'know_many': 'I know many recipes that I like more than the one I have chosen',
            'recommend_recipe': 'I would recommend the chosen recipe to others',
            
            # Choice difficulty 
            'many_to_choose': 'I changed my mind several times before making a decision ',
            'diet_restriction': 'Do you have any dietary restrictions',
            'easy_choice': 'It was easy to make this choice ',
            'choice_overwhelming': 'Making a choice was overwhelming ',

            # Perceived effort
            'sys_time':'The system takes up a lot of time',
            'unders_sys':'I quickly understood the functionalities of the system',
            'many_actions':'Many actions were required to use the system',
            
            # hashtag eval
            'understandability': 'The explanations are understandable ',
            'satisfaction': 'The explanations help to increase my satisfaction with the recommender system',
            'effectiveness': 'The explanations help me to understand to which extent the recommended recipe meets my preferences',
            'nudge_eval': 'The explanations help me understand the healthiness of the recipes',
            'persuasiveness':  'The explanations help me to make the final recipe choice'
            
            
            
        }




# Sustainabality








