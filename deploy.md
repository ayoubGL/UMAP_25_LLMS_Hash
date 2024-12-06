databases:
    - llm_hashtags
    - llm_explanations;
    - llm_labels;
    _ llm_nolabels;

- service/socket
    - [x] CB_base.service --> KB_nolabel.service: 5430, [ok]        
    - [x] CB_full.service --> kB_exp.service: 5439, [ok]
    - [x] CF_boost.service --> kB_label.service: 5438, [ok]
    - [x] CB_mtl.service --> kB_hashtags.service: 5431 [ok], 


- Change home 
	[x] KB_label
	[x] KB_nolabel
	[x] KB_hashtags
	[x] KB_expl
	

- Change admin
	[x] KB_label {sustainability} 
	[x] KB_nolabel
	[x] KB_hashtags
	[x] KB_expl

- change choice , weight
	[x] KB_label 
	[x] KB_nolabel
	[x] KB_hashtags
	[x] KB_expl


- Complex:
	[x] KB_label 
	[x] KB_nolabel
	[x] KB_hashtags
	[x] KB_expl

- Add llm generated to selected

	[x] KB_hashtags
	[x] KB_expl

- Depression to deepresionL
	[x] KB_label 
	[x] KB_nolabel
	[x] KB_hashtags
	[x] KB_expl

- Finishing
	[x] KB_label 
	[x] KB_nolabel
	[x] KB_hashtags
	[x] KB_expl.        : CJL9IR62


- evaluation questionnaire: 'The explanations helps me to make the final recipe choice'
	[x] KB_expl.       
	[x] KB_hashtags
	[x] KB_label 
	[] KB_nolabel

- Please Carefully
	[x] KB_expl.       
	[x] KB_hashtags
	[x] KB_label 
	[] KB_nolabel

- Recipe number h1, unh3, h4, unh_1
	[x] KB_expl.        
	[x] KB_hashtags
	[x] KB_label 
	[x] KB_nolabel

- Consent about AI generated explanations.    
	In this study, please imagine that you are looking for a dish to prepare on a weeknight. You will be first asked about your personal preferences related to food and to provide your opinion on a few statements. Afterwards, based on your personal preferences, you will be presented a list of ten personalized recipe recommendations. From that list, please select one recipe that you like the most and would like to cook at home. Afterwards, you will be asked a few questions about the chosen recipe and the decision-making process.

	[x] KB_label
	[x] KB_nolabel  
	[x] KB_hahstags
	[x] KB_expl

- Profile builder
	Please answer the following questions about your food preferences. Your responses will be processed anonymously and cannot be traced back to you.
         Based on your profile, you will receive personalized recipe recommendations tailored to your preferences.
	- update questions:
	         
           'RecipeWebUsage': 'How frequently do you use recipe websites?',
            'HomeCook':'How frequently do you prepare home-cooked meals?',
            'CookingExp':'What is you cooking experience level?',
            'EatingGoals':'Do you have any weight-related eating goals?',
            'Depression':'To what extent are you feeling depressed?',
            'PhysicalActivity':'How much physical activity do you do in a week?',
            'SleepHours' : 'How many hours of sleep do you usually get each night?',
            'CookingTime':'How much time do you typically have available for cooking?'
	[x] KB_label
	[x] KB_nolabel  
	[x] KB_hahstags
	[x] KB_expl




- Add Eval questions and admin
	- The hashtags were easy to understand”
    - The hashtags made it easier to use the system”      
	- The hashtags helped me to understand whether the recommended recipes fitted my preferences”
	- The hashtags helped me to understand the healthiness of each recipe”
	- The hashtags helped me to choose a recipe”
	[x] KB_expl.        
	[x] KB_hashtags
	[x] KB_label 
	[x] KB_nolabel


- Change the prompt
	[x] KB_expl.        
	[x] KB_hashtags
	

 

	

 sudo systemctl restart KB_nolabel KB_label KB_hashtags KB_exp

sudo -u postgres psql


