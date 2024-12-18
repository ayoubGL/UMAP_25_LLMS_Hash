sem_model_without_understan <- "
# Latent Variables
SubjectiveFoodKnowledge =~ FK_9 + FK_10 + FK_11 + FK_12
Sustainability =~ sus_1 + sus_2 + sus_3
ChoiceSatisfaction =~ liked_recipes + prepare_recipes + fit_preference + know_many + recommend_recipe
ChoiceDifficulty =~ many_to_choose + easy_choice + choice_overwhelming
PerceivedEffort =~ unders_sys +sys_time+many_actions

# Regressions
fsa_score ~ conditionHashtags + conditionExplanation + conditionLabel 
fsa_score ~ SubjectiveFoodKnowledge + Sustainability
fsa_score ~ ChoiceSatisfaction + ChoiceDifficulty + PerceivedEffort
ChoiceSatisfaction ~ conditionHashtags + conditionExplanation + conditionLabel 
ChoiceDifficulty ~ conditionHashtags + conditionExplanation + conditionLabel 
PerceivedEffort ~ conditionHashtags + conditionExplanation + conditionLabel 
"

## Results

lavaan 0.6.13 ended normally after 74 iterations

  Estimator                                         ML
  Optimization method                           NLMINB
  Number of model parameters                        55

  Number of observations                           240

Model Test User Model:
                                                      
  Test statistic                               437.415
  Degrees of freedom                               192
  P-value (Chi-square)                           0.000

Model Test Baseline Model:

  Test statistic                              1611.793
  Degrees of freedom                               228
  P-value                                        0.000

User Model versus Baseline Model:

  Comparative Fit Index (CFI)                    0.823
  Tucker-Lewis Index (TLI)                       0.789

Loglikelihood and Information Criteria:

  Loglikelihood user model (H0)              -5321.074
  Loglikelihood unrestricted model (H1)      -5102.395
                                                      
  Akaike (AIC)                               10752.148
  Bayesian (BIC)                             10943.583
  Sample-size adjusted Bayesian (SABIC)      10769.246

Root Mean Square Error of Approximation:

  RMSEA                                          0.073
  90 Percent confidence interval - lower         0.064
  90 Percent confidence interval - upper         0.082
  P-value H_0: RMSEA <= 0.050                    0.000
  P-value H_0: RMSEA >= 0.080                    0.103

Standardized Root Mean Square Residual:

  SRMR                                           0.113

Parameter Estimates:

  Standard errors                             Standard
  Information                                 Expected
  Information saturated (h1) model          Structured

Latent Variables:
                             Estimate  Std.Err  z-value  P(>|z|)   Std.lv
  SubjectiveFoodKnowledge =~                                             
    FK_9                        1.000                               0.522
    FK_10                       0.925    0.098    9.410    0.000    0.483
    FK_11                       1.085    0.112    9.657    0.000    0.566
    FK_12                       1.197    0.121    9.918    0.000    0.624
  Sustainability =~                                                      
    sus_1                       1.000                               0.555
    sus_2                       0.846    0.156    5.433    0.000    0.469
    sus_3                       0.904    0.160    5.663    0.000    0.502
  ChoiceSatisfaction =~                                                  
    liked_recipes               1.000                               0.619
    prepare_recips              1.283    0.093   13.795    0.000    0.794
    fit_preference              0.995    0.082   12.085    0.000    0.616
    know_many                   0.494    0.104    4.746    0.000    0.306
    recommend_recp              0.968    0.086   11.229    0.000    0.599
  ChoiceDifficulty =~                                                    
    many_to_choose              1.000                               0.797
    easy_choice                 1.085    0.157    6.895    0.000    0.865
    choic_vrwhlmng              0.458    0.075    6.081    0.000    0.365
  PerceivedEffort =~                                                     
    unders_sys                  1.000                               0.369
    sys_time                    1.611    0.419    3.842    0.000    0.594
    many_actions                1.031    0.247    4.178    0.000    0.380
  Std.all
         
    0.725
    0.698
    0.721
    0.747
         
    0.666
    0.528
    0.586
         
    0.824
    0.842
    0.742
    0.321
    0.698
         
    0.767
    0.879
    0.433
         
    0.529
    0.815
    0.360

