# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:29 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Sat Nov  4 13:46:46 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',0.325341,-10000,10000,0,'Beta_time_PT' )

LAMBDA = Beta('LAMBDA',0.198168,-10000,10000,0,'LAMBDA' )

Beta_time_PT_walk = Beta('Beta_time_PT_walk',-0.0373378,-10000,10000,0,'Beta_time_PT_walk' )

Beta_Cost = Beta('Beta_Cost',-0.0577091,-10000,10000,0,'Beta_Cost' )

Beta_Income = Beta('Beta_Income',-7.08767e-05,-10000,10000,0,'Beta_Income' )

Beta_Age = Beta('Beta_Age',-0.00615533,-10000,10000,0,'Beta_Age' )

Beta_typeBus = Beta('Beta_typeBus',-0.118625,-10000,10000,0,'Beta_typeBus' )

Beta_have_ga = Beta('Beta_have_ga',1.58064,-10000,10000,0,'Beta_have_ga' )

ASC_PM  = Beta('ASC_PM ',0.522057,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.0150434,-10000,10000,0,'Beta_time_PM' )

ASC_SM = Beta('ASC_SM',-0.500623,-10000,10000,0,'ASC_SM' )

Beta_Distance = Beta('Beta_Distance',-0.19013,-10000,10000,0,'Beta_Distance' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Beta_Age','Beta_Cost','Beta_Distance','Beta_Income','Beta_have_ga','Beta_time_PM','Beta_time_PT','Beta_time_PT_walk','Beta_typeBus','LAMBDA']
values = [[0.103311,0.0517464,0.000594419,0.000919564,0.0040233,-1.06651e-07,0.0156218,0.000503259,0.011044,0.000135039,0.00525479,-0.00170127],[0.0517464,0.200541,-6.52793e-05,0.000466292,-0.014506,5.74544e-06,0.00643918,0.000181724,0.00688266,3.12587e-05,0.00513006,-0.00245959],[0.000594419,-6.52793e-05,1.16468e-05,3.74244e-06,1.70217e-05,-1.59829e-09,1.58929e-05,9.77437e-07,-1.569e-06,3.64877e-07,5.28325e-06,9.20877e-06],[0.000919564,0.000466292,3.74244e-06,0.000179933,9.36591e-05,-9.50298e-09,0.00194968,2.5542e-05,5.64223e-06,1.07179e-05,2.87248e-06,2.36176e-05],[0.00402329,-0.014506,1.70217e-05,9.36591e-05,0.00293726,-8.27095e-08,0.00152854,7.24193e-05,0.000719831,1.66575e-05,2.56411e-05,0.00022562],[-1.06651e-07,5.74544e-06,-1.59829e-09,-9.50297e-09,-8.27095e-08,6.55652e-10,-4.05448e-07,-3.85574e-09,-2.11866e-08,-3.7605e-09,3.09717e-08,6.9764e-09],[0.0156218,0.00643917,1.58928e-05,0.00194968,0.00152854,-4.05448e-07,0.0745273,0.000400905,0.00194065,-2.60228e-05,-0.000176646,0.00111903],[0.000503259,0.000181723,9.77436e-07,2.5542e-05,7.24193e-05,-3.85574e-09,0.000400905,1.83559e-05,7.24687e-05,4.09894e-06,-7.02002e-07,0.000105105],[0.011044,0.00688266,-1.569e-06,5.64224e-06,0.000719831,-2.11866e-08,0.00194065,7.24687e-05,0.00442527,-6.538e-05,4.02153e-05,-0.00189306],[0.000135039,3.12587e-05,3.64877e-07,1.07179e-05,1.66575e-05,-3.7605e-09,-2.60228e-05,4.09894e-06,-6.538e-05,1.45806e-05,-1.3084e-06,-9.94216e-06],[0.00525479,0.00513006,5.28325e-06,2.87249e-06,2.56411e-05,3.09717e-08,-0.000176645,-7.02001e-07,4.02153e-05,-1.3084e-06,0.00105304,-0.000146024],[-0.00170127,-0.00245959,9.20877e-06,2.36176e-05,0.00022562,6.9764e-09,0.00111903,0.000105105,-0.00189306,-9.94216e-06,-0.000146024,0.00330195]]
vc = bioMatrix(12,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
