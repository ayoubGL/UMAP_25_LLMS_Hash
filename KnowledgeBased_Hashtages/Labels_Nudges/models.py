from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import ChoicesMeta
from django.db.models.fields import AutoField, CharField, DateTimeField
from django.db.models.fields.related import ForeignKey
from .choices import *
from django.core.validators import MaxValueValidator, MinValueValidator
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField

# Create your models here.


class Personal_info(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=50,
        editable=False,
        default='Personal_info')

    created = models.DateTimeField(auto_now_add=True)

    age = models.CharField(max_length=120,
                           choices=Age_choices,
                           verbose_name='age',
                           default=None,
                           blank=False
                           )

    country = CountryField(blank_label='')

    education = models.CharField(max_length=120,
                                 choices=EducationLevel,
                                 verbose_name='education',
                                 default=None,
                                 blank=False

                                 )


    gender = models.CharField(max_length=300,
                              choices=Gender_choices,
                              verbose_name='gender',
                              default=None,
                              blank=False
                              )
    FK_9 =  models.CharField(max_length = 300,
                             choices = FK__choices,
                             verbose_name = 'FK_9',
                             default=None,
                             blank = False)
    FK_10 =  models.CharField(max_length = 300,
                             choices = FK__choices,
                             verbose_name = 'FK_10',
                             default=None,
                             blank = False)
    FK_11 =  models.CharField(max_length = 300,
                             choices = FK__choices,
                             verbose_name = 'FK_11',
                             default=None,
                             blank = False)
    FK_12 = models.CharField(max_length = 300,
 			    choices = FK__choices,
			  verbose_name = 'FK_12',
			default = None,
			blank = False)
    
    

    # other_diet = models.CharField(("other_diet"), max_length=50, default='0')
    session_id = models.CharField(max_length=100, blank=False, default=None)
    class Meta:
        verbose_name = 'personal_info'
        ordering = ['id']
        db_table = 'personal_info'

    def __str__(self):
        return "{}".format(self.id)
    

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(
        Personal_info,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=50,
        editable=False,
        default='Profile')
    
    Height = models.IntegerField()
    
    Weight = models.IntegerField()
    
    RecipeWebUsage =  models.CharField(max_length = 300,
 			choices = DayFrequency,
			verbose_name = 'RecipeWebUsage',
			default = None,
			blank = False)
    
    HomeCook = models.CharField(max_length = 300,
                                choices = DayFrequency,
                                verbose_name = 'HomeCook',
                                default = None,
                                blank = False
                                )
    CookingExp = models.CharField(max_length = 300,
                                choices = LowHighChoices,
                                verbose_name = 'CookingExp',
                                default = None,
                                blank = False
                                )
    EatingGoals = models.CharField(max_length = 300,
                                choices = EatingGoalsChoiecs,
                                verbose_name = 'HomeCook',
                                default = None,
                                blank = False
                                )
    Depression = models.CharField(max_length = 300,
                                choices = mood,
                                verbose_name = 'mood',
                                default = None,
                                blank = False
                                )
    PhysicalActivity = models.CharField(max_length = 300,
                                choices = PhyActi,
                                verbose_name = 'PhysicalActivity',
                                default = None,
                                blank = False
                                )
    SleepHours = models.CharField(max_length = 300,
                                choices = sleephours,
                                verbose_name = 'sleephours',
                                default = None,
                                blank = False
                                )
    CookingTime =  models.CharField(max_length = 300,
                                choices = CookingTime,
                                verbose_name = 'CookingTime',
                                default = None,
                                blank = False
                                )    


    class Meta:
        verbose_name = 'Profile'
        ordering = ['id']
        db_table = 'Profile'

    def __str__(self):
        return "{}".format(self.id)



