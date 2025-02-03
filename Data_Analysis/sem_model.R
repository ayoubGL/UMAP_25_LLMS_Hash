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

