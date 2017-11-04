# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:29 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Sat Nov  4 10:43:19 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',-0.00910723,-10000,10000,0,'Beta_time_PT' )

Beta_Cost = Beta('Beta_Cost',0.0342206,-10000,10000,0,'Beta_Cost' )

ASC_PM  = Beta('ASC_PM ',0.787024,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.00819562,-10000,10000,0,'Beta_time_PM' )

ASC_SM = Beta('ASC_SM',-1.84601,-10000,10000,0,'ASC_SM' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Beta_Cost','Beta_time_PM','Beta_time_PT']
values = [[0.00861208,0.0077279,-0.000259625,-2.62816e-06,8.85496e-05],[0.0077279,0.0319777,4.26084e-05,0.000206852,0.000121278],[-0.000259625,4.26084e-05,4.92201e-05,1.05953e-06,-9.00228e-06],[-2.62816e-06,0.000206852,1.05953e-06,2.87107e-06,8.11933e-07],[8.85496e-05,0.000121278,-9.00228e-06,8.11933e-07,2.38001e-06]]
vc = bioMatrix(5,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
