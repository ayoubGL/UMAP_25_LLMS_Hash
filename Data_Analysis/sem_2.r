sem_model_with_understan <- "
# Latent Variables
SubjectiveFoodKnowledge =~ FK_9 + FK_10 + FK_11 + FK_12
Sustainability =~ sus_1 + sus_2 + sus_3
ChoiceSatisfaction =~ liked_recipes + prepare_recipes + fit_preference + know_many + recommend_recipe
ChoiceDifficulty =~ many_to_choose + easy_choice + choice_overwhelming
PerceivedEffort =~ unders_sys +sys_time+many_actions
understandability =~ under_1 + under_2 + under_3

# Regressions
fsa_score ~ conditionHashtags + conditionExplanation + conditionLabel 
fsa_score ~ SubjectiveFoodKnowledge + Sustainability
fsa_score ~ ChoiceSatisfaction + ChoiceDifficulty + PerceivedEffort
ChoiceSatisfaction ~ conditionHashtags + conditionExplanation + conditionLabel 
ChoiceDifficulty ~ conditionHashtags + conditionExplanation + conditionLabel 
PerceivedEffort ~ conditionHashtags + conditionExplanation + conditionLabel 
understandability ~  conditionHashtags + conditionExplanation + conditionLabel
"



lavaan 0.6.13 ended normally after 74 iterations

  Estimator                                         ML
  Optimization method                           NLMINB
  Number of model parameters                        65

  Number of observations                           240

Model Test User Model:
                                                      
  Test statistic                               595.129
  Degrees of freedom                               254
  P-value (Chi-square)                           0.000

Model Test Baseline Model:

  Test statistic                              1922.823
  Degrees of freedom                               297
  P-value                                        0.000

User Model versus Baseline Model:

  Comparative Fit Index (CFI)                    0.790
  Tucker-Lewis Index (TLI)                       0.755

Loglikelihood and Information Criteria:

  Loglikelihood user model (H0)              -6182.441
  Loglikelihood unrestricted model (H1)      -5884.905
                                                      
  Akaike (AIC)                               12494.881
  Bayesian (BIC)                             12721.123
  Sample-size adjusted Bayesian (SABIC)      12515.089

Root Mean Square Error of Approximation:

  RMSEA                                          0.075
  90 Percent confidence interval - lower         0.067
  90 Percent confidence interval - upper         0.083
  P-value H_0: RMSEA <= 0.050                    0.000
  P-value H_0: RMSEA >= 0.080                    0.140

Standardized Root Mean Square Residual:

  SRMR                                           0.125

Parameter Estimates:

  Standard errors                             Standard
  Information                                 Expected
  Information saturated (h1) model          Structured

Latent Variables:
                             Estimate  Std.Err  z-value  P(>|z|)   Std.lv
  SubjectiveFoodKnowledge =~                                             
    FK_9                        1.000                               0.522
    FK_10                       0.925    0.098    9.409    0.000    0.483
    FK_11                       1.085    0.112    9.658    0.000    0.566
    FK_12                       1.196    0.121    9.917    0.000    0.624
  Sustainability =~                                                      
    sus_1                       1.000                               0.555
    sus_2                       0.846    0.156    5.433    0.000    0.469
    sus_3                       0.904    0.160    5.663    0.000    0.502
  ChoiceSatisfaction =~                                                  
    liked_recipes               1.000                               0.619
    prepare_recips              1.283    0.093   13.794    0.000    0.794
    fit_preference              0.996    0.082   12.082    0.000    0.616
    know_many                   0.494    0.104    4.747    0.000    0.306
    recommend_recp              0.968    0.086   11.227    0.000    0.599
  ChoiceDifficulty =~                                                    
    many_to_choose              1.000                               0.797
    easy_choice                 1.086    0.158    6.892    0.000    0.866
    choic_vrwhlmng              0.458    0.075    6.081    0.000    0.365
  PerceivedEffort =~                                                     
    unders_sys                  1.000                               0.369
    sys_time                    1.613    0.420    3.842    0.000    0.595
    many_actions                1.031    0.247    4.179    0.000    0.380
  understandability =~                                                   
    under_1                     1.000                               0.542
    under_2                     1.120    0.161    6.950    0.000    0.607
    under_3                     1.215    0.178    6.828    0.000    0.659
  Std.all
         
    0.725
    0.698
    0.721
    0.747
         
    0.666
    0.528
    0.586
         
    0.824
    0.843
    0.742
    0.321
    0.698
         
    0.767
    0.879
    0.433
         
    0.529
    0.815
    0.360
         
    0.625
    0.638
    0.772