class HealthyRecipe(models.Model):
    id =  models.AutoField(primary_key=True)
    URL  = models.CharField(max_length=1000)
    Name = models.CharField(max_length=1000)
    fiber_g  = models.CharField(max_length=1000)
    sodium_g = models.CharField(max_length=1000)
    carbohydrates_g = models.CharField(max_length=1000)
    fat_g = models.CharField(max_length=1000)
    protein_g = models.CharField(max_length=1000)
    sugar_g = models.CharField(max_length=1000)
    saturate_g = models.CharField(max_length=1000)
    size_g = models.CharField(max_length=1000)
    Servings = models.CharField(max_length=1000)
    calories_kCal = models.CharField(max_length=1000)
    category = models.CharField(max_length=1000)
    image_link = models.CharField(max_length=1000)
    fat_100g = models.CharField(max_length=1000)
    fiber_100g = models.CharField(max_length=1000)
    sugar_100g = models.CharField(max_length=1000)
    saturated_100g = models.CharField(max_length=1000)
    sodium_100mg = models.CharField(max_length=1000)
    carbohydrates_100g = models.CharField(max_length=1000)
    kj_100g = models.CharField(max_length=1000)
    Nutri_score = models.CharField(max_length=1000)
    Fsa_new = models.CharField(max_length=1000)
    salt_100g = models.CharField(max_length=1000)
    salt_g = models.CharField(max_length=1000)
    fat_count = models.CharField(max_length=1000)
    satfat_count = models.CharField(max_length=1000)
    sugar_count = models.CharField(max_length=1000)
    salt_count = models.CharField(max_length=1000)
    NumberRatings = models.CharField(max_length=1000)
    content = models.CharField(max_length=1000)
    healthiness = models.CharField(max_length=1000)
    recipe_cal = models.CharField(max_length=1000)
    recipe_cal_per = models.CharField(max_length=1000)
    recipe_col = models.CharField(max_length=1000)
    recipe_col_per = models.CharField(max_length=1000)
    recipe_fiber = models.CharField(max_length=1000)
    recipe_fiber_per = models.CharField(max_length=1000)
    recipe_sodium = models.CharField(max_length=1000)
    recipe_sodium_per = models.CharField(max_length=1000)
    recipe_carbs = models.CharField(max_length=1000)
    recipe_carbs_per = models.CharField(max_length=1000)
    recipe_fat = models.CharField(max_length=1000)
    recipe_fat_per = models.CharField(max_length=1000)
    recipe_protein = models.CharField(max_length=1000)
    recipe_protein_per = models.CharField(max_length=1000)
    recipe_serving_size = models.CharField(max_length=1000)
    recipe_serving = models.CharField(max_length=1000)
    recipe_calories = models.CharField(max_length=1000)
    recipe_calories_fat = models.CharField(max_length=1000)
    recipe_total_fat = models.CharField(max_length=1000)
    recipe_total_fat_per = models.CharField(max_length=1000)
    recipe_saturated_fat = models.CharField(max_length=1000)
    recipe_saturated_fat_unit = models.CharField(max_length=1000)
    recipe_saturated_fat_per   = models.CharField(max_length=1000)
    recipe_cholesterol  = models.CharField(max_length=1000)
    recipe_cholesterol_unit = models.CharField(max_length=1000)
    recipe_cholesterol_per = models.CharField(max_length=1000)
    recipe_sodium1 = models.CharField(max_length=1000)
    recipe_sodium1_unit = models.CharField(max_length=1000)
    recipe_sodium1_per = models.CharField(max_length=1000)
    recipe_potassium = models.CharField(max_length=1000)
    recipe_potassium_unit = models.CharField(max_length=1000)
    recipe_potassium_per = models.CharField(max_length=1000)
    recipe_carbs1 = models.CharField(max_length=1000)
    recipe_carbs1_unit = models.CharField(max_length=1000)
    recipe_carbs1_per = models.CharField(max_length=1000)
    recipe_fiber1 = models.CharField(max_length=1000)
    recipe_fiber1_unit = models.CharField(max_length=1000)
    recipe_fiber1_per = models.CharField(max_length=1000)
    recipe_prot = models.CharField(max_length=1000)
    recipe_prot_unit = models.CharField(max_length=1000)
    recipe_prot_per = models.CharField(max_length=1000)
    recipe_sugar = models.CharField(max_length=1000)
    recipe_sugar_unit = models.CharField(max_length=1000)
    recipe_vita = models.CharField(max_length=1000)
    recipe_vita_per = models.CharField(max_length=1000)
    recipe_vitc = models.CharField(max_length=1000)
    recipe_vitc_per = models.CharField(max_length=1000)
    recipe_calcium = models.CharField(max_length=1000)
    recipe_calcium_per = models.CharField(max_length=1000)
    recipe_iron = models.CharField(max_length=1000)
    recipe_iron_per = models.CharField(max_length=1000)
    recipe_thiamin = models.CharField(max_length=1000)
    recipe_thiamin_per = models.CharField(max_length=1000)
    recipe_niacin = models.CharField(max_length=1000)
    recipe_niacin_per = models.CharField(max_length=1000)
    recipe_vitb6 = models.CharField(max_length=1000)
    recipe_vitb6_per = models.CharField(max_length=1000)
    recipe_magnesium = models.CharField(max_length=1000)
    recipe_magnesium_per = models.CharField(max_length=1000)
    recipe_folate = models.CharField(max_length=1000)
    recipe_folate_per = models.CharField(max_length=1000)

    class Meta:
        verbose_name = 'HealthyRecipes'
        ordering = ['id']
        db_table = 'HealthyRecipes'
    def __str__(self):
        return self.Name

