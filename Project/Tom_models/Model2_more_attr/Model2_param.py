# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:29 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Sat Nov  4 10:54:54 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',0.00366499,-10000,10000,0,'Beta_time_PT' )

Beta_time_PT_walk = Beta('Beta_time_PT_walk',-0.0286547,-10000,10000,0,'Beta_time_PT_walk' )

Beta_time_PT_wait = Beta('Beta_time_PT_wait',-0.0512377,-10000,10000,0,'Beta_time_PT_wait' )

Beta_Cost = Beta('Beta_Cost',0.00189418,-10000,10000,0,'Beta_Cost' )

ASC_PM  = Beta('ASC_PM ',0.424403,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.0221626,-10000,10000,0,'Beta_time_PM' )

ASC_SM = Beta('ASC_SM',-0.0886738,-10000,10000,0,'ASC_SM' )

Beta_Distance = Beta('Beta_Distance',-0.203642,-10000,10000,0,'Beta_Distance' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Beta_Cost','Beta_Distance','Beta_time_PM','Beta_time_PT','Beta_time_PT_wait','Beta_time_PT_walk']
values = [[0.0125527,0.00428644,4.65471e-05,0.00101199,2.63478e-05,5.66895e-05,-8.42212e-05,0.000224729],[0.00428644,0.11007,-4.32714e-06,-0.0163996,-0.000197176,-0.000114218,-9.76808e-05,7.60232e-05],[4.65471e-05,-4.32714e-06,2.97989e-05,3.79542e-05,1.34912e-05,7.4098e-07,-1.3601e-06,2.7455e-06],[0.00101199,-0.0163996,3.79542e-05,0.00307526,0.000101358,5.63577e-05,-4.07963e-07,3.51043e-05],[2.63478e-05,-0.000197176,1.34912e-05,0.000101358,3.43217e-05,1.73828e-05,-2.6675e-06,6.59192e-06],[5.66895e-05,-0.000114218,7.4098e-07,5.63577e-05,1.73828e-05,1.59747e-05,-1.55028e-05,5.16836e-07],[-8.42212e-05,-9.76808e-05,-1.3601e-06,-4.07963e-07,-2.6675e-06,-1.55028e-05,6.9385e-05,-5.02438e-07],[0.000224729,7.60232e-05,2.7455e-06,3.51043e-05,6.59192e-06,5.16836e-07,-5.02438e-07,1.17565e-05]]
vc = bioMatrix(8,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
