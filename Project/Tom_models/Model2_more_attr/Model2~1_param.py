# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:29 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Sat Nov  4 10:55:31 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',0.000514877,-10000,10000,0,'Beta_time_PT' )

Beta_time_PT_walk = Beta('Beta_time_PT_walk',-0.0330849,-10000,10000,0,'Beta_time_PT_walk' )

Beta_Cost = Beta('Beta_Cost',0.00209324,-10000,10000,0,'Beta_Cost' )

ASC_PM  = Beta('ASC_PM ',0.303749,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.0224402,-10000,10000,0,'Beta_time_PM' )

ASC_SM = Beta('ASC_SM',-0.194819,-10000,10000,0,'ASC_SM' )

Beta_Distance = Beta('Beta_Distance',-0.205361,-10000,10000,0,'Beta_Distance' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Beta_Cost','Beta_Distance','Beta_time_PM','Beta_time_PT','Beta_time_PT_walk']
values = [[0.0111648,0.00339658,2.12771e-05,0.000852298,-2.16836e-05,-1.30195e-05,0.000174523],[0.00339658,0.110588,-2.51602e-05,-0.0166968,-0.000237991,-0.00016287,5.12718e-05],[2.12771e-05,-2.51602e-05,3.03992e-05,3.90833e-05,1.42782e-05,5.58283e-07,1.96025e-06],[0.000852298,-0.0166968,3.90833e-05,0.00309456,9.84871e-05,5.01682e-05,2.75545e-05],[-2.16836e-05,-0.000237991,1.42782e-05,9.84871e-05,3.29606e-05,1.53147e-05,4.48699e-06],[-1.30195e-05,-0.00016287,5.58283e-07,5.01682e-05,1.53147e-05,1.23755e-05,-2.10321e-06],[0.000174523,5.12718e-05,1.96025e-06,2.75545e-05,4.48699e-06,-2.10321e-06,9.62085e-06]]
vc = bioMatrix(7,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