class UnhealthyRecipe(models.Model):
    id =  models.AutoField(primary_key=True)
    URL  = models.CharField(max_length=1000)
    Name = models.CharField(max_length=1000)
    fiber_g  = models.CharField(max_length=1000)
    sodium_g = models.CharField(max_length=1000)
    carbohydrates_g = models.CharField(max_length=1000)
    fat_g = models.CharField(max_length=1000)
    protein_g = models.CharField(max_length=1000)
    sugar_g = models.CharField(max_length=1000)
    saturate_g = models.CharField(max_length=1000)
    size_g = models.CharField(max_length=1000)
    Servings = models.CharField(max_length=1000)
    calories_kCal = models.CharField(max_length=1000)
    category = models.CharField(max_length=1000)
    image_link = models.CharField(max_length=1000)
    fat_100g = models.CharField(max_length=1000)
    fiber_100g = models.CharField(max_length=1000)
    sugar_100g = models.CharField(max_length=1000)
    saturated_100g = models.CharField(max_length=1000)
    sodium_100mg = models.CharField(max_length=1000)
    carbohydrates_100g = models.CharField(max_length=1000)
    kj_100g = models.CharField(max_length=1000)
    Nutri_score = models.CharField(max_length=1000)
    Fsa_new = models.CharField(max_length=1000)
    salt_100g = models.CharField(max_length=1000)
    salt_g = models.CharField(max_length=1000)
    fat_count = models.CharField(max_length=1000)
    satfat_count = models.CharField(max_length=1000)
    sugar_count = models.CharField(max_length=1000)
    salt_count = models.CharField(max_length=1000)
    NumberRatings = models.CharField(max_length=1000)
    content = models.CharField(max_length=1000)
    healthiness = models.CharField(max_length=1000)
    recipe_cal = models.CharField(max_length=1000)
    recipe_cal_per = models.CharField(max_length=1000)
    recipe_col = models.CharField(max_length=1000)
    recipe_col_per = models.CharField(max_length=1000)
    recipe_fiber = models.CharField(max_length=1000)
    recipe_fiber_per = models.CharField(max_length=1000)
    recipe_sodium = models.CharField(max_length=1000)
    recipe_sodium_per = models.CharField(max_length=1000)
    recipe_carbs = models.CharField(max_length=1000)
    recipe_carbs_per = models.CharField(max_length=1000)
    recipe_fat = models.CharField(max_length=1000)
    recipe_fat_per = models.CharField(max_length=1000)
    recipe_protein = models.CharField(max_length=1000)
    recipe_protein_per = models.CharField(max_length=1000)
    recipe_serving_size = models.CharField(max_length=1000)
    recipe_serving = models.CharField(max_length=1000)
    recipe_calories = models.CharField(max_length=1000)
    recipe_calories_fat = models.CharField(max_length=1000)
    recipe_total_fat = models.CharField(max_length=1000)
    recipe_total_fat_per = models.CharField(max_length=1000)
    recipe_saturated_fat = models.CharField(max_length=1000)
    recipe_saturated_fat_unit = models.CharField(max_length=1000)
    recipe_saturated_fat_per   = models.CharField(max_length=1000)
    recipe_cholesterol  = models.CharField(max_length=1000)
    recipe_cholesterol_unit = models.CharField(max_length=1000)
    recipe_cholesterol_per = models.CharField(max_length=1000)
    recipe_sodium1 = models.CharField(max_length=1000)
    recipe_sodium1_unit = models.CharField(max_length=1000)
    recipe_sodium1_per = models.CharField(max_length=1000)
    recipe_potassium = models.CharField(max_length=1000)
    recipe_potassium_unit = models.CharField(max_length=1000)
    recipe_potassium_per = models.CharField(max_length=1000)
    recipe_carbs1 = models.CharField(max_length=1000)
    recipe_carbs1_unit = models.CharField(max_length=1000)
    recipe_carbs1_per = models.CharField(max_length=1000)
    recipe_fiber1 = models.CharField(max_length=1000)
    recipe_fiber1_unit = models.CharField(max_length=1000)
    recipe_fiber1_per = models.CharField(max_length=1000)
    recipe_prot = models.CharField(max_length=1000)
    recipe_prot_unit = models.CharField(max_length=1000)
    recipe_prot_per = models.CharField(max_length=1000)
    recipe_sugar = models.CharField(max_length=1000)
    recipe_sugar_unit = models.CharField(max_length=1000)
    recipe_vita = models.CharField(max_length=1000)
    recipe_vita_per = models.CharField(max_length=1000)
    recipe_vitc = models.CharField(max_length=1000)
    recipe_vitc_per = models.CharField(max_length=1000)
    recipe_calcium = models.CharField(max_length=1000)
    recipe_calcium_per = models.CharField(max_length=1000)
    recipe_iron = models.CharField(max_length=1000)
    recipe_iron_per = models.CharField(max_length=1000)
    recipe_thiamin = models.CharField(max_length=1000)
    recipe_thiamin_per = models.CharField(max_length=1000)
    recipe_niacin = models.CharField(max_length=1000)
    recipe_niacin_per = models.CharField(max_length=1000)
    recipe_vitb6 = models.CharField(max_length=1000)
    recipe_vitb6_per = models.CharField(max_length=1000)
    recipe_magnesium = models.CharField(max_length=1000)
    recipe_magnesium_per = models.CharField(max_length=1000)
    recipe_folate = models.CharField(max_length=1000)
    recipe_folate_per = models.CharField(max_length=1000)

    class Meta:
        verbose_name = 'UnhealthyRecipes'
        ordering = ['id']
        db_table = 'UnhealthyRecipes'
    def __str__(self):
        return self.Name



