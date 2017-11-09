# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:29 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Thu Nov  9 21:14:28 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',0.000670054,-10000,10000,0,'Beta_time_PT' )

Beta_time_PT_walk = Beta('Beta_time_PT_walk',-0.0338389,-10000,10000,0,'Beta_time_PT_walk' )

Beta_Cost = Beta('Beta_Cost',-0.000624341,-10000,10000,0,'Beta_Cost' )

ASC_PM  = Beta('ASC_PM ',0.408421,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.0232024,-10000,10000,0,'Beta_time_PM' )

ASC_SM = Beta('ASC_SM',1.22145,-10000,10000,0,'ASC_SM' )

Beta_Distance = Beta('Beta_Distance',-0.659956,-10000,10000,0,'Beta_Distance' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Beta_Cost','Beta_Distance','Beta_time_PM','Beta_time_PT','Beta_time_PT_walk']
values = [[0.0126142,0.00666045,1.07001e-05,0.000519527,-4.15757e-05,-2.22333e-05,0.000201744],[0.00666045,0.0550616,3.36672e-05,-0.0128502,-1.70811e-05,-4.29297e-05,0.000149803],[1.07001e-05,3.36672e-05,3.57236e-05,5.42286e-05,1.72717e-05,9.88025e-07,2.15639e-06],[0.000519527,-0.0128502,5.42286e-05,0.00572507,8.02431e-05,3.52135e-05,1.7872e-05],[-4.15757e-05,-1.70811e-05,1.72717e-05,8.02431e-05,3.81334e-05,1.83931e-05,3.91514e-06],[-2.22333e-05,-4.29297e-05,9.88025e-07,3.52135e-05,1.83931e-05,1.49361e-05,-2.88878e-06],[0.000201744,0.000149803,2.15639e-06,1.7872e-05,3.91514e-06,-2.88878e-06,1.08087e-05]]
vc = bioMatrix(7,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
