databases:
    - llm_hashtags
    - llm_explanations
    - llm_labels
    _ llm_nolabels

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
	[] KB_label 
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
	[] KB_hashtags
	[] KB_label 
	[] KB_nolabel

- Please Carefully
	[x] KB_expl.       
	[] KB_hashtags
	[] KB_label 
	[] KB_nolabel

- Recipe number h1, unh3, h4, unh_1
	[x] KB_expl.        
	[x] KB_hashtags
	[] KB_label 
	[] KB_nolabel


	

 sudo systemctl restart KB_nolabel KB_label KB_hashtags KB_expl

sudo -u postgres psql