class Recommendations(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(
        Personal_info,
        on_delete=models.CASCADE)
    recommended_recipes = models.CharField(max_length=500)
    healthiness = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)




class SelectedRecipe(models.Model):
    id = models.AutoField(primary_key = True)

    person = models.ForeignKey(
        Personal_info,
        blank=False,
        on_delete=models.CASCADE
    )  
    recipe_id = models.IntegerField()  # recipe id that will be saved only
    recipe_name = models.CharField(max_length=200)

    Nutri_score = models.CharField(max_length= 100)
    fsa_score = models.CharField(max_length=100)

    healthiness = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=100, blank=False, default=None)
    def __str__(self):
        return self.healthiness
    class Meta:
        unique_together = ('person','recipe_id')
        verbose_name = 'selectedRecipe'
        db_table  ='selectedrecipe'


class EvaluateChoices(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=50,
        editable=False,
        default='EvaluateChoices')

    person = models.ForeignKey(
        Personal_info,
        on_delete=models.CASCADE
    )

    liked_recipes = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='liked_recipes',
        default=None,
        blank=False
    )
    prepare_recipes = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='prepare_recipes',
        default=None,
        blank=False
    )
    fit_preference = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='fit_preference',
        default=None,
        blank=False
    )
    know_many = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='know_many',
        default=None,
        blank=False
    )
    recommend_recipe = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='recommend_recipe',
        default=None,
        blank=False
    )

