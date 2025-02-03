##another one 

sem_model_with_understan_mi<- "
# Latent Variables
ChoiceSatisfaction =~ liked_recipes + prepare_recipes + fit_preference  + recommend_recipe
ChoiceDifficulty =~ many_to_choose  + easy_choice
understandability =~ under_1 + under_2  
SubjectiveFoodKnowledge =~ FK_9 + FK_10 + FK_11 + FK_12
Sustainability =~ sus_1+sus_2+sus_3+sus_4

# Regressions
fsa_score ~ conditionHashtags + conditionExplanation + conditionLabel  
fsa_score ~ SubjectiveFoodKnowledge + Sustainability
ChoiceSatisfaction  ~ conditionHashtags + conditionExplanation + conditionLabel  + Sustainability
ChoiceDifficulty  ~ conditionHashtags + conditionExplanation + conditionLabel   + Sustainability
understandability  ~ conditionHashtags + conditionExplanation + conditionLabel  + SubjectiveFoodKnowledge
understandability~ ChoiceSatisfaction  
ChoiceSatisfaction ~ ChoiceDifficulty
"

conditionnoLabelfit <- sem(model = sem_model_with_understan_mi, data = df_dummies, ridge = 1e-5)
print(summary(conditionnoLabelfit, fit.measures = TRUE, standardized = TRUE,rsq=TRUE))


lavaan 0.6.13 ended normally after 80 iterations

  Estimator                                         ML
  Optimization method                           NLMINB
  Number of model parameters                        54

  Number of observations                           240

Model Test User Model:
                                                      
  Test statistic                               203.258
  Degrees of freedom                               150
  P-value (Chi-square)                           0.002

Model Test Baseline Model:

  Test statistic                              1443.638
  Degrees of freedom                               187
  P-value                                        0.000

User Model versus Baseline Model:

  Comparative Fit Index (CFI)                    0.958
  Tucker-Lewis Index (TLI)                       0.947

Loglikelihood and Information Criteria:

  Loglikelihood user model (H0)              -4770.069
  Loglikelihood unrestricted model (H1)      -4668.469
                                                      
  Akaike (AIC)                                9648.138
  Bayesian (BIC)                              9836.093
  Sample-size adjusted Bayesian (SABIC)       9664.926

Root Mean Square Error of Approximation:

  RMSEA                                          0.038
  90 Percent confidence interval - lower         0.024
  90 Percent confidence interval - upper         0.051
  P-value H_0: RMSEA <= 0.050                    0.929
  P-value H_0: RMSEA >= 0.080                    0.000

Standardized Root Mean Square Residual:

  SRMR                                           0.051

Parameter Estimates:

  Standard errors                             Standard
  Information                                 Expected
  Information saturated (h1) model          Structured

Latent Variables:
                             Estimate  Std.Err  z-value  P(>|z|)   Std.lv
  ChoiceSatisfaction =~                                                  
    liked_recipes               1.000                               0.609
    prepare_recips              1.311    0.093   14.105    0.000    0.799
    fit_preference              1.018    0.083   12.229    0.000    0.620
    recommend_recp              0.983    0.087   11.264    0.000    0.599
  ChoiceDifficulty =~                                                    
    many_to_choose              1.000                               0.497
    easy_choice                -2.797    0.861   -3.250    0.001   -1.389
  understandability =~                                                   
    under_1                     1.000                               0.513
    under_2                     1.341    0.233    5.745    0.000    0.687
  SubjectiveFoodKnowledge =~                                             
    FK_9                        1.000                               0.522
    FK_10                       0.927    0.098    9.453    0.000    0.484
    FK_11                       1.084    0.112    9.687    0.000    0.566
    FK_12                      -1.192    0.120   -9.932    0.000   -0.623
  Sustainability =~                                                      
    sus_1                       1.000                               0.567
    sus_2                       0.819    0.144    5.667    0.000    0.464
    sus_3                       0.862    0.145    5.944    0.000    0.489
    sus_4                       0.443    0.146    3.030    0.002    0.251
  Std.all
         
    0.812
    0.848
    0.748
    0.699
         
    0.478
   -1.411
         
    0.589
    0.719
         
    0.725
    0.700
    0.721
   -0.745
         
    0.681
    0.522
    0.570
    0.244