Regressions:
                       Estimate  Std.Err  z-value  P(>|z|)   Std.lv  Std.all
  fsa_score ~                                                               
    conditinHshtgs       -0.789    0.370   -2.132    0.033   -0.789   -0.164
    conditnExplntn       -1.230    0.384   -3.205    0.001   -1.230   -0.256
    conditionLabel       -1.279    0.371   -3.445    0.001   -1.279   -0.266
    SbjctvFdKnwldg       -0.032    0.378   -0.084    0.933   -0.017   -0.008
    Sustainability       -0.201    0.394   -0.509    0.611   -0.111   -0.053
    ChoiceSatsfctn       -0.039    0.227   -0.170    0.865   -0.024   -0.012
    ChoiceDiffclty        0.166    0.180    0.925    0.355    0.133    0.064
    PerceivedEffrt        0.192    0.436    0.440    0.660    0.071    0.034
  ChoiceSatisfaction ~                                                      
    conditinHshtgs        0.050    0.120    0.414    0.679    0.080    0.035
    conditnExplntn       -0.122    0.120   -1.014    0.311   -0.197   -0.085
    conditionLabel        0.101    0.120    0.845    0.398    0.164    0.071
  ChoiceDifficulty ~                                                        
    conditinHshtgs        0.211    0.160    1.318    0.188    0.265    0.115
    conditnExplntn        0.057    0.159    0.361    0.718    0.072    0.031
    conditionLabel        0.062    0.159    0.393    0.695    0.078    0.034
  PerceivedEffort ~                                                         
    conditinHshtgs        0.022    0.078    0.279    0.780    0.059    0.025
    conditnExplntn        0.241    0.093    2.600    0.009    0.654    0.283
    conditionLabel        0.095    0.080    1.189    0.234    0.259    0.112

Covariances:
                             Estimate  Std.Err  z-value  P(>|z|)   Std.lv
  SubjectiveFoodKnowledge ~~                                             
    Sustainability              0.161    0.033    4.927    0.000    0.555
  Std.all
         
    0.555

Variances:
                   Estimate  Std.Err  z-value  P(>|z|)   Std.lv  Std.all
   .FK_9              0.246    0.030    8.241    0.000    0.246    0.475
   .FK_10             0.245    0.028    8.633    0.000    0.245    0.513
   .FK_11             0.296    0.036    8.303    0.000    0.296    0.480
   .FK_12             0.309    0.039    7.850    0.000    0.309    0.442
   .sus_1             0.386    0.060    6.418    0.000    0.386    0.556
   .sus_2             0.571    0.065    8.773    0.000    0.571    0.721
   .sus_3             0.483    0.061    7.942    0.000    0.483    0.657
   .liked_recipes     0.180    0.025    7.313    0.000    0.180    0.320
   .prepare_recips    0.258    0.038    6.796    0.000    0.258    0.291
   .fit_preference    0.309    0.035    8.912    0.000    0.309    0.449
   .know_many         0.814    0.076   10.771    0.000    0.814    0.897
   .recommend_recp    0.377    0.040    9.387    0.000    0.377    0.512
   .many_to_choose    0.445    0.094    4.736    0.000    0.445    0.412
   .easy_choice       0.221    0.102    2.173    0.030    0.221    0.228
   .choic_vrwhlmng    0.577    0.056   10.357    0.000    0.577    0.812
   .unders_sys        0.350    0.046    7.540    0.000    0.350    0.720
   .sys_time          0.178    0.088    2.038    0.042    0.178    0.336
   .many_actions      0.972    0.097   10.033    0.000    0.972    0.870
   .fsa_score         4.053    0.371   10.920    0.000    4.053    0.935
    SbjctvFdKnwldg    0.272    0.046    5.911    0.000    1.000    1.000
    Sustainability    0.308    0.072    4.292    0.000    1.000    1.000
   .ChoiceSatsfctn    0.376    0.051    7.344    0.000    0.982    0.982
   .ChoiceDiffclty    0.630    0.122    5.151    0.000    0.990    0.990
   .PerceivedEffrt    0.127    0.042    3.028    0.002    0.934    0.934

