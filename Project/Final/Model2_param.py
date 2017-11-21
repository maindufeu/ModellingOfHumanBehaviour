# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:39 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Tue Nov 21 17:09:05 2017</p>
#
ASC_PT = Beta('ASC_PT',-1.22145,-10000,10000,0,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',0.00067006,-10000,10000,0,'Beta_time_PT' )

Beta_time_PT_walk = Beta('Beta_time_PT_walk',-0.0338389,-10000,10000,0,'Beta_time_PT_walk' )

Beta_Cost = Beta('Beta_Cost',-0.000624367,-10000,10000,0,'Beta_Cost' )

ASC_PM  = Beta('ASC_PM ',-0.813034,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.0232024,-10000,10000,0,'Beta_time_PM' )

Beta_Distance = Beta('Beta_Distance',-0.659961,-10000,10000,0,'Beta_Distance' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_PT','Beta_Cost','Beta_Distance','Beta_time_PM','Beta_time_PT','Beta_time_PT_walk']
values = [[0.0543553,0.0484016,-2.29661e-05,0.0133699,-2.44941e-05,2.06965e-05,5.19416e-05],[0.0484016,0.0550621,-3.36663e-05,0.0128504,1.70816e-05,4.29299e-05,-0.000149803],[-2.29661e-05,-3.36663e-05,3.57237e-05,5.42293e-05,1.72718e-05,9.88007e-07,2.1564e-06],[0.0133699,0.0128504,5.42293e-05,0.00572524,8.02435e-05,3.52136e-05,1.78722e-05],[-2.44941e-05,1.70816e-05,1.72718e-05,8.02435e-05,3.81334e-05,1.83931e-05,3.91514e-06],[2.06965e-05,4.29299e-05,9.88007e-07,3.52136e-05,1.83931e-05,1.49362e-05,-2.88878e-06],[5.19416e-05,-0.000149803,2.1564e-06,1.78722e-05,3.91514e-06,-2.88878e-06,1.08087e-05]]
vc = bioMatrix(7,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
