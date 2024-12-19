sem_model_with_understan <- "
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

