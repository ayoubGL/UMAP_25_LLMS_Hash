sem_model_with_understan_1 <- "
# Latent Variables
SubjectiveFoodKnowledge =~ FK_9 + FK_10 + FK_11 + FK_12
Sustainability =~ sus_1 + sus_2 + sus_3
ChoiceSatisfaction =~ liked_recipes + prepare_recipes + fit_preference + know_many + recommend_recipe
ChoiceDifficulty =~ many_to_choose + easy_choice + choice_overwhelming
understandability =~ under_1 + under_2 + under_3

# Regressions
fsa_score ~ conditionHashtags + conditionExplanation + conditionLabel  
ChoiceSatisfaction  ~ conditionHashtags + conditionExplanation + conditionLabel
ChoiceDifficulty  ~ conditionHashtags + conditionExplanation + conditionLabel  
understandability  ~ conditionHashtags + conditionExplanation + conditionLabel  
ChoiceSatisfaction ~ understandability 
ChoiceDifficulty ~ understandability 
ChoiceSatisfaction ~ ChoiceDifficulty
ChoiceSatisfaction ~SubjectiveFoodKnowledge  + Sustainability
ChoiceDifficulty ~  SubjectiveFoodKnowledge  + Sustainability
understandability ~  SubjectiveFoodKnowledge  + Sustainability
"



lavaan 0.6.13 ended normally after 60 iterations

  Estimator                                         ML
  Optimization method                           NLMINB
  Number of model parameters                        60

  Number of observations                           240

Model Test User Model:
                                                      
  Test statistic                               304.983
  Degrees of freedom                               187
  P-value (Chi-square)                           0.000

Model Test Baseline Model:

  Test statistic                              1671.575
  Degrees of freedom                               228
  P-value                                        0.000

User Model versus Baseline Model:

  Comparative Fit Index (CFI)                    0.918
  Tucker-Lewis Index (TLI)                       0.900

Loglikelihood and Information Criteria:

  Loglikelihood user model (H0)              -5290.589
  Loglikelihood unrestricted model (H1)      -5138.126
                                                      
  Akaike (AIC)                               10701.177
  Bayesian (BIC)                             10910.015
  Sample-size adjusted Bayesian (SABIC)      10719.830

Root Mean Square Error of Approximation:

  RMSEA                                          0.051
  90 Percent confidence interval - lower         0.041
  90 Percent confidence interval - upper         0.062
  P-value H_0: RMSEA <= 0.050                    0.409
  P-value H_0: RMSEA >= 0.080                    0.000

Standardized Root Mean Square Residual:

  SRMR                                           0.065

Parameter Estimates:

  Standard errors                             Standard
  Information                                 Expected
  Information saturated (h1) model          Structured

Latent Variables:
                             Estimate  Std.Err  z-value  P(>|z|)   Std.lv
  SubjectiveFoodKnowledge =~                                             
    FK_9                        1.000                               0.523
    FK_10                       0.926    0.098    9.469    0.000    0.484
    FK_11                       1.077    0.111    9.660    0.000    0.563
    FK_12                       1.194    0.120    9.966    0.000    0.624
  Sustainability =~                                                      
    sus_1                       1.000                               0.560
    sus_2                       0.848    0.148    5.717    0.000    0.475
    sus_3                       0.874    0.148    5.921    0.000    0.489
  ChoiceSatisfaction =~                                                  
    liked_recipes               1.000                               0.605
    prepare_recips              1.323    0.094   14.006    0.000    0.801
    fit_preference              1.015    0.085   12.006    0.000    0.614
    know_many                   0.514    0.106    4.843    0.000    0.311
    recommend_recp              1.004    0.088   11.381    0.000    0.607
  ChoiceDifficulty =~                                                    
    many_to_choose              1.000                               0.634
    easy_choice                 1.728    0.244    7.095    0.000    1.096
    choic_vrwhlmng              0.391    0.078    5.007    0.000    0.248
  understandability =~                                                   
    under_1                     1.000                               0.558
    under_2                     1.212    0.160    7.557    0.000    0.676
    under_3                     1.052    0.141    7.480    0.000    0.587
  Std.all
         
    0.726
    0.700
    0.717
    0.747
         
    0.672
    0.534
    0.571
         
    0.807
    0.850
    0.741
    0.326
    0.708
         
    0.610
    1.113
    0.295
         
    0.642
    0.709
    0.686

