sem_model_with_understan_mi<- "
# Latent Variables
ChoiceSatisfaction =~ liked_recipes + prepare_recipes + fit_preference + know_many + recommend_recipe
ChoiceDifficulty =~ many_to_choose  + easy_choice
understandability =~ under_1 + under_2 

# Regressions
fsa_score ~ conditionHashtags + conditionExplanation + conditionLabel  
ChoiceSatisfaction  ~ conditionHashtags + conditionExplanation + conditionLabel
ChoiceDifficulty  ~ conditionHashtags + conditionExplanation + conditionLabel  
understandability  ~ conditionHashtags + conditionExplanation + conditionLabel  
understandability~ ChoiceSatisfaction + ChoiceDifficulty 
ChoiceSatisfaction ~ ChoiceDifficulty
"




llavaan 0.6.13 ended normally after 64 iterations

  Estimator                                         ML
  Optimization method                           NLMINB
  Number of model parameters                        35

  Number of observations                           240

Model Test User Model:
                                                      
  Test statistic                                73.953
  Degrees of freedom                                50
  P-value (Chi-square)                           0.015

Model Test Baseline Model:

  Test statistic                               879.159
  Degrees of freedom                                75
  P-value                                        0.000

User Model versus Baseline Model:

  Comparative Fit Index (CFI)                    0.970
  Tucker-Lewis Index (TLI)                       0.955

Loglikelihood and Information Criteria:

  Loglikelihood user model (H0)              -2962.908
  Loglikelihood unrestricted model (H1)      -2925.961
                                                      
  Akaike (AIC)                                5995.817
  Bayesian (BIC)                              6117.639
  Sample-size adjusted Bayesian (SABIC)       6006.697

Root Mean Square Error of Approximation:

  RMSEA                                          0.045
  90 Percent confidence interval - lower         0.020
  90 Percent confidence interval - upper         0.065
  P-value H_0: RMSEA <= 0.050                    0.640
  P-value H_0: RMSEA >= 0.080                    0.001

Standardized Root Mean Square Residual:

  SRMR                                           0.044

Parameter Estimates:

  Standard errors                             Standard
  Information                                 Expected
  Information saturated (h1) model          Structured

Latent Variables:
                        Estimate  Std.Err  z-value  P(>|z|)   Std.lv  Std.all
  ChoiceSatisfaction =~                                                      
    liked_recipes          1.000                               0.609    0.811
    prepare_recips         1.309    0.093   14.056    0.000    0.797    0.846
    fit_preference         1.014    0.084   12.131    0.000    0.617    0.743
    know_many              0.512    0.105    4.863    0.000    0.312    0.327
    recommend_recp         0.999    0.087   11.450    0.000    0.608    0.709
  ChoiceDifficulty =~                                                        
    many_to_choose         1.000                               0.480    0.462
    easy_choice           -2.996    1.016   -2.949    0.003   -1.438   -1.460
  understandability =~                                                       
    under_1                1.000                               0.553    0.636
    under_2                1.140    0.201    5.669    0.000    0.630    0.661

Regressions:
                       Estimate  Std.Err  z-value  P(>|z|)   Std.lv  Std.all
  fsa_score ~                                                               
    conditinHshtgs       -0.750    0.370   -2.027    0.043   -0.750   -0.156
    conditnExplntn       -1.166    0.370   -3.154    0.002   -1.166   -0.242
    conditionLabel       -1.250    0.370   -3.379    0.001   -1.250   -0.259
  ChoiceSatisfaction ~                                                      
    conditinHshtgs        0.085    0.109    0.777    0.437    0.139    0.060
    conditnExplntn       -0.141    0.108   -1.306    0.191   -0.233   -0.101
    conditionLabel        0.120    0.108    1.106    0.269    0.197    0.085
  ChoiceDifficulty ~                                                        
    conditinHshtgs        0.082    0.062    1.309    0.191    0.170    0.074
    conditnExplntn       -0.046    0.056   -0.812    0.417   -0.095   -0.041
    conditionLabel        0.045    0.056    0.794    0.427    0.093    0.040
  understandability ~                                                       
    conditinHshtgs        0.126    0.117    1.071    0.284    0.228    0.099
    conditnExplntn        0.164    0.118    1.391    0.164    0.297    0.129
    conditionLabel        0.244    0.119    2.050    0.040    0.442    0.191
    ChoiceSatsfctn        0.537    0.095    5.662    0.000    0.591    0.591
    ChoiceDiffclty       -0.052    0.052   -1.004    0.315   -0.045   -0.045
  ChoiceSatisfaction ~                                                      
    ChoiceDiffclty       -0.433    0.070   -6.199    0.000   -0.342   -0.342

Covariances:
                       Estimate  Std.Err  z-value  P(>|z|)   Std.lv  Std.all
 .understandability ~~                                                      
   .fsa_score             0.042    0.083    0.500    0.617    0.097    0.048

Variances:
                   Estimate  Std.Err  z-value  P(>|z|)   Std.lv  Std.all
   .liked_recipes     0.193    0.024    8.018    0.000    0.193    0.343
   .prepare_recips    0.253    0.035    7.136    0.000    0.253    0.285
   .fit_preference    0.308    0.034    9.096    0.000    0.308    0.447
   .know_many         0.811    0.075   10.779    0.000    0.811    0.893
   .recommend_recp    0.366    0.039    9.445    0.000    0.366    0.498
   .many_to_choose    0.850    0.105    8.109    0.000    0.850    0.787
   .easy_choice      -1.098    0.641   -1.714    0.087   -1.098   -1.132
   .under_1           0.449    0.065    6.889    0.000    0.449    0.595
   .under_2           0.511    0.081    6.332    0.000    0.511    0.563
   .fsa_score         4.105    0.375   10.954    0.000    4.105    0.944
   .ChoiceSatsfctn    0.321    0.046    6.908    0.000    0.866    0.866
   .ChoiceDiffclty    0.228    0.091    2.496    0.013    0.990    0.990
   .understandblty    0.183    0.053    3.463    0.001    0.600    0.600

R-Square:
                   Estimate
    liked_recipes     0.657
    prepare_recips    0.715
    fit_preference    0.553
    know_many         0.107
    recommend_recp    0.502
    many_to_choose    0.213
    easy_choice          NA
    under_1           0.405
    under_2           0.437
    fsa_score         0.056
    ChoiceSatsfctn    0.134
    ChoiceDiffclty    0.010
    understandblty    0.400

