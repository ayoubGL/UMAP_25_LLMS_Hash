databases:
    - llm_hashtags
    - llm_explanations
    - llm_labels
    _ llm_nolabels

- service/socket
    - [x] CB_base.service --> KB_nolabel.service: 5430, Admin DB          
    - [x] CB_full.service --> kB_explanations.service: 5434, Admin DB
    - [x] CF_boost.service --> kB_label.service: 5438, admin DB
    - [x] CB_mtl.service --> kB_hashtags.service: 543, admin DB