Regressions:
                       Estimate  Std.Err  z-value  P(>|z|)   Std.lv  Std.all
  fsa_score ~                                                               
    conditinHshtgs       -0.750    0.370   -2.027    0.043   -0.750   -0.156
    conditnExplntn       -1.166    0.370   -3.154    0.002   -1.166   -0.242
    conditionLabel       -1.250    0.370   -3.379    0.001   -1.250   -0.259
  ChoiceSatisfaction ~                                                      
    conditinHshtgs        0.011    0.101    0.106    0.916    0.018    0.008
    conditnExplntn       -0.223    0.100   -2.223    0.026   -0.369   -0.160
    conditionLabel       -0.057    0.105   -0.544    0.586   -0.095   -0.041
  ChoiceDifficulty ~                                                        
    conditinHshtgs        0.215    0.103    2.085    0.037    0.339    0.147
    conditnExplntn        0.018    0.097    0.184    0.854    0.028    0.012
    conditionLabel        0.193    0.105    1.834    0.067    0.305    0.132
  understandability ~                                                       
    conditinHshtgs        0.193    0.116    1.659    0.097    0.345    0.150
    conditnExplntn        0.205    0.116    1.765    0.078    0.368    0.159
    conditionLabel        0.391    0.120    3.270    0.001    0.702    0.304
  ChoiceSatisfaction ~                                                      
    understandblty        0.450    0.098    4.585    0.000    0.415    0.415
  ChoiceDifficulty ~                                                        
    understandblty       -0.317    0.099   -3.209    0.001   -0.279   -0.279
  ChoiceSatisfaction ~                                                      
    ChoiceDiffclty       -0.299    0.064   -4.697    0.000   -0.314   -0.314
    SbjctvFdKnwldg       -0.168    0.109   -1.537    0.124   -0.145   -0.145
    Sustainability        0.227    0.117    1.933    0.053    0.210    0.210
  ChoiceDifficulty ~                                                        
    SbjctvFdKnwldg        0.201    0.110    1.834    0.067    0.166    0.166
    Sustainability       -0.325    0.124   -2.619    0.009   -0.287   -0.287
  understandability ~                                                       
    SbjctvFdKnwldg        0.191    0.120    1.584    0.113    0.179    0.179
    Sustainability        0.090    0.123    0.726    0.468    0.090    0.090

Covariances:
                             Estimate  Std.Err  z-value  P(>|z|)   Std.lv
  SubjectiveFoodKnowledge ~~                                             
    Sustainability              0.164    0.033    5.018    0.000    0.559
 .ChoiceSatisfaction ~~                                                  
   .fsa_score                  -0.014    0.069   -0.204    0.839   -0.030
  Std.all
         
    0.559
         
   -0.015

