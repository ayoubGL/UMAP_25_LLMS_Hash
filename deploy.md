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
	[] KB_label 
	[] KB_nolabel
	[] KB_hashtags
	[x] KB_expl

- Depression to deepresionL
	[] KB_label 
	[] KB_nolabel
	[] KB_hashtags
	[x] KB_expl




 sudo systemctl restart KB_nolabel KB_label KB_hashtags KB_explanations

