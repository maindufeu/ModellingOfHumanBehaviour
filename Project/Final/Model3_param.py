# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:29 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Thu Nov 23 17:35:18 2017</p>
#
ASC_PT = Beta('ASC_PT',-1.1256,-10000,10000,0,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',0.00823547,-10000,10000,0,'Beta_time_PT' )

Beta_time_PT_walk = Beta('Beta_time_PT_walk',-0.0335014,-10000,10000,0,'Beta_time_PT_walk' )

Beta_Cost_age1 = Beta('Beta_Cost_age1',-0.00788147,-10000,10000,0,'Beta_Cost_age1' )

Beta_Cost_age2 = Beta('Beta_Cost_age2',-0.00180526,-10000,10000,0,'Beta_Cost_age2' )

Beta_Cost_age3 = Beta('Beta_Cost_age3',-0.000648953,-10000,10000,0,'Beta_Cost_age3' )

Beta_Age1_PT = Beta('Beta_Age1_PT',2.25718,-10000,10000,0,'Beta_Age1_PT' )

Beta_Age2_PT = Beta('Beta_Age2_PT',-0.0159007,-10000,10000,0,'Beta_Age2_PT' )

Beta_urb = Beta('Beta_urb',0.873923,-10000,10000,0,'Beta_urb' )

Beta_TripWork = Beta('Beta_TripWork',0.32484,-10000,10000,0,'Beta_TripWork' )

Beta_TripLeisure = Beta('Beta_TripLeisure',-0.204178,-10000,10000,0,'Beta_TripLeisure' )

ASC_PM  = Beta('ASC_PM ',-1.00968,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.0201289,-10000,10000,0,'Beta_time_PM' )

Beta_Age1_PM = Beta('Beta_Age1_PM',2.16987,-10000,10000,0,'Beta_Age1_PM' )

Beta_Age2_PM = Beta('Beta_Age2_PM',-0.0118403,-10000,10000,0,'Beta_Age2_PM' )

Beta_roman = Beta('Beta_roman',0.891759,-10000,10000,0,'Beta_roman' )

Beta_Distance = Beta('Beta_Distance',-0.719566,-10000,10000,0,'Beta_Distance' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_PT','Beta_Age1_PM','Beta_Age1_PT','Beta_Age2_PM','Beta_Age2_PT','Beta_Cost_age1','Beta_Cost_age2','Beta_Cost_age3','Beta_Distance','Beta_TripLeisure','Beta_TripWork','Beta_roman','Beta_time_PM','Beta_time_PT','Beta_time_PT_walk','Beta_urb']
values = [[0.191394,0.177298,0.0916596,0.0916905,-0.00243501,-0.00228203,-9.00315e-06,-7.72419e-07,-1.68602e-06,0.0164925,0.00158971,0.00304922,-0.010152,3.48662e-05,6.22845e-05,3.61821e-05,-0.0534029],[0.177298,0.235565,0.0932894,0.0926476,-0.00229031,-0.00258572,2.6657e-05,-1.67547e-07,-2.0741e-05,0.0153043,-0.043311,-0.0343043,-0.0047347,-1.2657e-05,8.67437e-05,-0.000408227,-0.0530189],[0.0916596,0.0932894,0.481152,0.480913,-0.00256151,-0.00263497,-9.22584e-06,-1.27151e-06,-6.95208e-06,-0.00930626,-0.00117088,0.00423745,-0.00290426,-4.37063e-05,-4.12344e-05,1.44813e-05,0.0283225],[0.0916905,0.0926476,0.480913,0.481036,-0.00256388,-0.00263148,-2.91637e-05,-8.70481e-07,-6.66737e-06,-0.00932967,-0.000742873,0.00435801,-0.00257022,-6.15359e-05,-5.29972e-05,1.41546e-05,0.0284033],[-0.00243501,-0.00229031,-0.00256151,-0.00256388,6.33201e-05,5.90007e-05,8.15653e-08,3.70881e-08,-1.58661e-08,8.64119e-06,-5.39136e-06,-1.40986e-05,-2.53781e-05,-6.38329e-07,-3.90901e-07,-4.20754e-08,-0.000133912],[-0.00228203,-0.00258572,-0.00263497,-0.00263148,5.90007e-05,6.79954e-05,3.10271e-07,-4.07729e-07,2.97724e-07,9.05758e-06,9.00199e-05,-7.06552e-05,-4.25392e-05,2.08952e-06,1.92782e-06,7.19738e-08,-0.000174934],[-9.00315e-06,2.6657e-05,-9.22584e-06,-2.91637e-05,8.15653e-08,3.10271e-07,4.66474e-06,-7.6123e-08,1.47875e-08,4.15241e-06,-1.11069e-05,2.01421e-06,-1.02011e-05,3.0036e-06,1.39574e-06,1.63412e-07,-7.72065e-06],[-7.72419e-07,-1.67547e-07,-1.27151e-06,-8.70481e-07,3.70881e-08,-4.07729e-07,-7.6123e-08,1.32874e-07,9.31378e-09,1.22811e-06,3.48314e-06,6.56252e-06,-2.6225e-06,2.83312e-07,-5.63964e-08,1.05557e-07,6.42243e-07],[-1.68602e-06,-2.0741e-05,-6.95208e-06,-6.66737e-06,-1.58661e-08,2.97724e-07,1.47875e-08,9.31378e-09,1.11961e-07,5.98404e-07,-5.30103e-08,3.64955e-06,3.43953e-06,2.66837e-07,-6.99253e-08,3.37781e-07,9.10222e-07],[0.0164925,0.0153043,-0.00930626,-0.00932967,8.64119e-06,9.05758e-06,4.15241e-06,1.22811e-06,5.98404e-07,0.00642351,0.000526738,0.000735396,-0.00033395,0.000119256,8.03003e-05,1.36848e-05,-0.00416605],[0.00158971,-0.043311,-0.00117088,-0.000742873,-5.39136e-06,9.00199e-05,-1.11069e-05,3.48314e-06,-5.30103e-08,0.000526738,0.0473602,0.0344931,0.000430806,-5.63529e-05,-8.5807e-05,0.000194834,-0.000477941],[0.00304922,-0.0343043,0.00423745,0.00435801,-1.40986e-05,-7.06552e-05,2.01421e-06,6.56252e-06,3.64955e-06,0.000735396,0.0344931,0.0440906,-0.000444111,4.06727e-05,-6.18404e-05,0.000204169,0.000689235],[-0.010152,-0.0047347,-0.00290426,-0.00257022,-2.53781e-05,-4.25392e-05,-1.02011e-05,-2.6225e-06,3.43953e-06,-0.00033395,0.000430806,-0.000444111,0.0254453,-9.44455e-05,-6.37766e-05,2.95841e-06,0.00561643],[3.48662e-05,-1.2657e-05,-4.37063e-05,-6.15359e-05,-6.38329e-07,2.08952e-06,3.0036e-06,2.83312e-07,2.66837e-07,0.000119256,-5.63529e-05,4.06727e-05,-9.44455e-05,6.69828e-05,4.38681e-05,3.1589e-06,-1.76059e-05],[6.22845e-05,8.67437e-05,-4.12344e-05,-5.29972e-05,-3.90901e-07,1.92782e-06,1.39574e-06,-5.63964e-08,-6.99253e-08,8.03003e-05,-8.5807e-05,-6.18404e-05,-6.37766e-05,4.38681e-05,3.56245e-05,-4.92212e-06,-1.20809e-05],[3.61821e-05,-0.000408227,1.44813e-05,1.41546e-05,-4.20754e-08,7.19738e-08,1.63412e-07,1.05557e-07,3.37781e-07,1.36848e-05,0.000194834,0.000204169,2.95841e-06,3.1589e-06,-4.92212e-06,1.39217e-05,3.25364e-05],[-0.0534029,-0.0530189,0.0283225,0.0284033,-0.000133912,-0.000174934,-7.72065e-06,6.42243e-07,9.10222e-07,-0.00416605,-0.000477941,0.000689235,0.00561643,-1.76059e-05,-1.20809e-05,3.25364e-05,0.0937433]]
vc = bioMatrix(17,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