Variances:
                   Estimate  Std.Err  z-value  P(>|z|)   Std.lv  Std.all
   .FK_9              0.245    0.030    8.244    0.000    0.245    0.472
   .FK_10             0.244    0.028    8.634    0.000    0.244    0.510
   .FK_11             0.299    0.036    8.390    0.000    0.299    0.486
   .FK_12             0.308    0.039    7.884    0.000    0.308    0.442
   .sus_1             0.381    0.057    6.641    0.000    0.381    0.549
   .sus_2             0.565    0.064    8.883    0.000    0.565    0.715
   .sus_3             0.495    0.059    8.415    0.000    0.495    0.674
   .liked_recipes     0.196    0.024    8.070    0.000    0.196    0.349
   .prepare_recips    0.245    0.035    6.949    0.000    0.245    0.277
   .fit_preference    0.311    0.034    9.109    0.000    0.311    0.452
   .know_many         0.811    0.075   10.779    0.000    0.811    0.894
   .recommend_recp    0.366    0.039    9.435    0.000    0.366    0.498
   .many_to_choose    0.679    0.076    8.936    0.000    0.679    0.628
   .easy_choice      -0.231    0.136   -1.690    0.091   -0.231   -0.238
   .choic_vrwhlmng    0.648    0.059   11.038    0.000    0.648    0.913
   .under_1           0.444    0.053    8.305    0.000    0.444    0.588
   .under_2           0.451    0.064    7.091    0.000    0.451    0.497
   .under_3           0.386    0.051    7.546    0.000    0.386    0.529
   .fsa_score         4.105    0.375   10.954    0.000    4.105    0.944
    SbjctvFdKnwldg    0.273    0.046    5.937    0.000    1.000    1.000
    Sustainability    0.313    0.070    4.481    0.000    1.000    1.000
   .ChoiceSatsfctn    0.215    0.034    6.335    0.000    0.588    0.588
   .ChoiceDiffclty    0.341    0.070    4.832    0.000    0.847    0.847
   .understandblty    0.274    0.059    4.646    0.000    0.880    0.880


sem_model_with_understan_2 <- "
# Latent Variables
ChoiceSatisfaction =~ liked_recipes + prepare_recipes + fit_preference + know_many + recommend_recipe
ChoiceDifficulty =~ many_to_choose + easy_choice + choice_overwhelming
understandability =~ under_1 + under_2 + under_3

# Regressions
fsa_score ~ conditionHashtags + conditionExplanation + conditionLabel  
ChoiceSatisfaction  ~ conditionHashtags + conditionExplanation + conditionLabel
ChoiceDifficulty  ~ conditionHashtags + conditionExplanation + conditionLabel  
understandability  ~ conditionHashtags + conditionExplanation + conditionLabel  
ChoiceSatisfaction ~ understandability 
ChoiceDifficulty ~ understandability 
ChoiceSatisfaction ~ ChoiceDifficulty
"


lavaan 0.6.13 ended normally after 53 iterations

  Estimator                                         ML
  Optimization method                           NLMINB
  Number of model parameters                        39

  Number of observations                           240

Model Test User Model:
                                                      
  Test statistic                               127.526
  Degrees of freedom                                75
  P-value (Chi-square)                           0.000

Model Test Baseline Model:

  Test statistic                              1043.101
  Degrees of freedom                               102
  P-value                                        0.000

User Model versus Baseline Model:

  Comparative Fit Index (CFI)                    0.944
  Tucker-Lewis Index (TLI)                       0.924

Loglikelihood and Information Criteria:

  Loglikelihood user model (H0)              -3509.771
  Loglikelihood unrestricted model (H1)      -3446.037
                                                      
  Akaike (AIC)                                7097.542
  Bayesian (BIC)                              7233.286
  Sample-size adjusted Bayesian (SABIC)       7109.666

Root Mean Square Error of Approximation:

  RMSEA                                          0.054
  90 Percent confidence interval - lower         0.037
  90 Percent confidence interval - upper         0.070
  P-value H_0: RMSEA <= 0.050                    0.325
  P-value H_0: RMSEA >= 0.080                    0.003

Standardized Root Mean Square Residual:

  SRMR                                           0.056

Parameter Estimates:

  Standard errors                             Standard
  Information                                 Expected
  Information saturated (h1) model          Structured