Regressions:
                       Estimate  Std.Err  z-value  P(>|z|)   Std.lv  Std.all
  fsa_score ~                                                               
    conditinHshtgs       -0.755    0.369   -2.048    0.041   -0.755   -0.157
    conditnExplntn       -1.174    0.369   -3.182    0.001   -1.174   -0.244
    conditionLabel       -1.260    0.369   -3.416    0.001   -1.260   -0.262
    SbjctvFdKnwldg       -0.023    0.376   -0.061    0.951   -0.012   -0.006
    Sustainability       -0.309    0.380   -0.812    0.417   -0.175   -0.084
  ChoiceSatisfaction ~                                                      
    conditinHshtgs        0.086    0.107    0.806    0.420    0.141    0.061
    conditnExplntn       -0.130    0.106   -1.222    0.222   -0.213   -0.092
    conditionLabel        0.123    0.106    1.157    0.247    0.202    0.087
    Sustainability        0.254    0.089    2.856    0.004    0.236    0.236
  ChoiceDifficulty ~                                                        
    conditinHshtgs        0.086    0.065    1.338    0.181    0.174    0.075
    conditnExplntn       -0.051    0.059   -0.851    0.395   -0.102   -0.044
    conditionLabel        0.044    0.059    0.743    0.457    0.088    0.038
    Sustainability       -0.142    0.068   -2.079    0.038   -0.162   -0.162
  understandability ~                                                       
    conditinHshtgs        0.126    0.106    1.194    0.233    0.246    0.106
    conditnExplntn        0.176    0.107    1.653    0.098    0.344    0.149
    conditionLabel        0.236    0.108    2.183    0.029    0.461    0.200
    SbjctvFdKnwldg        0.192    0.083    2.306    0.021    0.196    0.196
    ChoiceSatsfctn        0.480    0.090    5.355    0.000    0.570    0.570
  ChoiceSatisfaction ~                                                      
    ChoiceDiffclty       -0.394    0.068   -5.829    0.000   -0.321   -0.321

Covariances:
                             Estimate  Std.Err  z-value  P(>|z|)   Std.lv
  SubjectiveFoodKnowledge ~~                                             
    Sustainability              0.164    0.033    5.047    0.000    0.555
 .understandability ~~                                                   
   .fsa_score                   0.026    0.074    0.349    0.727    0.067
  Std.all
         
    0.555
         
    0.033

Variances:
                   Estimate  Std.Err  z-value  P(>|z|)   Std.lv  Std.all
   .liked_recipes     0.192    0.024    7.983    0.000    0.192    0.341
   .prepare_recips    0.250    0.035    7.058    0.000    0.250    0.281
   .fit_preference    0.304    0.034    9.042    0.000    0.304    0.441
   .recommend_recp    0.377    0.040    9.529    0.000    0.377    0.512
   .many_to_choose    0.834    0.102    8.175    0.000    0.834    0.772
   .easy_choice      -0.961    0.538   -1.785    0.074   -0.961   -0.990
   .under_1           0.495    0.062    8.000    0.000    0.495    0.653
   .under_2           0.441    0.086    5.126    0.000    0.441    0.483
   .FK_9              0.246    0.030    8.259    0.000    0.246    0.474
   .FK_10             0.244    0.028    8.635    0.000    0.244    0.511
   .FK_11             0.296    0.036    8.329    0.000    0.296    0.480
   .FK_12             0.311    0.039    7.918    0.000    0.311    0.445
   .sus_1             0.373    0.057    6.520    0.000    0.373    0.537
   .sus_2             0.575    0.064    9.029    0.000    0.575    0.727
   .sus_3             0.496    0.059    8.441    0.000    0.496    0.675
   .sus_4             0.995    0.094   10.641    0.000    0.995    0.940
   .fsa_score         4.072    0.373   10.911    0.000    4.072    0.935
   .ChoiceSatsfctn    0.297    0.043    6.875    0.000    0.800    0.800
   .ChoiceDiffclty    0.238    0.086    2.761    0.006    0.963    0.963
   .understandblty    0.149    0.043    3.448    0.001    0.567    0.567
    SbjctvFdKnwldg    0.273    0.046    5.925    0.000    1.000    1.000
    Sustainability    0.321    0.070    4.561    0.000    1.000    1.000

R-Square:
                   Estimate
    liked_recipes     0.659
    prepare_recips    0.719
    fit_preference    0.559
    recommend_recp    0.488
    many_to_choose    0.228
    easy_choice          NA
    under_1           0.347
    under_2           0.517
    FK_9              0.526
    FK_10             0.489
    FK_11             0.520
    FK_12             0.555
    sus_1             0.463
    sus_2             0.273
    sus_3             0.325
    sus_4             0.060
    fsa_score         0.065
    ChoiceSatsfctn    0.200
    ChoiceDiffclty    0.037
    understandblty    0.433