#--- choice difficulty-------

    many_to_choose = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='many_to_choose',
        default=None,
        blank=False
    )
    easy_choice = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='easy_choice',
        default=None,
        blank=False
    )
    choice_overwhelming = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='choice_overwhelming',
        default=None,
        blank=False
    )
    
    # --- system effort
    sys_time = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='sys_time',
        default=None,
        blank=False
    )
    unders_sys = models.CharField(max_length=100,
    choices=FK__choices,
    verbose_name='unders_sys',
    default=None,
    blank=False
    )
    many_actions = models.CharField(max_length=100,
    choices=FK__choices,
    verbose_name='many_actions',
    default=None,
    blank=False
    )
# -- hashtag evaluations

    understandability = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='understandability',
        default=None,
        blank=False
    )
    satisfaction = models.CharField(max_length=100,
    choices=FK__choices,
    verbose_name='satisfaction',
    default=None,
    blank=False
    )
    effectiveness = models.CharField(max_length=100,
    choices=FK__choices,
    verbose_name='effectiveness',
    default=None,
    blank=False
    )
    persuasiveness = models.CharField(max_length=100,
    choices=FK__choices,
    verbose_name='persuasiveness',
    default=None,
    blank=False
    )




    created = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=100, blank=False, default=None)
    #prolific_id = models.CharField(max_length=100, blank=False, default=None)
    class Meta:
        verbose_name = 'EvaluateChoices'
        ordering = ['id']
        db_table = 'EvaluateChoices'

    def __str__(self):
        return "{}".format(self.id)























# class user_rate(models.Model):
#     id = models.AutoField(primary_key=True)
#     person = models.ForeignKey(
#         Personal_info,
#         blank=False,
#         on_delete=models.CASCADE
#     )
#     recipe = models.ForeignKey(
#         Recipes,
#         # blank=False,
#         on_delete=models.CASCADE
#     )

#     recipe_rating = models.IntegerField(
#         validators=[MinValueValidator(0), MaxValueValidator(5)], blank=False, default=0)

#     created = models.DateTimeField(auto_now_add=True)

#     # def __str__(self):
#     #     return self.recipe.id
#     class Meta:
#         unique_together = (('recipe','person'))
#         verbose_name = 'user_rate'
#         db_table = 'user_ratings'


class FoodCategory(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(
        Personal_info,
        on_delete=models.CASCADE
    )

    category = models.CharField(("Category"),
                                max_length=50,
                                choices=foodCategories,
                                blank=False,
                                default=None)
    
    recipe_popularity = models.CharField(("recipe_popularity"),
                                max_length=50,
                                # choices=likert_scale,
                                blank=False,
                                default=None)
    
    calories = models.IntegerField(
                                   validators=[MinValueValidator(200),
                                    MaxValueValidator(1000),], )
    
    
    recipe_size = models.IntegerField(
                                   validators=[MinValueValidator(1),
                                    MaxValueValidator(10),], )

    preparation_time = models.IntegerField(
                                   validators=[MinValueValidator(15),
                                    MaxValueValidator(60),], )
    
    n_ingredient = models.IntegerField(
                                   validators=[MinValueValidator(3),
                                    MaxValueValidator(10),], )


    created = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=100, blank=False, default=None)
    class Meta:
        verbose_name = 'FoodCategory'
        ordering = ['id']
        db_table = 'FoodCategory'