Latent Variables:
                        Estimate  Std.Err  z-value  P(>|z|)   Std.lv  Std.all
  ChoiceSatisfaction =~                                                      
    liked_recipes          1.000                               0.608    0.810
    prepare_recips         1.313    0.094   13.991    0.000    0.797    0.847
    fit_preference         1.013    0.084   12.060    0.000    0.615    0.742
    know_many             -0.515    0.106   -4.877    0.000   -0.313   -0.328
    recommend_recp         1.000    0.088   11.415    0.000    0.608    0.709
  ChoiceDifficulty =~                                                        
    many_to_choose         1.000                               0.634    0.610
    easy_choice           -1.726    0.247   -6.974    0.000   -1.095   -1.112
    choic_vrwhlmng         0.393    0.078    5.018    0.000    0.249    0.296
  understandability =~                                                       
    under_1                1.000                               0.574    0.662
    under_2                1.141    0.152    7.504    0.000    0.655    0.688
    under_3                1.023    0.136    7.504    0.000    0.588    0.688

Regressions:
                       Estimate  Std.Err  z-value  P(>|z|)   Std.lv  Std.all
  fsa_score ~                                                               
    conditinHshtgs       -0.750    0.370   -2.027    0.043   -0.750   -0.156
    conditnExplntn       -1.166    0.370   -3.154    0.002   -1.166   -0.242
    conditionLabel       -1.250    0.370   -3.379    0.001   -1.250   -0.259
  ChoiceSatisfaction ~                                                      
    conditinHshtgs        0.020    0.102    0.195    0.845    0.033    0.014
    conditnExplntn       -0.224    0.101   -2.216    0.027   -0.368   -0.159
    conditionLabel       -0.045    0.105   -0.430    0.667   -0.074   -0.032
  ChoiceDifficulty ~                                                        
    conditinHshtgs        0.219    0.106    2.077    0.038    0.346    0.150
    conditnExplntn        0.024    0.099    0.241    0.809    0.038    0.016
    conditionLabel        0.194    0.107    1.806    0.071    0.305    0.132
  understandability ~                                                       
    conditinHshtgs        0.193    0.122    1.585    0.113    0.336    0.146
    conditnExplntn        0.203    0.122    1.664    0.096    0.354    0.153
    conditionLabel        0.392    0.125    3.133    0.002    0.682    0.295
  ChoiceSatisfaction ~                                                      
    understandblty        0.430    0.092    4.682    0.000    0.406    0.406
  ChoiceDifficulty ~                                                        
    understandblty       -0.327    0.096   -3.411    0.001   -0.296   -0.296
  ChoiceSatisfaction ~                                                      
    ChoiceDiffclty       -0.344    0.062   -5.550    0.000   -0.360   -0.360

Covariances:
                        Estimate  Std.Err  z-value  P(>|z|)   Std.lv  Std.all
 .ChoiceSatisfaction ~~                                                      
   .fsa_score             -0.017    0.069   -0.248    0.804   -0.036   -0.018

Variances:
                   Estimate  Std.Err  z-value  P(>|z|)   Std.lv  Std.all
   .liked_recipes     0.194    0.024    7.989    0.000    0.194    0.344
   .prepare_recips    0.251    0.036    7.041    0.000    0.251    0.283
   .fit_preference    0.310    0.034    9.084    0.000    0.310    0.450
   .know_many         0.810    0.075   10.775    0.000    0.810    0.892
   .recommend_recp    0.366    0.039    9.422    0.000    0.366    0.498
   .many_to_choose    0.678    0.077    8.841    0.000    0.678    0.628
   .easy_choice      -0.228    0.140   -1.633    0.102   -0.228   -0.236
   .choic_vrwhlmng    0.648    0.059   11.029    0.000    0.648    0.913
   .under_1           0.424    0.054    7.902    0.000    0.424    0.562
   .under_2           0.477    0.064    7.410    0.000    0.477    0.526
   .under_3           0.383    0.052    7.407    0.000    0.383    0.526
   .fsa_score         4.105    0.375   10.954    0.000    4.105    0.944
   .ChoiceSatsfctn    0.228    0.035    6.551    0.000    0.617    0.617
   .ChoiceDiffclty    0.364    0.077    4.707    0.000    0.903    0.903
   .understandblty    0.311    0.064    4.820    0.000    0.942    0.942

