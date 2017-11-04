# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:29 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Sat Nov  4 11:42:44 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',0.01288,-10000,10000,0,'Beta_time_PT' )

Beta_time_PT_walk = Beta('Beta_time_PT_walk',-0.0336339,-10000,10000,0,'Beta_time_PT_walk' )

Beta_Cost = Beta('Beta_Cost',-0.0945239,-10000,10000,0,'Beta_Cost' )

Beta_Income = Beta('Beta_Income',-5.57367e-05,-10000,10000,0,'Beta_Income' )

Beta_Age = Beta('Beta_Age',-0.00806024,-10000,10000,0,'Beta_Age' )

ASC_PM  = Beta('ASC_PM ',-0.189337,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.0165368,-10000,10000,0,'Beta_time_PM' )

ASC_SM = Beta('ASC_SM',-0.740076,-10000,10000,0,'ASC_SM' )

Beta_Distance = Beta('Beta_Distance',-0.209659,-10000,10000,0,'Beta_Distance' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Beta_Age','Beta_Cost','Beta_Distance','Beta_Income','Beta_time_PM','Beta_time_PT','Beta_time_PT_walk']
values = [[0.0362463,0.00152597,0.000470797,0.000592552,0.00161598,-9.33165e-08,4.76101e-06,-2.34862e-05,0.000243959],[0.00152597,0.15772,-7.76151e-05,0.000447557,-0.0175411,5.19293e-06,-0.000412544,-0.000331674,9.14543e-05],[0.000470797,-7.76151e-05,9.98637e-06,1.26495e-06,1.30496e-05,-7.61065e-10,7.53425e-07,3.28894e-07,2.71428e-07],[0.000592552,0.000447557,1.26495e-06,0.000218634,5.47283e-05,1.04069e-09,6.44879e-06,-1.0197e-05,9.12841e-06],[0.00161598,-0.0175411,1.30496e-05,5.47283e-05,0.00323439,-8.71803e-08,0.000163458,0.000111001,2.29151e-05],[-9.33165e-08,5.19293e-06,-7.61065e-10,1.04069e-09,-8.71803e-08,6.03638e-10,-4.77617e-09,-2.14171e-09,-2.9557e-09],[4.76101e-06,-0.000412544,7.53425e-07,6.44879e-06,0.000163458,-4.77617e-09,6.14806e-05,4.10768e-05,1.87248e-06],[-2.34862e-05,-0.000331674,3.28894e-07,-1.0197e-05,0.000111001,-2.14171e-09,4.10768e-05,3.43933e-05,-5.47009e-06],[0.000243959,9.14543e-05,2.71428e-07,9.12841e-06,2.29151e-05,-2.9557e-09,1.87248e-06,-5.47009e-06,1.2431e-05]]
vc = bioMatrix(9,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
