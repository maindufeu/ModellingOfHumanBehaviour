# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:29 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Sat Nov  4 11:28:29 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',0.0130586,-10000,10000,0,'Beta_time_PT' )

Beta_time_PT_walk = Beta('Beta_time_PT_walk',-0.0329828,-10000,10000,0,'Beta_time_PT_walk' )

Beta_Cost = Beta('Beta_Cost',-0.0952574,-10000,10000,0,'Beta_Cost' )

Beta_Income_PT = Beta('Beta_Income_PT',-7.31222e-05,-10000,10000,0,'Beta_Income_PT' )

ASC_PM  = Beta('ASC_PM ',0.0147862,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.01647,-10000,10000,0,'Beta_time_PM' )

Beta_Income_car = Beta('Beta_Income_car',-4.7692e-05,-10000,10000,0,'Beta_Income_car' )

ASC_SM = Beta('ASC_SM',-0.862769,-10000,10000,0,'ASC_SM' )

Beta_Distance = Beta('Beta_Distance',-0.208489,-10000,10000,0,'Beta_Distance' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Beta_Cost','Beta_Distance','Beta_Income_PT','Beta_Income_car','Beta_time_PM','Beta_time_PT','Beta_time_PT_walk']
values = [[0.0248386,0.0137352,0.000724911,0.000897363,1.07101e-06,-6.10478e-07,9.15799e-05,3.26018e-06,0.000200901],[0.0137352,0.166081,0.000616152,-0.0175621,6.36084e-06,4.95152e-06,-0.000304359,-0.000296918,7.00564e-05],[0.000724911,0.000616152,0.00022632,5.02841e-05,2.34476e-08,-6.97717e-09,6.84671e-06,-1.06015e-05,8.14807e-06],[0.000897363,-0.0175621,5.02841e-05,0.00322738,-9.4152e-08,-7.81642e-08,0.000159197,0.000108074,2.29097e-05],[1.07101e-06,6.36084e-06,2.34476e-08,-9.41521e-08,7.55636e-10,5.77098e-10,8.17531e-09,1.90224e-09,-5.39455e-09],[-6.10478e-07,4.95152e-06,-6.97717e-09,-7.81643e-08,5.77098e-10,6.50509e-10,-8.60005e-09,-3.83864e-09,-1.84549e-09],[9.15799e-05,-0.000304359,6.84671e-06,0.000159197,8.17531e-09,-8.60005e-09,6.03458e-05,3.98071e-05,2.0448e-06],[3.26018e-06,-0.000296918,-1.06015e-05,0.000108074,1.90225e-09,-3.83864e-09,3.98071e-05,3.3319e-05,-5.36603e-06],[0.000200901,7.00564e-05,8.14807e-06,2.29097e-05,-5.39455e-09,-1.84549e-09,2.0448e-06,-5.36603e-06,1.24508e-05]]
vc = bioMatrix(9,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
