# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:29 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Sat Nov  4 11:26:12 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',0.0128529,-10000,10000,0,'Beta_time_PT' )

Beta_time_PT_walk = Beta('Beta_time_PT_walk',-0.0332403,-10000,10000,0,'Beta_time_PT_walk' )

Beta_Cost = Beta('Beta_Cost',-0.0934346,-10000,10000,0,'Beta_Cost' )

Beta_Income = Beta('Beta_Income',-5.42148e-05,-10000,10000,0,'Beta_Income' )

ASC_PM  = Beta('ASC_PM ',0.196207,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.0162874,-10000,10000,0,'Beta_time_PM' )

ASC_SM = Beta('ASC_SM',-0.730183,-10000,10000,0,'ASC_SM' )

Beta_Distance = Beta('Beta_Distance',-0.208112,-10000,10000,0,'Beta_Distance' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Beta_Cost','Beta_Distance','Beta_Income','Beta_time_PM','Beta_time_PT','Beta_time_PT_walk']
values = [[0.0136142,0.00464121,0.000515166,0.00102035,-5.9876e-08,-2.62722e-05,-3.99095e-05,0.000227343],[0.00464121,0.157862,0.000442659,-0.0174165,5.34067e-06,-0.000402509,-0.000328521,8.87623e-05],[0.000515166,0.000442659,0.000218541,4.93704e-05,9.50528e-10,4.53934e-06,-1.13335e-05,8.72146e-06],[0.00102035,-0.0174165,4.93704e-05,0.00322878,-7.53206e-08,0.000160327,0.000108712,2.32009e-05],[-5.9876e-08,5.34067e-06,9.50528e-10,-7.53206e-08,6.27904e-10,-4.85165e-09,-2.2327e-09,-2.89211e-09],[-2.62722e-05,-0.000402509,4.53934e-06,0.000160327,-4.85165e-09,6.03462e-05,4.01627e-05,2.20093e-06],[-3.99095e-05,-0.000328521,-1.13335e-05,0.000108712,-2.2327e-09,4.01627e-05,3.3541e-05,-5.24942e-06],[0.000227343,8.87623e-05,8.72146e-06,2.32009e-05,-2.89211e-09,2.20093e-06,-5.24942e-06,1.23994e-05]]
vc = bioMatrix(8,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
