# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:29 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Sat Nov  4 12:29:54 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',0.331359,-10000,10000,0,'Beta_time_PT' )

LAMBDA = Beta('LAMBDA',0.201759,-10000,10000,0,'LAMBDA' )

Beta_time_PT_walk = Beta('Beta_time_PT_walk',-0.0372066,-10000,10000,0,'Beta_time_PT_walk' )

Beta_Cost = Beta('Beta_Cost',-0.0913319,-10000,10000,0,'Beta_Cost' )

Beta_Income = Beta('Beta_Income',-5.8618e-05,-10000,10000,0,'Beta_Income' )

Beta_Age = Beta('Beta_Age',-0.00727272,-10000,10000,0,'Beta_Age' )

Beta_typeBus = Beta('Beta_typeBus',-0.113874,-10000,10000,0,'Beta_typeBus' )

ASC_PM  = Beta('ASC_PM ',0.231286,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.0182568,-10000,10000,0,'Beta_time_PM' )

ASC_SM = Beta('ASC_SM',-0.560301,-10000,10000,0,'ASC_SM' )

Beta_Distance = Beta('Beta_Distance',-0.195672,-10000,10000,0,'Beta_Distance' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Beta_Age','Beta_Cost','Beta_Distance','Beta_Income','Beta_time_PM','Beta_time_PT','Beta_time_PT_walk','Beta_typeBus','LAMBDA']
values = [[0.0997666,0.0553563,0.000526716,0.00103324,0.0041102,1.03151e-07,0.000637986,0.0102669,0.000143617,0.00512052,0.000678709],[0.0553563,0.189701,-6.25773e-05,0.000651155,-0.0126516,5.34222e-06,0.000297894,0.006668,4.17399e-05,0.005299,-0.000639333],[0.000526716,-6.25773e-05,1.01636e-05,2.95451e-06,1.73758e-05,-2.05248e-09,1.25465e-06,8.5203e-07,3.5283e-07,3.82671e-06,1.2197e-05],[0.00103324,0.000651155,2.95451e-06,0.000204046,0.000110429,-8.38125e-10,2.79471e-05,1.20537e-05,1.26168e-05,1.53404e-05,9.20128e-05],[0.0041102,-0.0126516,1.73758e-05,0.000110429,0.00270989,-5.786e-08,8.85282e-05,0.000682602,1.95581e-05,-7.7603e-06,0.000431148],[1.03151e-07,5.34222e-06,-2.05248e-09,-8.38125e-10,-5.786e-08,6.07882e-10,-1.67543e-09,7.54866e-09,-3.14722e-09,3.02051e-08,1.41703e-08],[0.000637986,0.000297894,1.25465e-06,2.79471e-05,8.85282e-05,-1.67543e-09,2.48708e-05,8.23821e-05,5.10154e-06,-1.18149e-06,0.000174558],[0.0102669,0.006668,8.5203e-07,1.20537e-05,0.000682602,7.54866e-09,8.23821e-05,0.00392677,-4.85249e-05,6.91364e-05,-0.00155752],[0.000143617,4.17399e-05,3.5283e-07,1.26168e-05,1.95581e-05,-3.14722e-09,5.10154e-06,-4.85249e-05,1.32631e-05,-3.51088e-06,-6.99837e-06],[0.00512052,0.005299,3.82671e-06,1.53404e-05,-7.7603e-06,3.02051e-08,-1.18149e-06,6.91364e-05,-3.51088e-06,0.00101235,-0.000163202],[0.000678709,-0.000639333,1.2197e-05,9.20128e-05,0.000431148,1.41703e-08,0.000174558,-0.00155752,-6.99837e-06,-0.000163202,0.00389419]]
vc = bioMatrix(11,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
