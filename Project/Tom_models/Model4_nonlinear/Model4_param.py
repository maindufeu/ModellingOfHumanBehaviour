# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:29 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Sat Nov  4 12:18:41 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',0.335183,-10000,10000,0,'Beta_time_PT' )

LAMBDA = Beta('LAMBDA',0.192777,-10000,10000,0,'LAMBDA' )

Beta_time_PT_walk = Beta('Beta_time_PT_walk',-0.0381508,-10000,10000,0,'Beta_time_PT_walk' )

Beta_Cost = Beta('Beta_Cost',-0.0912782,-10000,10000,0,'Beta_Cost' )

Beta_Income = Beta('Beta_Income',-5.70995e-05,-10000,10000,0,'Beta_Income' )

Beta_Age = Beta('Beta_Age',-0.00690679,-10000,10000,0,'Beta_Age' )

ASC_PM  = Beta('ASC_PM ',0.792133,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.0182548,-10000,10000,0,'Beta_time_PM' )

ASC_SM = Beta('ASC_SM',-0.0125103,-10000,10000,0,'ASC_SM' )

Beta_Distance = Beta('Beta_Distance',-0.195292,-10000,10000,0,'Beta_Distance' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Beta_Age','Beta_Cost','Beta_Distance','Beta_Income','Beta_time_PM','Beta_time_PT','Beta_time_PT_walk','LAMBDA']
values = [[0.0742879,0.0284311,0.000506691,0.000953466,0.00419138,-1.08374e-07,0.000677516,0.00988389,0.000157267,0.00229243],[0.0284311,0.16075,-7.54689e-05,0.000583991,-0.0125826,5.096e-06,0.000325332,0.00597185,5.91252e-05,0.000903453],[0.000506691,-7.54689e-05,1.00532e-05,2.5566e-06,1.67574e-05,-2.06055e-09,1.34033e-06,2.91684e-06,3.12358e-07,1.28041e-05],[0.000953466,0.000583991,2.5566e-06,0.000198734,0.000109685,-1.10801e-09,2.75796e-05,1.27667e-05,1.31763e-05,9.10496e-05],[0.00419138,-0.0125826,1.67574e-05,0.000109685,0.00271747,-5.90764e-08,8.92727e-05,0.000722525,1.95171e-05,0.000429321],[-1.08374e-07,5.096e-06,-2.06055e-09,-1.10801e-09,-5.90764e-08,6.02387e-10,-1.93506e-09,-5.10324e-09,-2.98325e-09,1.69371e-08],[0.000677516,0.000325332,1.34033e-06,2.75796e-05,8.92727e-05,-1.93506e-09,2.47694e-05,9.69173e-05,4.96894e-06,0.000168019],[0.00988389,0.00597185,2.91684e-06,1.27667e-05,0.000722525,-5.10324e-09,9.69173e-05,0.00378997,-5.13341e-05,-0.00115752],[0.000157267,5.91252e-05,3.12358e-07,1.31763e-05,1.95171e-05,-2.98325e-09,4.96894e-06,-5.13341e-05,1.33276e-05,-7.81008e-06],[0.00229243,0.000903453,1.28041e-05,9.10496e-05,0.000429321,1.69371e-08,0.000168019,-0.00115752,-7.81008e-06,0.00350102]]
vc = bioMatrix(10,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