Regressions:
                       Estimate  Std.Err  z-value  P(>|z|)   Std.lv  Std.all
  fsa_score ~                                                               
    conditinHshtgs       -0.789    0.370   -2.130    0.033   -0.789   -0.164
    conditnExplntn       -1.237    0.384   -3.223    0.001   -1.237   -0.257
    conditionLabel       -1.279    0.371   -3.445    0.001   -1.279   -0.266
    SbjctvFdKnwldg       -0.042    0.378   -0.112    0.911   -0.022   -0.011
    Sustainability       -0.197    0.394   -0.499    0.618   -0.109   -0.052
    ChoiceSatsfctn       -0.058    0.227   -0.255    0.798   -0.036   -0.017
    ChoiceDiffclty        0.166    0.180    0.924    0.355    0.133    0.064
    PerceivedEffrt        0.211    0.436    0.484    0.629    0.078    0.037
  ChoiceSatisfaction ~                                                      
    conditinHshtgs        0.050    0.120    0.414    0.679    0.080    0.035
    conditnExplntn       -0.122    0.120   -1.014    0.310   -0.197   -0.085
    conditionLabel        0.101    0.120    0.846    0.398    0.164    0.071
  ChoiceDifficulty ~                                                        
    conditinHshtgs        0.211    0.160    1.318    0.187    0.265    0.115
    conditnExplntn        0.057    0.159    0.360    0.719    0.072    0.031
    conditionLabel        0.062    0.159    0.393    0.694    0.078    0.034
  PerceivedEffort ~                                                         
    conditinHshtgs        0.022    0.078    0.279    0.780    0.059    0.025
    conditnExplntn        0.241    0.093    2.600    0.009    0.654    0.283
    conditionLabel        0.095    0.080    1.190    0.234    0.259    0.112
  understandability ~                                                       
    conditinHshtgs        0.193    0.114    1.688    0.091    0.355    0.154
    conditnExplntn        0.220    0.115    1.920    0.055    0.406    0.176
    conditionLabel        0.394    0.119    3.306    0.001    0.726    0.314

Covariances:
                             Estimate  Std.Err  z-value  P(>|z|)   Std.lv
  SubjectiveFoodKnowledge ~~                                             
    Sustainability              0.161    0.033    4.927    0.000    0.555
 .understandability ~~                                                   
   .fsa_score                   0.021    0.080    0.259    0.796    0.040
  Std.all
         
    0.555
         
    0.020

Variances:
                   Estimate  Std.Err  z-value  P(>|z|)   Std.lv  Std.all
   .FK_9              0.246    0.030    8.241    0.000    0.246    0.475
   .FK_10             0.245    0.028    8.633    0.000    0.245    0.513
   .FK_11             0.296    0.036    8.303    0.000    0.296    0.480
   .FK_12             0.309    0.039    7.850    0.000    0.309    0.442
   .sus_1             0.386    0.060    6.417    0.000    0.386    0.556
   .sus_2             0.571    0.065    8.773    0.000    0.571    0.721
   .sus_3             0.483    0.061    7.942    0.000    0.483    0.657
   .liked_recipes     0.181    0.025    7.320    0.000    0.181    0.321
   .prepare_recips    0.258    0.038    6.789    0.000    0.258    0.290
   .fit_preference    0.309    0.035    8.912    0.000    0.309    0.449
   .know_many         0.814    0.076   10.771    0.000    0.814    0.897
   .recommend_recp    0.377    0.040    9.387    0.000    0.377    0.512
   .many_to_choose    0.445    0.094    4.742    0.000    0.445    0.412
   .easy_choice       0.221    0.102    2.165    0.030    0.221    0.227
   .choic_vrwhlmng    0.577    0.056   10.357    0.000    0.577    0.812
   .unders_sys        0.350    0.046    7.547    0.000    0.350    0.720
   .sys_time          0.178    0.088    2.032    0.042    0.178    0.335
   .many_actions      0.972    0.097   10.034    0.000    0.972    0.871
   .under_1           0.460    0.057    8.116    0.000    0.460    0.610
   .under_2           0.538    0.068    7.867    0.000    0.538    0.593
   .under_3           0.294    0.061    4.807    0.000    0.294    0.404
   .fsa_score         4.053    0.371   10.919    0.000    4.053    0.934
    SbjctvFdKnwldg    0.272    0.046    5.911    0.000    1.000    1.000
    Sustainability    0.308    0.072    4.292    0.000    1.000    1.000
   .ChoiceSatsfctn    0.376    0.051    7.341    0.000    0.982    0.982
   .ChoiceDiffclty    0.629    0.122    5.149    0.000    0.990    0.990
   .PerceivedEffrt    0.127    0.042    3.027    0.002    0.935    0.935
   .understandblty    0.275    0.062    4.407    0.000    0.934    0.934

