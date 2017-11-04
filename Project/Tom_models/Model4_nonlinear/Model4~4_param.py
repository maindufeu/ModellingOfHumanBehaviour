# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:29 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Sat Nov  4 12:44:44 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',0.335623,-10000,10000,0,'Beta_time_PT' )

LAMBDA = Beta('LAMBDA',0.200322,-10000,10000,0,'LAMBDA' )

Beta_time_PT_walk = Beta('Beta_time_PT_walk',-0.0378342,-10000,10000,0,'Beta_time_PT_walk' )

Beta_Cost = Beta('Beta_Cost',-0.0996676,-10000,10000,0,'Beta_Cost' )

Beta_Income = Beta('Beta_Income',-7.15841e-05,-10000,10000,0,'Beta_Income' )

Beta_Age = Beta('Beta_Age',-0.00513603,-10000,10000,0,'Beta_Age' )

ASC_PM  = Beta('ASC_PM ',0.878158,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.0178051,-10000,10000,0,'Beta_time_PM' )

ASC_SM = Beta('ASC_SM',-0.204956,-10000,10000,0,'ASC_SM' )

Beta_Distance = Beta('Beta_Distance',-0.188447,-10000,10000,0,'Beta_Distance' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Beta_Age','Beta_Cost','Beta_Distance','Beta_Income','Beta_time_PM','Beta_time_PT','Beta_time_PT_walk','LAMBDA']
values = [[0.0858462,0.0304466,0.000684837,0.00101815,0.00411192,-1.55308e-07,0.000686161,0.00994853,0.000137858,0.00269814],[0.0304466,0.159306,-6.80371e-05,0.000761094,-0.0116287,4.82156e-06,0.000365817,0.00626187,5.94164e-05,0.00105428],[0.000684837,-6.80371e-05,1.32139e-05,-1.33438e-07,1.28803e-05,-4.26902e-09,7.37656e-07,3.47144e-06,3.71672e-08,1.33497e-05],[0.00101815,0.000761094,-1.33438e-07,0.000247798,0.000130412,-4.69318e-10,3.50014e-05,2.91123e-05,1.47845e-05,0.000127265],[0.00411192,-0.0116287,1.28803e-05,0.000130412,0.00268232,5.91644e-08,9.2836e-05,0.000693423,1.82958e-05,0.000493849],[-1.55308e-07,4.82156e-06,-4.26902e-09,-4.69318e-10,5.91644e-08,6.18434e-10,-8.6766e-10,1.71254e-08,-2.54395e-09,8.86826e-09],[0.000686161,0.000365817,7.37656e-07,3.50014e-05,9.2836e-05,-8.6766e-10,2.67225e-05,9.08425e-05,4.58184e-06,0.000195753],[0.00994853,0.00626187,3.47144e-06,2.91123e-05,0.000693423,1.71254e-08,9.08425e-05,0.00386205,-5.4451e-05,-0.00132879],[0.000137858,5.94164e-05,3.71672e-08,1.47845e-05,1.82958e-05,-2.54395e-09,4.58184e-06,-5.4451e-05,1.36587e-05,-1.18467e-05],[0.00269814,0.00105428,1.33497e-05,0.000127265,0.000493849,8.86826e-09,0.000195753,-0.00132879,-1.18467e-05,0.00403156]]
vc = bioMatrix(10,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
