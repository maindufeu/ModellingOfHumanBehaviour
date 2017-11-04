# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:29 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Sat Nov  4 11:33:44 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',0.012832,-10000,10000,0,'Beta_time_PT' )

Beta_time_PT_walk = Beta('Beta_time_PT_walk',-0.0331905,-10000,10000,0,'Beta_time_PT_walk' )

Beta_Cost = Beta('Beta_Cost',-0.0933492,-10000,10000,0,'Beta_Cost' )

Beta_Income = Beta('Beta_Income',-5.67913e-05,-10000,10000,0,'Beta_Income' )

Beta_Age = Beta('Beta_Age',0.00759167,-10000,10000,0,'Beta_Age' )

ASC_PM  = Beta('ASC_PM ',0.198701,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.016299,-10000,10000,0,'Beta_time_PM' )

ASC_SM = Beta('ASC_SM',-0.37797,-10000,10000,0,'ASC_SM' )

Beta_Distance = Beta('Beta_Distance',-0.209794,-10000,10000,0,'Beta_Distance' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Beta_Age','Beta_Cost','Beta_Distance','Beta_Income','Beta_time_PM','Beta_time_PT','Beta_time_PT_walk']
values = [[0.0135592,0.00456346,-7.19634e-06,0.000512187,0.000985126,-5.01456e-08,-2.75383e-05,-4.0472e-05,0.000226094],[0.00456346,0.265951,0.00193623,0.000454266,-0.0210574,5.04345e-06,-0.000520304,-0.000413779,8.24642e-05],[-7.19634e-06,0.00193623,3.25619e-05,6.17617e-08,-7.31262e-05,2.16363e-09,-2.4527e-06,-1.74413e-06,-2.49277e-07],[0.000512187,0.000454266,6.17617e-08,0.000218269,4.81222e-05,1.25408e-09,4.48707e-06,-1.1352e-05,8.66287e-06],[0.000985126,-0.0210574,-7.31262e-05,4.81222e-05,0.00327291,-6.57281e-08,0.000161705,0.000109891,2.2472e-05],[-5.01456e-08,5.04345e-06,2.16363e-09,1.25408e-09,-6.57281e-08,5.87446e-10,-4.02012e-09,-1.67731e-09,-2.69191e-09],[-2.75383e-05,-0.000520304,-2.4527e-06,4.48707e-06,0.000161705,-4.02012e-09,6.03933e-05,4.01971e-05,2.18239e-06],[-4.0472e-05,-0.000413779,-1.74413e-06,-1.1352e-05,0.000109891,-1.67731e-09,4.01971e-05,3.35668e-05,-5.25836e-06],[0.000226094,8.24642e-05,-2.49277e-07,8.66287e-06,2.2472e-05,-2.69191e-09,2.18239e-06,-5.25836e-06,1.23735e-05]]
vc = bioMatrix(9,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
