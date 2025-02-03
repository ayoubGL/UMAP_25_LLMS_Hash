sem_model_with_understan_mi<- "
# Latent Variables
ChoiceSatisfaction =~ liked_recipes + prepare_recipes + fit_preference  
understandability =~ under_2 + under_3
ChoiceDifficulty =~ many_to_choose  
SubjectiveFoodKnowledge =~ FK_9  + FK_11 + FK_12

# Regressions
fsa_score ~ conditionHashtags + conditionExplanation + conditionLabel  
fsa_score ~ SubjectiveFoodKnowledge 
ChoiceSatisfaction ~ SubjectiveFoodKnowledge     
ChoiceDifficulty ~ SubjectiveFoodKnowledge     
understandability  ~ conditionHashtags + conditionExplanation + conditionLabel  + SubjectiveFoodKnowledge
understandability ~ ChoiceSatisfaction  
ChoiceDifficulty ~ understandability 
ChoiceSatisfaction ~ ChoiceDifficulty
"

conditionnoLabelfit <- sem(model = sem_model_with_understan_mi, data = df_dummies, ridge = 1e-5)
print(summary(conditionnoLabelfit, fit.measures = TRUE, standardized = TRUE,rsq=TRUE))

lavaan 0.6.13 ended normally after 51 iterations

  Estimator                                         ML
  Optimization method                           NLMINB
  Number of model parameters                        28

  Number of observations                           240

Model Test User Model:
                                                      
  Test statistic                                47.770
  Degrees of freedom                                44
  P-value (Chi-square)                           0.322

Model Test Baseline Model:

  Test statistic                               684.773
  Degrees of freedom                                63
  P-value                                        0.000

User Model versus Baseline Model:

  Comparative Fit Index (CFI)                    0.994
  Tucker-Lewis Index (TLI)                       0.991

Loglikelihood and Information Criteria:

  Loglikelihood user model (H0)              -2565.188
  Loglikelihood unrestricted model (H1)      -2541.332
                                                      
  Akaike (AIC)                                5186.377
  Bayesian (BIC)                              5283.835
  Sample-size adjusted Bayesian (SABIC)       5195.081

Root Mean Square Error of Approximation:

  RMSEA                                          0.019
  90 Percent confidence interval - lower         0.000
  90 Percent confidence interval - upper         0.048
  P-value H_0: RMSEA <= 0.050                    0.961
  P-value H_0: RMSEA >= 0.080                    0.000

Standardized Root Mean Square Residual:

  SRMR                                           0.038

Parameter Estimates:

  Standard errors                             Standard
  Information                                 Expected
  Information saturated (h1) model          Structured

Latent Variables:
                             Estimate  Std.Err  z-value  P(>|z|)   Std.lv
  ChoiceSatisfaction =~                                                  
    liked_recipes               1.000                               0.619
    prepare_recips              1.252    0.099   12.631    0.000    0.775
    fit_preference              1.043    0.086   12.178    0.000    0.645
  understandability =~                                                   
    under_3                     1.000                               0.503
    under_2                     1.563    0.303    5.160    0.000    0.786
  SubjectiveFoodKnowledge =~                                             
    FK_9                        1.000                               0.502
    FK_11                       1.180    0.135    8.732    0.000    0.592
    FK_12                      -1.250    0.143   -8.730    0.000   -0.628
  Std.all
         
    0.825
    0.823
    0.778
         
    0.589
    0.825
         
    0.697
    0.754
   -0.751

Regressions:
                       Estimate  Std.Err  z-value  P(>|z|)   Std.lv  Std.all
  fsa_score ~                                                               
    conditinHshtgs       -0.762    0.369   -2.064    0.039   -0.762   -0.158
    conditnExplntn       -1.178    0.369   -3.190    0.001   -1.178   -0.244
    conditionLabel       -1.265    0.369   -3.427    0.001   -1.265   -0.263
    SbjctvFdKnwldg       -0.278    0.295   -0.944    0.345   -0.140   -0.067
  ChoiceSatisfaction ~                                                      
    SbjctvFdKnwldg        0.122    0.098    1.248    0.212    0.099    0.099
  understandability ~                                                       
    conditinHshtgs        0.181    0.101    1.797    0.072    0.361    0.156
    conditnExplntn        0.261    0.105    2.487    0.013    0.520    0.225
    conditionLabel        0.289    0.107    2.702    0.007    0.574    0.248
    SbjctvFdKnwldg        0.236    0.088    2.685    0.007    0.236    0.236
    ChoiceSatsfctn        0.339    0.082    4.142    0.000    0.417    0.417

Covariances:
                       Estimate  Std.Err  z-value  P(>|z|)   Std.lv  Std.all
 .understandability ~~                                                      
   .fsa_score            -0.020    0.070   -0.292    0.770   -0.048   -0.024

Variances:
                   Estimate  Std.Err  z-value  P(>|z|)   Std.lv  Std.all
   .liked_recipes     0.180    0.027    6.609    0.000    0.180    0.320
   .prepare_recips    0.287    0.043    6.672    0.000    0.287    0.323
   .fit_preference    0.272    0.035    7.891    0.000    0.272    0.395
   .under_3           0.476    0.062    7.628    0.000    0.476    0.653
   .under_2           0.290    0.113    2.576    0.010    0.290    0.320
   .FK_9              0.266    0.034    7.849    0.000    0.266    0.514
   .FK_11             0.266    0.041    6.531    0.000    0.266    0.431
   .FK_12             0.304    0.046    6.612    0.000    0.304    0.436
   .fsa_score         4.086    0.373   10.940    0.000    4.086    0.938
   .ChoiceSatsfctn    0.379    0.053    7.166    0.000    0.990    0.990
   .understandblty    0.177    0.046    3.864    0.000    0.701    0.701
    SbjctvFdKnwldg    0.252    0.047    5.362    0.000    1.000    1.000

R-Square:
                   Estimate
    liked_recipes     0.680
    prepare_recips    0.677
    fit_preference    0.605
    under_3           0.347
    under_2           0.680
    FK_9              0.486
    FK_11             0.569
    FK_12             0.564
    fsa_score         0.062
    ChoiceSatsfctn    0.010
    understandblty    0.299

