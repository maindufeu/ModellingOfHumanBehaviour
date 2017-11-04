# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:29 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Sat Nov  4 11:34:51 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',0.0128995,-10000,10000,0,'Beta_time_PT' )

Beta_time_PT_walk = Beta('Beta_time_PT_walk',-0.0336111,-10000,10000,0,'Beta_time_PT_walk' )

Beta_Cost = Beta('Beta_Cost',-0.0944239,-10000,10000,0,'Beta_Cost' )

Beta_Income = Beta('Beta_Income',-5.36824e-05,-10000,10000,0,'Beta_Income' )

Beta_Age = Beta('Beta_Age',-0.00693683,-10000,10000,0,'Beta_Age' )

ASC_PM  = Beta('ASC_PM ',-0.136494,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.0164925,-10000,10000,0,'Beta_time_PM' )

ASC_SM = Beta('ASC_SM',-1.06597,-10000,10000,0,'ASC_SM' )

Beta_Distance = Beta('Beta_Distance',-0.208037,-10000,10000,0,'Beta_Distance' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Beta_Age','Beta_Cost','Beta_Distance','Beta_Income','Beta_time_PM','Beta_time_PT','Beta_time_PT_walk']
values = [[0.0387252,0.0329458,0.000534362,0.00058452,0.000792911,7.20083e-08,-1.77298e-05,-4.35927e-05,0.00023983],[0.0329458,0.189516,0.000598574,0.000518221,-0.0175904,5.51545e-06,-0.000389878,-0.000332237,0.000106844],[0.000534362,0.000598574,1.15492e-05,1.1348e-06,-4.56885e-06,2.51355e-09,2.69401e-07,-9.19952e-08,1.93686e-07],[0.00058452,0.000518221,1.1348e-06,0.0002187,5.14321e-05,1.49334e-09,6.09947e-06,-1.04175e-05,9.07393e-06],[0.000792911,-0.0175904,-4.56885e-06,5.14321e-05,0.00323171,-6.89665e-08,0.000161871,0.000110332,2.22746e-05],[7.20083e-08,5.51545e-06,2.51355e-09,1.49334e-09,-6.89665e-08,6.3611e-10,-4.55426e-09,-2.05964e-09,-2.5889e-09],[-1.77298e-05,-0.000389878,2.69401e-07,6.09947e-06,0.000161871,-4.55426e-09,6.12432e-05,4.09079e-05,1.88695e-06],[-4.35927e-05,-0.000332237,-9.19952e-08,-1.04175e-05,0.000110332,-2.05964e-09,4.09079e-05,3.42588e-05,-5.46363e-06],[0.00023983,0.000106844,1.93686e-07,9.07393e-06,2.22746e-05,-2.5889e-09,1.88695e-06,-5.46363e-06,1.2426e-05]]
vc = bioMatrix(9,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
